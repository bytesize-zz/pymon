from sqlalchemy import create_engine
import sqlite3

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.databaseTables import User, Character, SkillQueue, SkillQueueItem, CharacterPortrait, CompletedSkillItem, CompletedSkillList


import config

class DatabaseHandler():
    def __init__(self, parent=None):
        super(DatabaseHandler, self).__init__()

        # ToDo: is 'check_same_thread':False the right solution ?
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False})
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()

        # ToDo: Create a Loop that periodicly updates the Database with EvE Informations


    def saveUser(self, newUser):
        self.dbUser = self.getUser(newUser.CharacterID)  # ask DB for User with this ID
        id = None
        print("Saving User: "), print(newUser)
        # ToDo: Exception Handling
        if self.dbUser is None:
            print("New User found, lets add him do the Database")
            self.session.add(newUser)
            self.session.flush()        # We do this, so the DB can give us the autogenerating id to return
            id = newUser.id
        elif self.dbUser.CharacterID == newUser.CharacterID:
            print("User already present, lets update him.")
            self.dbUser.AccessToken = newUser.AccessToken
            self.dbUser.RefreshToken = newUser.RefreshToken
            self.dbUser.AccessTokenExpire = newUser.AccessTokenExpire
            id = self.dbUser.id
        else:
            print("Something is wrong at databaseHandler.saveUser()")

        self.session.commit()
        return id

    def getUser(self, cID):
        # Get User from DB if already existing
        print("Getting User with characterID:" + str(cID))
        try:
            user = self.session.query(User).filter_by(CharacterID=cID).first()
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            user = User()
            user.CharacterID = cID

        return user  # Might be an empty user

    def getAllUser(self):
        try:
            userList = self.session.query(User).order_by(User.CharacterName)
            return userList

        except NoResultFound:
            return None

    def saveCharacter(self, newCharacter):
        self.dbCharacter = self.getCharacter(newCharacter.owner_id)  # ask DB for User with this ID

        # ToDo: Exception Handling
        if self.dbCharacter is None:
            print("New Character found, lets add him do the Database")
            #print(newCharacter)
            self.session.add(newCharacter)
        elif self.dbCharacter.owner_id == newCharacter.owner_id:
            print("Character already present, lets update him.")
            self.dbCharacter.updateCharacter(newCharacter)
        else:
            print("Something is wrong at databaseHandler.saveCharacter()")

        self.session.commit()

    def saveCharacterSP(self, ownerID, total_sp, unallocated_sp):
        print(str(ownerID))
        self.dbCharacter = self.getCharacter(ownerID)  # ask DB for User with this ID
        if self.dbCharacter is None:
            print("No Character found, do nothing")
        elif self.dbCharacter.owner_id == ownerID:
            print("Character found, update Skillpoints")
            self.dbCharacter.setSkillpoints(total_sp, unallocated_sp)
        else:
            print("Something is wrong at databaseHandler.saveCharacterSP()")

        self.session.commit()

    def getCharacter(self, ownerID):
        # Get Character from DB if already existing
        print("Getting Character with ownerID: " + str(ownerID))
        try:
            character = self.session.query(Character).filter_by(owner_id=ownerID).first()
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print("NoResultFound")
            character = Character()
            character.owner_id = ownerID
        return character  # Might be an empty character


    def saveSkillQueue(self, newSkillQueue):
        # Add or update the received skillqueue
        try:
            print("Updating Skillqueue...")
            self.deleteSkillQueue(newSkillQueue.owner_id)   # First delete old SkillQueue
            for skill in newSkillQueue.items:               # Then add the new One
                self.session.add(skill)
        except Exception as e:
            print(e)

        self.session.commit()


    def getSkillQueue(self, ownerID):
        # Get SkillQueue for this owner from DB if already existing
        #print(ownerID)
        try:
            skillQueue = SkillQueue().createSkillQueue(self.session.query(SkillQueueItem).filter_by(owner_id=ownerID).all(), ownerID)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print("NoResultFound")

        if skillQueue is None or len(skillQueue.items) == 0:
            return None
        else:
            return skillQueue  # Might be an empty skillqueue

    def deleteSkillQueue(self, ownerID):
        print("Deleting old Skill Queue from owner " + str(ownerID))
        try:  # Deleting old SkillQueueItems
            self.session.query(SkillQueueItem).filter_by(owner_id=ownerID).delete(synchronize_session=False)
        except Exception as e:
            print(e)

        self.session.commit()

    def saveCompletedSkills(self, newSkillList):
        # Add or update the received CompletedSkills
        try:
            print("Updating completed Skills...")
            self.deleteCompletedSkills(newSkillList.owner_id)   # First delete old SkillList
            for skill in newSkillList.items:               # Then add the new One
                self.session.add(skill)
        except Exception as e:
            print(e)
        print("Update complete.")
        self.session.commit()

    def getCompletedSkills(self, ownerID):
        # Get CompletedSkillList for this owner from DB if already existing
        #print(ownerID)
        try:
            skillList = CompletedSkillList().createCSL(self.session.query(CompletedSkillItem).filter_by(owner_id=ownerID).all(), ownerID)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print("NoResultFound")

        if skillList is None or len(skillList.items) == 0:
            return None
        else:
            return skillList  # Might be an empty skillqueue

    def deleteCompletedSkills(self, ownerID):
        print("Deleting old List of Completed Skills from owner " + str(ownerID))
        try:  # Deleting old CompletedSkillItem's
            self.session.query(CompletedSkillItem).filter_by(owner_id=ownerID).delete(synchronize_session=False)
        except Exception as e:
            print(e)

        self.session.commit()

    def saveCharacterPortrait(self, newCharacterPortrait):
        # Add or update the received CharacterPortrait
        self.dbCharacterPortrait = self.getCharacterPortrait(newCharacterPortrait.owner_id)  # ask DB for User with this ID

        # ToDo: Exception Handling
        try:
            if self.dbCharacterPortrait is None:
                print("New Portrait found, lets add it do the Database")
                self.session.add(newCharacterPortrait)
            elif self.dbCharacterPortrait.owner_id == newCharacterPortrait.owner_id:
                print("Portrait already present, lets update it.")
                self.dbCharacterPortrait.setCharacterPortrait(newCharacterPortrait, newCharacterPortrait.owner_id)
            else:
                print("Something is wrong at databaseHandler.saveCharacterPortrait()")
        except Exception as e:
            print(e)
        print("Character Portrait saved")
        self.session.commit()

    def getCharacterPortrait(self, ownerID):
        # Get CharacterPortrait for this owner from DB if already existing
        print("Gettin characterPortrait with ownerID: " + str(ownerID))
        try:
            characterPortrait = self.session.query(CharacterPortrait).filter_by(owner_id=ownerID).first()
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print(NoResultFound)
            characterPortrait = CharacterPortrait()
            characterPortrait.owner_id = ownerID

        print(characterPortrait)
        return characterPortrait  # Might be an empty CharacterPortrait

    def close(self):
        self.session.close()

    def __del__(self):
        self.session.close()
