from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

from datetime import datetime
import config
import time


# User is mainly for Authorisation purposes and root for all Character Informations
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    CharacterID = Column(Integer, nullable=False)
    CharacterName = Column(String(37), nullable=False)
    CharacterOwnerHash = Column(String(40), nullable=False)  # Maybe Length of 28 is enough
    RefreshToken = Column(String(75))                       # Maybe Length of 65 is enough
    AccessToken = Column(String(100))                       # Maybe Length of 87 is enough
    AccessTokenExpire = Column(DateTime)

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
            self.CharacterID, self.CharacterName, self.CharacterOwnerHash, self.AccessToken,
            self.RefreshToken, self.AccessTokenExpire)


# Character's public information filled by GET /characters/{character_id}/
class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(37))
    description = Column(String(500))
    corporation_id = Column(Integer)
    alliance_id = Column(Integer)
    birthday = Column(DateTime)
    gender = Column(String(6))
    race_id = Column(Integer)
    bloodline_id = Column(Integer)
    ancestry_id = Column(Integer)
    security_status = Column(Float)
    faction_id = Column(Integer)
    UserID = Column(Integer, ForeignKey('User.id'))


class CharacterPortrait(Base):
    __tablename__ = 'Portrait'
    id = Column(Integer, primary_key=True)
    px64x64 = Column(String(100))
    px128x128 = Column(String(100))     # ToDo: Check for necessary String Length
    px256x256 = Column(String(100))
    px512x512 = Column(String(100))
    UserID = Column(Integer, ForeignKey('User.id'))


class Implants(Base):
    __tablename__ = 'Implants'
    id = Column(Integer, primary_key=True)
    # List of Integer (implant_type_id) max. 11      # ToDo: Find Informations for this
    UserID = Column(Integer, ForeignKey('User.id'))


class SkillQueue(Base):
    __tablename__ = 'SkillQueue'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer)
    finish_date = Column(DateTime)
    start_date = Column(DateTime)
    finished_level = Column(Integer)
    queue_position = Column(Integer)
    training_start_sp = Column(Integer)
    level_end_sp = Column(Integer)
    level_start_sp = Column(Integer)
    UserID = Column(Integer, ForeignKey('User.id'))


class SkillsCompleted(Base):
    __tablename__ = 'SkillCompleted'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer)
    skillpoints_in_skill = Column(Integer)
    trained_skill_level = Column(Integer)
    active_skill_level = Column(Integer)
    total_sp = Column(Integer)
    unallocated_sp = Column(Integer)
    UserID = Column(Integer, ForeignKey('User.id'))


class CorpHistory(Base):
    __tablename__ = 'CorpHistory'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    corporation_id = Column(Integer)
    is_deleted = Column(String(5))      # True or False
    record_id = Column(Integer)


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
