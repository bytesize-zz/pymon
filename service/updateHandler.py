"""
    update Handler

    Responsible for every inquiry to the esipy api and timed updates from eve

"""
import swagger_client
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtCore import QUrl

import config
import threading
import skilldump

from db.databaseHandler import DatabaseHandler
from db.databaseTables import User, Character, CharacterPortrait, SkillQueue, CompletedSkillList, CharacterAttributes

from service.esipy.app import App
from service.esipy.security import EsiSecurity

class UpdateHandler():
    def __init__(self, parent=None):
        super(UpdateHandler, self).__init__()

        esiapp = App.create(config.ESI_SWAGGER_JSON)

        # init the security object
        self.esisecurity = EsiSecurity(
            app=esiapp,
            redirect_uri=config.ESI_CALLBACK,
            client_id=config.ESI_CLIENT_ID,
            secret_key=config.ESI_SECRET_KEY,
        )


        self.dbHandler = DatabaseHandler()
        #self.dbHandler.initSession()

    def calculateTimeDifference(self):
        config.TIME_DIFFERENCE = 0

    def getServerStatus(self):
        # GET /status/
        print("x")

    def setApiDetails(self, api, user):

        api.api_client.set_default_header(config.ESI_USER_AGENT, config.ESI_AGENT_DESCRIPTION)
        api.api_client.host = config.ESI_ESI_URL
        api.api_client.configuration.access_token = user.AccessToken

        return api

    def updateAll(self):
        """ Method to update Data for all stored Users.

        """

        # If we have'nt yet, we get the Static Informations for Skills/Ships etc from Eve
        # ToDo: Get Ship Dump and implement a real update function
        if self.dbHandler.staticDumpPresent() == False:
            #print("No Skill Dump present, lets get it ... ")
            dumpThread = threading.Thread(target=self.getSkilldump)
            dumpThread.daemon = True
            dumpThread.start()

        try:
            userList = self.dbHandler.getAllUser()
            for user in userList:
                self.updateUser(user)
        except Exception as e:
            print(e)

    def getSkilldump(self):
        skilldump.SkillDump()

    def updateUser(self, user):
        """ Method to update Data for one stored User.

            1. refresh the Authentication
            2. ask EvE API for new Data
        """
        self.refreshUserAuth(user)
        self.updateCharacter(user)
        self.updateBalance(user)
        self.updatePortrait(user)
        self.updateSkillQueue(user)
        self.updateCompletedSkills(user)
        self.updateCharacterAttributes(user)


        #self.getStructureDetails(user)


    def refreshUserAuth(self, user):
        """ Get a new Access Token based on Refresh Token.

        Feeding the esipy with Datas from the Database and ask if AcessToken is expired.
        If so, we refresh the Auth, store the New Tokens in user Class and write them to the Database

        :param user: Stored User Class from Database
        """

        #print("Starting Auth refresh for " + user.CharacterName)
        self.esisecurity.set_token(user.AccessToken, user.RefreshToken, user.AccessTokenExpire)

        if self.esisecurity.is_token_expired() == True:
            #print("Access Token is expired, getting a new one ...")
            user.update_token(self.esisecurity.refresh())
            #print("Saving new Token in th DB")
            self.dbHandler.saveUser(user)
        else:
            print("Access Token valid, nothing to do")


    def updateCharacter(self, user):

        api = swagger_client.CharacterApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id(user.CharacterID)
            char = Character().setCharacter(response, user.get_id())  # create an databaseTables Object of Character
            self.dbHandler.saveCharacter(char)
        except Exception as e:
            print("Exception in updateHandler.updateCharacter(): %s\n" % e)

    def updateBalance(self, user):

        api = swagger_client.WalletApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_wallet(user.CharacterID)
            self.dbHandler.saveCharacterBalance(response, user.get_id())
        except Exception as e:
            print(e)

    def updatePortrait(self, user):

        api = swagger_client.CharacterApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_portrait(user.CharacterID)
            portrait = CharacterPortrait().setCharacterPortrait(response, user.get_id())
            self.dbHandler.saveCharacterPortrait(portrait)

        except Exception as e:
            print("Exception in updateHandler.updatePortrait(): %s\n" % e)

    def downloadPortraits(self, user):
        #ToDo: finalize this
        netwManager = QNetworkAccessManager()
        url = QUrl()

    def updateSkillQueue(self, user):

        api = swagger_client.SkillsApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_skillqueue(user.CharacterID)
            if len(response) > 0:
                # Create a SkillQueue Object, containing list of Skills and the owner ID
                skillQueue = SkillQueue().createSkillQueue(response, user.get_id())
                # Saving the Skill Queue
                self.dbHandler.saveSkillQueue(skillQueue)
            else:
                print(user.CharacterName + " has an Empty Skillqueue")
        except Exception as e:
            print("Exception in updateHandler.updateSkillqueue(): %s\n" % e)

    def updateCompletedSkills(self, user):
        """ Update the completed Skills
        Since we get a List of completed Skills and the Skillpoint values, we need to split where we save them
        The Skills go in the CompletedSkillItems DB.
        The Skillpoint values will be added to the character Table

        :param user: Stored User Class from Database
        """

        api = swagger_client.SkillsApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_skills(user.CharacterID)
            skillList = CompletedSkillList().createCSL(response, user.get_id())
            self.dbHandler.saveCompletedSkills(skillList)
            self.dbHandler.saveCharacterSP(user.get_id(), response.total_sp, response.unallocated_sp)
        except Exception as e:
            print(e)

    def updateCharacterAttributes(self, user):

        api = swagger_client.SkillsApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_attributes(user.CharacterID)
            charAttributes = CharacterAttributes().create(response, user.get_id())
            self.dbHandler.saveCharacterAttributes(charAttributes)
        except Exception as e:
            print(e)

    def updateAlliName(self, user):

        api = swagger_client.AllianceApi()
        api = self.setApiDetails(api)

        char = self.dbHandler.getCharacter(user.id)

        try:
            response = api.get_alliances_alliance_id(char.alliance_id)
            print(response.name)
        except Exception as e:
            print("Exception in UpdateHandler.updateAlliName: " + str(e))


    def getCharacterNotifications(self, user):

        api = swagger_client.CharacterApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_notifications(user.CharacterID)
            #notifications = Charac().createCSL(response, user.get_id())
            #self.dbHandler.saveCompletedSkills(skillList)
            self.dbHandler.saveCharacterSP(user.get_id(), response.total_sp, response.unallocated_sp)
        except Exception as e:
            print(e)

    def getStructureDetails(self, user):
        # Test Function for getting Corp Structures, specially remaining structure fuel/time
        api = swagger_client.CorporationApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_corporations_corporation_id_structures(573400667)
            print(response)
            print(response.data)
        except Exception as e:
            print(e)
