from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.data.user import User

import config

class DatabaseHandler():
    def __init__(self, parent=None):
        super(DatabaseHandler, self).__init__()


        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()


    def addUser(self, newUser):
        self.dbUser = self.getUser(newUser.CharacterID)  # ask DB for User with this ID

        #print("newUser: "), print(newUser)
        #print("dbUser: "), print(self.dbUser)

        # ToDo: Exception Handling
        if self.dbUser is None:
            print("New Character found, lets add him do the Database")
            self.session.add(newUser)
        elif self.dbUser.CharacterID == newUser.CharacterID:
            print("Character already present, lets update him.")
            self.dbUser.AccessToken = newUser.AccessToken
            self.dbUser.RefreshToken = newUser.RefreshToken
            self.dbUser.AccessTokenExpire = newUser.AccessTokenExpire
        else:
            print("Something is wrong at databaseHandler.addUser()")

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




