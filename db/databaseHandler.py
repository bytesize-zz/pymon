from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.data.user import User

import config

class MyDatabese():
    def __init__(self, parent=None):
        super(MyDatabese, self).__init__()


        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()


    def addUser(self, user):

        self.session.add(user)

    def getUser(self, characterID): #TODO: change names characterID CharacterID -> confusing

        # Get User from DB if already excisting
        try:
            user = self.session.query(User).filter(
                User.CharacterID == characterID,
            ).one()
            return user
        # if not retun None
        except NoResultFound:
            user = User()
            user.CharacterID = characterID
            return None





