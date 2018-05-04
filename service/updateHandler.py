"""
    update Handler

    Responsible for every inquiry to the esipy api and timed updates from eve

"""
import swagger_client
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtCore import QUrl, QTimer

import config
import threading
import skilldump
import datetime
import time

from db.databaseHandler import DatabaseHandler
from db.databaseTables import User, Character, CharacterPortrait, SkillQueue, CompletedSkillList, CharacterAttributes, \
    CharacterNotifications, ServerStatus

from service.esipy.app import App
from service.esipy.security import EsiSecurity

class UpdateHandler():
    def __init__(self, parent=None):
        super(UpdateHandler, self).__init__()

        esiapp = App.create(config.ESI_SWAGGER_JSON)

        self.clientStartTime = datetime.datetime.now()

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

    def setApiDetails(self, api, user):

        api.api_client.set_default_header(config.ESI_USER_AGENT, config.ESI_AGENT_DESCRIPTION)
        api.api_client.host = config.ESI_ESI_URL
        api.api_client.configuration.access_token = user.AccessToken

        return api

    def updateAll(self, gui_queue):
        """ Method to update Data for all stored Users.

        """

        self.updateServerStatus()

        # If we have'nt yet, we get the Static Informations for Skills/Ships etc from Eve
        # ToDo: Get Ship Dump and implement a real update function
        if self.dbHandler.staticDumpPresent() == False:
            print("No Skill Dump present ... ")
            #dumpThread = threading.Thread(target=self.getSkilldump)
            #dumpThread.daemon = True
            #dumpThread.start()

        try:
            self.userList = self.dbHandler.getAllUser()
            for user in self.userList:
                self.updateUser(user)
        except Exception as e:
            print("Exception in updateHandler.updateAll: %s\n" % e)
        finally:
            gui_queue.put("Reprint MainWindow")

        self.updateLoop()


    def updateLoop(self):
        while True:
            self.frequentlyUpdate()
            time.sleep(1)

    def frequentlyUpdate(self):
        # Get a new Server Status every Minute

        now = datetime.datetime.now()
        clientRunTime = int((now - self.clientStartTime).total_seconds())


        if (clientRunTime % 60) == 0:   # minutely Update
            # Server Status
            self.updateServerStatus()
        if (clientRunTime % 300) == 0:  # 5 minutely Update
            print("5 Min Update now")
            # Jump Fatigue
            # Balance
            # Notifications
            for user in self.userList:
                self.refreshUserAuth(user)
                self.updateBalance(user)
                self.updateCharacterNotifications(user)
        if (clientRunTime % 900) == 0:  # 15 minutely Update
            print("15 Min Update now")

        if (clientRunTime % 1800) == 0:  # 30 minutely Update
            print("30 Min Update now")
            # Skill Queue
            # Completed Skills
            # Attributes
            for user in self.userList:
                self.updateSkillQueue(user)
                self.updateCompletedSkills(user)
                self.updateCharacterAttributes(user)
        if (clientRunTime % 3600) == 0:  # 60 minutely Update
            print("60 Min Update now")
            # Skill Points
            # Corp History


    def getSkilldump(self):
        #skilldump.SkillDump()
        skilldump.ShipDump()

    def updateUser(self, user):
        """ Method to update Data for one stored User.

            1. refresh the Authentication
            2. ask EvE API for new Data
        """
        #if self.getServerStatus() is not None:
        self.refreshUserAuth(user)
        self.updateCharacter(user)
        self.updateBalance(user)
        self.updatePortrait(user)
        self.updateSkillQueue(user)
        self.updateCompletedSkills(user)
        self.updateCharacterAttributes(user)
        self.updateCharacterNotifications(user)

        #self.getStructureDetails(user)


    def refreshUserAuth(self, user):
        """ Get a new Access Token based on Refresh Token.

        Feeding the esipy with Datas from the Database and ask if AcessToken is expired.
        If so, we refresh the Auth, store the New Tokens in user Class and write them to the Database

        :param user: Stored User Class from Database
        """
        try:
            self.esisecurity.set_token(user.AccessToken, user.RefreshToken, user.AccessTokenExpire)

            if self.esisecurity.is_token_expired() is True:
                user.update_token(self.esisecurity.refresh())
                self.dbHandler.saveUser(user)
            else:
                print("Access Token valid, nothing to do")
        except Exception as e:
            print("Exception in updateHandler.refreshUserAuth: %s\n" % e)



    def updateServerStatus(self):

        api = swagger_client.StatusApi()
        api.api_client.set_default_header(config.ESI_USER_AGENT, config.ESI_AGENT_DESCRIPTION)
        api.api_client.host = config.ESI_ESI_URL
        status = None

        try:
            response = api.get_status()
            now = datetime.datetime.utcnow()
            status = ServerStatus().setStatus(response, now)
            # ToDo: Handle 502 Exception differently as is only means that server is offline
        except Exception as e:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            print("Exception in updateHandler.getServerStatus: %s\n" % e)

            status = ServerStatus().setStatus(None, None)
        finally:

            self.dbHandler.saveServerStatus(status)

    def updateCharacter(self, user):

        api = swagger_client.CharacterApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id(user.CharacterID)
            char = Character().setCharacter(response, user.get_id())  # create an databaseTables Object of Character
            self.dbHandler.saveCharacter(char)
            #self.updateAllianceName(char)
            #self.updateCorporationName(char)
        except Exception as e:
            print("Exception in updateHandler.updateCharacter(): %s\n" % e)

    def updateBalance(self, user):

        api = swagger_client.WalletApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_wallet(user.CharacterID)
            self.dbHandler.saveCharacterBalance(response, user.get_id())
        except Exception as e:
            print("Exception in updateHandler.updateBalance(): %s\n" % e)

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
            print("Exception in updateHandler.updateCompletedSkills: %s\n" % e)

    def updateCharacterAttributes(self, user):

        api = swagger_client.SkillsApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_attributes(user.CharacterID)
            charAttributes = CharacterAttributes().create(response, user.get_id())
            self.dbHandler.saveCharacterAttributes(charAttributes)
        except Exception as e:
            print("Exception in updateHandler.updateCharacterAttributes(): %s\n" % e)

    def updateAllianceName(self, char):

        api = swagger_client.AllianceApi()
        api = self.setApiDetails(api)

        try:
            response = api.get_alliances_alliance_id(char.alliance_id)
            print(response)
        except Exception as e:
            print("Exception in UpdateHandler.updateAllianceName: " + str(e))

    def updateCorporationName(self, char):

        api = swagger_client.CorporationApi()
        api = self.setApiDetails(api)

        try:
            response = api.get_alliances_alliance_id(char.corporation_id)
            print(response)
        except Exception as e:
            print("Exception in UpdateHandler.updateCorporationName: " + str(e))


    def updateCharacterNotifications(self, user):

        api = swagger_client.CharacterApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_characters_character_id_notifications(user.CharacterID)
            notifications = []
            for item in response:
                new = CharacterNotifications().create(item, user.id)
                notifications.append(new)
                self.dbHandler.saveCharacterNotification(new)
        except Exception as e:
            print("Exception in updateHandler.getCharacterNotifications: %s\n" % e)

    def getStructureDetails(self, user):
        # Test Function for getting Corp Structures, specially remaining structure fuel/time
        api = swagger_client.CorporationApi()
        api = self.setApiDetails(api, user)

        try:
            response = api.get_corporations_corporation_id_structures(573400667)
            print(response)
            print(response.data)
        except Exception as e:
            print("Exception in updateHandler.getStructureDetails: %s\n" % e)
