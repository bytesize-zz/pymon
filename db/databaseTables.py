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
        return self.id

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security
        """
        return {
            'access_token': self.AccessToken,
            'refresh_token': self.RefreshToken,
            'expires_in': int((
                self.AccessTokenExpire - datetime.utcnow()
            ).total_seconds())
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
    owner_id = Column(Integer, ForeignKey('User.id'))

    def setCharacter(self, request_response, ownerID):
        self.name = request_response.name
        self.description = request_response.description
        self.corporation_id = request_response.corporation_id
        self.alliance_id = request_response.alliance_id
        self.birthday = request_response.birthday
        self.gender = request_response.gender
        self.race_id = request_response.race_id
        self.bloodline_id = request_response.bloodline_id
        self.ancestry_id = request_response.ancestry_id
        self.security_status = request_response.security_status
        self.faction_id = request_response.faction_id
        self.owner_id = ownerID
        return self

    def updateCharacter(self, newCharacter):
        # ToDO: remove unchangeable elements
        self.name = newCharacter.name
        self.description = newCharacter.description
        self.corporation_id = newCharacter.corporation_id
        self.alliance_id = newCharacter.alliance_id
        self.birthday = newCharacter.birthday
        self.gender = newCharacter.gender
        self.race_id = newCharacter.race_id
        self.bloodline_id = newCharacter.bloodline_id
        self.ancestry_id = newCharacter.ancestry_id
        self.security_status = newCharacter.security_status
        self.faction_id = newCharacter.faction_id
        return self

    def __repr__(self):
        return "<Character(name='%s', description='%s', corporation_id='%s', alliance_id='%s', birthday='%s', gender='%s', " \
               "race_id='%s', bloodline_id='%s', ancestry_id='%s', security_status='%s', faction_id'%s', owner_id='%s' )>" % (
            self.name, self.description, self.corporation_id, self.alliance_id, self.birthday, self.gender, self.race_id,
            self.bloodline_id, self.ancestry_id, self.security_status, self.faction_id, self.owner_id)


class CharacterPortrait(Base):
    __tablename__ = 'CharacterPortrait'
    id = Column(Integer, primary_key=True)
    px64x64 = Column(String(100))
    px128x128 = Column(String(100))     # ToDo: Check for necessary String Length
    px256x256 = Column(String(100))
    px512x512 = Column(String(100))
    owner_id = Column(Integer, ForeignKey('User.id'))

    def setCharacterPortrait(self, request_response, ownerID):
        self.px64x64 = request_response.px64x64
        self.px128x128 = request_response.px128x128
        self.px256x256 = request_response.px256x256
        self.px512x512 = request_response.px512x512
        self.owner_id = ownerID
        return self


class Implants(Base):
    __tablename__ = 'Implants'
    id = Column(Integer, primary_key=True)
    # List of Integer (implant_type_id) max. 11      # ToDo: Find Informations for this
    owner_id = Column(Integer, ForeignKey('User.id'))


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
    owner_id = Column(Integer, ForeignKey('User.id'))


class SkillsCompleted(Base):
    __tablename__ = 'SkillCompleted'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer)
    skillpoints_in_skill = Column(Integer)
    trained_skill_level = Column(Integer)
    active_skill_level = Column(Integer)
    total_sp = Column(Integer)
    unallocated_sp = Column(Integer)
    owner_id = Column(Integer, ForeignKey('User.id'))


class CorpHistory(Base):
    __tablename__ = 'CorpHistory'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    corporation_id = Column(Integer)
    is_deleted = Column(String(5))      # True or False
    record_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey('User.id'))

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
