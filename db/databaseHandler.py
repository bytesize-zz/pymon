from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.databaseTables import User, Character, SkillQueue, CharacterPortrait


import config

class DatabaseHandler():
    def __init__(self, parent=None):
        super(DatabaseHandler, self).__init__()


        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()


    def saveUser(self, newUser):
        self.dbUser = self.getUser(newUser.CharacterID)  # ask DB for User with this ID

        #print("newUser: "), print(newUser)
        #print("dbUser: "), print(self.dbUser)

        # ToDo: Exception Handling
        if self.dbUser is None:
            print("New User found, lets add him do the Database")
            self.session.add(newUser)
        elif self.dbUser.CharacterID == newUser.CharacterID:
            print("User already present, lets update him.")
            self.dbUser.AccessToken = newUser.AccessToken
            self.dbUser.RefreshToken = newUser.RefreshToken
            self.dbUser.AccessTokenExpire = newUser.AccessTokenExpire
        else:
            print("Something is wrong at databaseHandler.saveUser()")

        #print("Updated Line: "), print(self.session.dirty)
        #print("New Line: "), print(self.session.new)

        self.session.commit()

    def getUser(self, cID):

        # Get User from DB if already existing
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
        print(newCharacter.owner_id)
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


    def getCharacter(self, ownerID):
        # Get Character from DB if already existing
        #print(ownerID)
        try:
            character = self.session.query(Character).filter_by(owner_id=ownerID).first()
            print(character)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print(NoResultFound)
            character = Character()
            character.owner_id = ownerID
        return character  # Might be an empty character

    def saveSkillQueue(self, newSkillQueue):
        # Add or update the received skillqueue
        print(newSkillQueue.owner_id)
        self.dbSkillQueue = self.getCharacter(newSkillQueue.owner_id)  # ask DB for User with this ID

        # ToDo: Exception Handling
        if self.dbSkillQueue is None:
            print("New Character found, lets add him do the Database")
            print(newSkillQueue)
            self.session.add(newSkillQueue)
        elif self.dbSkillQueue.owner_id == newSkillQueue.owner_id:
            print("Character already present, lets update him.")
            self.dbSkillQueue.updatekillQueue(newSkillQueue)
        else:
            print("Something is wrong at databaseHandler.saveCharacter()")

        self.session.commit()

    def getSkillQueue(self, ownerID):
        # Get SkillQueue for this owner from DB if already existing
        #print(ownerID)
        try:
            skillQueue = self.session.query(SkillQueue).filter_by(owner_id=ownerID).first()
            print(skillQueue)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print(NoResultFound)
            skillQueue = SkillQueue()
            skillQueue.owner_id = ownerID
        return skillQueue  # Might be an empty skillqueue

    def saveCharacterPortrait(self, newCharacterPortrait):
        # Add or update the received CharacterPortrait
        #print(newCharacterPortrait.owner_id)
        self.dbCharacterPortrait = self.getCharacterPortrait(newCharacterPortrait.owner_id)  # ask DB for User with this ID

        # ToDo: Exception Handling
        try:
            if self.dbCharacterPortrait is None:
                print("New Portrait found, lets add him do the Database")
                #print(newCharacterPortrait)
                self.session.add(newCharacterPortrait)
            elif self.dbCharacterPortrait.owner_id == newCharacterPortrait.owner_id:
                print("Portrait already present, lets update him.")
                self.dbCharacterPortrait.setCharacterPortrait(newCharacterPortrait, newCharacterPortrait.owner_id)
            else:
                print("Something is wrong at databaseHandler.saveCharacterPortrait()")
        except Exception as e:
            print(e)

        self.session.commit()

    def getCharacterPortrait(self, ownerID):
        # Get CharacterPortrait for this owner from DB if already existing
        #print(ownerID)
        try:
            print("Ask Database CharacterPortrait entry for owner", + ownerID)
            characterPortrait = self.session.query(CharacterPortrait).filter_by(owner_id=ownerID).first()
            #print(CharacterPortrait)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print(NoResultFound)
            characterPortrait = CharacterPortrait()
            characterPortrait.owner_id = ownerID
        return characterPortrait  # Might be an empty CharacterPortrait