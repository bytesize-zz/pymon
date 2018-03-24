from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

from datetime import datetime
import config
import time

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    CharacterID = Column(Integer, nullable=False)
    CharacterName = Column(String(100), nullable=False)
    CharacterOwnerHash = Column(String(100), nullable=False)
    RefreshToken = Column(String(100))
    AccessToken = Column(String(100))
    AccessTokenExpire = Column(String(100))
    def get_id(self):
        return self.CharacterID

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security
        """
        return {
            'access_token': self.AccessToken,
            'refresh_token': self.RefreshToken,
            'expires_in': (
                self.AccessTokenExpire - datetime.utcnow()
            ).total_seconds()
        }

    def update_token(self, token_response):
        """ helper function to update token data from SSO response """
        self.AccessToken = token_response['access_token']
        self.AccessTokenExpire = datetime.fromtimestamp(
            time.time() + token_response['expires_in'],
        )
        if 'refresh_token' in token_response:
            self.RefreshToken = token_response['refresh_token']

    def __repr__(self):
        return "<User(ID='%s', name='%s', hash='%s', access='%s', refresh='%s', expire='%s')>" % (
            self.CharacterID, self.CharacterName, self.CharacterOwnerHash, self.AccessToken, self.RefreshToken, self.AccessTokenExpire)

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.id'))

class SkillQueue(Base):
    __tablename__ = 'SkillQueue'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer)
    finish_date = Column(String(100))
    start_date = Column(String(100))
    finished_level = Column(Integer)
    UserID = Column(Integer, ForeignKey('User.id'))


class SkillsCompleted(Base):
    __tablename__ = 'SkillCompleted'
    id = Column(Integer, primary_key=True)
    skillname = Column(String(100), nullable=False)
    UserID = Column(Integer, ForeignKey('User.id'))


class CorpHistory(Base):
    __tablename__ = 'CorpHistory'
    id = Column(Integer, primary_key=True)
    CorpName = Column(String(100), nullable=False)
    EntryDate = Column(DateTime)


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
