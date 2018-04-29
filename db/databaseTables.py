"""
    Database Tables

    containing the Tables for the Database, with useful functions
    as well as some object classes, to handle the tables, but won't be saved in the DB themselves

"""
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
        return "<User(id='%s', charID='%s', name='%s', hash='%s', access='%s', refresh='%s', expire='%s')>" % (
            self.id, self.CharacterID, self.CharacterName, self.CharacterOwnerHash,
            self.AccessToken, self.RefreshToken, self.AccessTokenExpire)


# Character's public information filled by GET /characters/{character_id}/
class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(37))
    description = Column(String(500))
    corporation_id = Column(Integer)
    corporation_name = Column(String)
    alliance_id = Column(Integer)
    alliance_name = Column(String)
    birthday = Column(DateTime)
    gender = Column(String(6))
    race_id = Column(Integer)
    bloodline_id = Column(Integer)
    ancestry_id = Column(Integer)
    security_status = Column(Float)
    faction_id = Column(Integer)
    total_sp = Column(Integer)
    unallocated_sp = Column(Integer)
    balance = Column(Integer)
    jump_fatigue_expire_date = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('User.id'))

    def setCharacter(self, request_response, ownerID=None):
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
        if ownerID is not None:
            self.owner_id = ownerID
        return self

    def setSkillpoints(self,  total_sp, unallocated_sp):
        self.total_sp = total_sp
        self.unallocated_sp = unallocated_sp

    def setBalance(self, balance):
        self.balance = balance

    def setFatigue(self, fatigue):
        self.jump_fatigue_expire_date = fatigue

    def setAllianceName(self, name):
        self.alliance_name = name

    def setCorporationName(self, name):
        self.corporation_name = name

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

    def __repr__(self):
        return"<Character_Portrait(64='%s', 128='%s', 256='%s', 512='%s')>" % \
              (self.px64x64, self.px128x128, self.px256x256, self.px512x512)


class CharacterAttributes(Base):
    __tablename__ = 'CharacterAttributes'
    id = Column(Integer, primary_key=True)
    charisma = Column(Integer)
    intelligence = Column(Integer)
    memory = Column(Integer)
    perception = Column(Integer)
    willpower = Column(Integer)
    bonus_remaps = Column(Integer)
    last_remap_date = Column(DateTime)  # Datetime of last neural remap, including usage of bonus remaps
    accrued_remap_cooldown_date = Column(DateTime)  # Neural remapping cooldown after a character uses remap accrued over time
    owner_id = Column(Integer, ForeignKey('User.id'))


    def test(self, request_response, ownerID):

        self = request_response     # Might work because of same naming ?
        self.owner_id = ownerID
        return self

    def create(self, request_response, ownerID):
        self.charisma = request_response.charisma
        self.intelligence = request_response.intelligence
        self.memory = request_response.memory
        self.perception = request_response.perception
        self.willpower = request_response.willpower
        self.bonus_remaps = request_response.bonus_remaps
        self.last_remap_date = request_response.last_remap_date
        self.accrued_remap_cooldown_date = request_response.accrued_remap_cooldown_date
        self.owner_id = ownerID

        return self

    def update(self, newAttributes):
        self.charisma = newAttributes.charisma
        self.intelligence = newAttributes.intelligence
        self.memory = newAttributes.memory
        self.perception = newAttributes.perception
        self.willpower = newAttributes.willpower
        self.bonus_remaps = newAttributes.bonus_remaps
        self.last_remap_date = newAttributes.last_remap_date
        self.accrued_remap_cooldown_date = newAttributes.accrued_remap_cooldown_date

        return self


class CharacterNotifications(Base):
    __tablename__ = 'CharacterNotifications'
    id = Column(Integer, primary_key=True)
    notification_id = Column(Integer)
    sender_id = Column(Integer)
    sender_type = Column(String)    # Enum [ character, corporation, alliance, faction, other ]
    timestamp = Column(DateTime)
    is_read = Column(String)    # Boolean
    text = Column(String)
    type = Column(String)
    owner_id = Column(Integer, ForeignKey('User.id'))

    def create(self, response, ownerID):
        self.notification_id = response.notification_id
        self.sender_id = response.sender_id
        self.sender_type = response.sender_type
        self.timestamp = response.timestamp
        self.is_read = response.is_read
        self.text = response.text
        self.type = response.type
        self.owner_id = ownerID

        return self

class Implants(Base):
    __tablename__ = 'Implants'
    id = Column(Integer, primary_key=True)
    # List of Integer (implant_type_id) max. 11      # ToDo: Find Informations for this
    owner_id = Column(Integer, ForeignKey('User.id'))

class SkillPlan(Base):
    __tablename__ = 'SkillPlan'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    skill_list = Column(String)  # String with Skill ID's
    owner_id = Column(Integer, ForeignKey('User.id'))

    def create(self, name, description, ownerID):
        self.name = name
        self.description = description
        self.owner_id = ownerID
        return self

    def saveSkillList(self, skill_list):
        self.skill_list = skill_list


class SkillQueueItem(Base):
    __tablename__ = 'SkillQueueItem'
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

    def setSkillQueueItem(self, newSkill, ownerID):
        self.skill_id = newSkill.skill_id
        self.finish_date = newSkill.finish_date
        self.start_date = newSkill.start_date
        self.finished_level = newSkill.finished_level
        self.queue_position = newSkill.queue_position
        self.training_start_sp = newSkill.training_start_sp
        self.level_end_sp = newSkill.level_end_sp
        self.level_start_sp = newSkill.level_start_sp
        self.owner_id = ownerID

        return self

    def __repr__(self):
        return"<SkillQueueItem(id='%s', skill_id='%s', finish_date='%s', start_date='%s'," \
              "finished_level='%s', queue_position='%s', training_start_sp='%s', level_end_sp='%s'," \
              "level_start_sp='%s', owner_id='%s')>" % \
              (self.id, self.skill_id, self.finish_date, self.start_date, self.finished_level, self.queue_position,
               self.training_start_sp, self.level_end_sp, self.level_start_sp, self.owner_id)


class SkillQueue():
    items = []  # List of SkillQueueItems
    owner_id = None

    def createSkillQueue(self, request_response, ownerID):
        # We use this, to add the ownerID to our List of skills
        self.owner_id = ownerID
        for entry in request_response:
            skill = SkillQueueItem()
            skill.setSkillQueueItem(entry, ownerID)
            self.items.append(skill)
        return self

    def __repr__(self):
        rep = "owner_id" + str(self.owner_id) + "\n"
        for item in self.items:
            rep = rep + item.__repr__() + "\n"
        return rep


class CompletedSkillItem(Base):
    __tablename__ = 'CompletedSkillItem'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer)
    skillpoints_in_skill = Column(Integer)
    trained_skill_level = Column(Integer)
    active_skill_level = Column(Integer)
    #total_sp = Column(Integer)
    #unallocated_sp = Column(Integer)
    owner_id = Column(Integer, ForeignKey('User.id'))

    def setCompletedSkillItem(self, newSkill, ownerID):
        self.skill_id = newSkill.skill_id
        self.skillpoints_in_skill = newSkill.skillpoints_in_skill
        self.trained_skill_level = newSkill.trained_skill_level
        self.active_skill_level = newSkill.active_skill_level
        #self.total_sp = newSkill.total_sp
        #self.unallocated_sp = newSkill.unallocated_sp
        self.owner_id = ownerID

    def __repr__(self):
        return"<CompletedSkillItem(id='%s', skill_id='%s', skillpoints_in_skill='%s', trained_skill_level='%s'," \
              "active_skill_level='%s', owner_id='%s')>" % \
              (self.id, self.skill_id, self.skillpoints_in_skill, self.trained_skill_level, self.active_skill_level, self.owner_id)

class CompletedSkillList():
    items = []  # List of SkillsCompletedItems
    owner_id = None

    def createCSL(self, request_response, ownerID):
        # We use this, to add the ownerID to our List of skills
        self.owner_id = ownerID

        for entry in request_response.skills:
            skill = CompletedSkillItem()
            skill.setCompletedSkillItem(entry, ownerID)
            self.items.append(skill)

        return self

    def __repr__(self):
        rep = "owner_id" + str(self.owner_id) + "\n"
        for item in self.items:
            rep = rep + item.__repr__() + "\n"
        return rep


class CorpHistoryItem(Base):
    __tablename__ = 'CorpHistoryItem'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    corporation_id = Column(Integer)
    is_deleted = Column(String(5))      # True or False
    record_id = Column(Integer)
    list_id = Column(Integer, ForeignKey('CorpHistoryList.id'))


class CorpHistoryList(Base):
    __tablename__ = 'CorpHistoryList'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    corporation_id = Column(Integer)
    is_deleted = Column(String(5))      # True or False
    record_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey('User.id'))

class StaticSkillGroups(Base):
    __tablename__ = 'StaticSkillGroups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    group_id = Column(Integer)

    def setData(self, name, group_id):
        self.name = name
        self.group_id = group_id
        return self

    def __repr__(self):
        return"<Static Skill Group(id='%s', name='%s', group_id='%s')>" % (self.id, self.name, self.group_id)

class StaticSkills(Base):
    __tablename__ = 'StaticSkills'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    skill_id = Column(Integer)
    rank = Column(Integer)
    description = Column(String)
    primary_attribute = Column(Integer)
    secondary_attribute = Column(Integer)
    icon_id = Column(Integer)
    market_group_id = Column(Integer)
    basePrice = Column(Integer)
    group_id = Column(Integer, ForeignKey('StaticSkillGroups.id'))
    requiredSkill1 = Column(Integer)
    requiredSkill2 = Column(Integer)
    requiredSkill3 = Column(Integer)
    requiredSkill4 = Column(Integer)
    requiredSkill5 = Column(Integer)
    requiredSkill6 = Column(Integer)
    requiredSkill1Level = Column(Integer)
    requiredSkill2Level = Column(Integer)
    requiredSkill3Level = Column(Integer)
    requiredSkill4Level = Column(Integer)
    requiredSkill5Level = Column(Integer)
    requiredSkill6Level = Column(Integer)

    def setData(self, data):
        self.name = data['name']
        self.skill_id = data['type_id']
        self.description = data['description']
        self.icon_id = data['icon_id']
        self.market_group_id = data['market_group_id']
        try:
            self.basePrice = Column['base_price']
        except Exception as e:
            print(e)
        self.group_id = data['group_id']

        # The Skillrank hides in data['dogma_attributes'][x]{'attribute_id': 275, 'value': 7.0}
        for attribute in data['dogma_attributes']:
            if attribute['attribute_id'] == 275:
                self.rank = attribute['value']
            elif attribute['attribute_id'] == 180:
                self.primary_attribute = attribute['value']
            elif attribute['attribute_id'] == 181:
                self.secondary_attribute = attribute['value']
            elif attribute['attribute_id'] == 182:
                self.requiredSkill1 = attribute['value']
            elif attribute['attribute_id'] == 183:
                self.requiredSkill2 = attribute['value']
            elif attribute['attribute_id'] == 184:
                self.requiredSkill3 = attribute['value']
            elif attribute['attribute_id'] == 1285:
                self.requiredSkill4 = attribute['value']
            elif attribute['attribute_id'] == 1289:
                self.requiredSkill5 = attribute['value']
            elif attribute['attribute_id'] == 1290:
                self.requiredSkill6 = attribute['value']
            elif attribute['attribute_id'] == 277:
                self.requiredSkill1Level = attribute['value']
            elif attribute['attribute_id'] == 278:
                self.requiredSkill2Level = attribute['value']
            elif attribute['attribute_id'] == 279:
                self.requiredSkill3Level = attribute['value']
            elif attribute['attribute_id'] == 1286:
                self.requiredSkill4Level = attribute['value']
            elif attribute['attribute_id'] == 1287:
                self.requiredSkill5Level = attribute['value']
            elif attribute['attribute_id'] == 1288:
                self.requiredSkill6Level = attribute['value']

        return self

class StaticShipGroups(Base):
    __tablename__ = 'StaticShipGroups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    group_id = Column(Integer)

    def setData(self, name, group_id):
        self.name = name
        self.group_id = group_id
        return self

    def __repr__(self):
        return"<Static Ship Group(id='%s', name='%s', group_id='%s')>" % (self.id, self.name, self.group_id)

class StaticShips(Base):
    __tablename__ = 'StaticShips'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    ship_id = Column(Integer)
    description = Column(String)
    icon_id = Column(Integer)
    market_group_id = Column(Integer)
    basePrice = Column(Integer)
    group_id = Column(Integer, ForeignKey('StaticShipGroups.id'))
    requiredSkill1 = Column(Integer)
    requiredSkill2 = Column(Integer)
    requiredSkill3 = Column(Integer)
    requiredSkill4 = Column(Integer)
    requiredSkill5 = Column(Integer)
    requiredSkill6 = Column(Integer)
    requiredSkill1Level = Column(Integer)
    requiredSkill2Level = Column(Integer)
    requiredSkill3Level = Column(Integer)
    requiredSkill4Level = Column(Integer)
    requiredSkill5Level = Column(Integer)
    requiredSkill6Level = Column(Integer)

    def setData(self, data):
        self.name = data['name']
        self.ship_id = data['type_id']
        self.description = data['description']
        try:
            self.icon_id = data['icon_id']
        except Exception as e:
            print(e)
        try:
            self.market_group_id = data['market_group_id']
        except Exception as e:
            print(e)
        try:
            self.basePrice = Column['base_price']
        except Exception as e:
            print(e)
        self.group_id = data['group_id']

        for attribute in data['dogma_attributes']:
            if attribute['attribute_id'] == 182:
                self.requiredSkill1 = attribute['value']
            elif attribute['attribute_id'] == 183:
                self.requiredSkill2 = attribute['value']
            elif attribute['attribute_id'] == 184:
                self.requiredSkill3 = attribute['value']
            elif attribute['attribute_id'] == 1285:
                self.requiredSkill4 = attribute['value']
            elif attribute['attribute_id'] == 1289:
                self.requiredSkill5 = attribute['value']
            elif attribute['attribute_id'] == 1290:
                self.requiredSkill6 = attribute['value']
            elif attribute['attribute_id'] == 277:
                self.requiredSkill1Level = attribute['value']
            elif attribute['attribute_id'] == 278:
                self.requiredSkill2Level = attribute['value']
            elif attribute['attribute_id'] == 279:
                self.requiredSkill3Level = attribute['value']
            elif attribute['attribute_id'] == 1286:
                self.requiredSkill4Level = attribute['value']
            elif attribute['attribute_id'] == 1287:
                self.requiredSkill5Level = attribute['value']
            elif attribute['attribute_id'] == 1288:
                self.requiredSkill6Level = attribute['value']

        return self

class StaticModuleGroups(Base):
    __tablename__ = 'StaticModuleGroups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    group_id = Column(Integer)

    def setData(self, name, group_id):
        self.name = name
        self.group_id = group_id
        return self

    def __repr__(self):
        return"<Static Module Group(id='%s', name='%s', group_id='%s')>" % (self.id, self.name, self.group_id)

class StaticModules(Base):
    __tablename__ = 'StaticModules'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    module_id = Column(Integer)
    description = Column(String)
    icon_id = Column(Integer)
    market_group_id = Column(Integer)
    basePrice = Column(Integer)
    group_id = Column(Integer, ForeignKey('StaticModuleGroups.id'))
    requiredSkill1 = Column(Integer)
    requiredSkill2 = Column(Integer)
    requiredSkill3 = Column(Integer)
    requiredSkill4 = Column(Integer)
    requiredSkill5 = Column(Integer)
    requiredSkill6 = Column(Integer)
    requiredSkill1Level = Column(Integer)
    requiredSkill2Level = Column(Integer)
    requiredSkill3Level = Column(Integer)
    requiredSkill4Level = Column(Integer)
    requiredSkill5Level = Column(Integer)
    requiredSkill6Level = Column(Integer)

    def setData(self, data):
        self.name = data['name']
        self.ship_id = data['type_id']
        self.description = data['description']
        try:
            self.icon_id = data['icon_id']
        except Exception as e:
            print(e)
        try:
            self.market_group_id = data['market_group_id']
        except Exception as e:
            print(e)
        try:
            self.basePrice = Column['base_price']
        except Exception as e:
            print(e)

        self.group_id = data['group_id']

        for attribute in data['dogma_attributes']:
            if attribute['attribute_id'] == 182:
                self.requiredSkill1 = attribute['value']
            elif attribute['attribute_id'] == 183:
                self.requiredSkill2 = attribute['value']
            elif attribute['attribute_id'] == 184:
                self.requiredSkill3 = attribute['value']
            elif attribute['attribute_id'] == 1285:
                self.requiredSkill4 = attribute['value']
            elif attribute['attribute_id'] == 1289:
                self.requiredSkill5 = attribute['value']
            elif attribute['attribute_id'] == 1290:
                self.requiredSkill6 = attribute['value']
            elif attribute['attribute_id'] == 277:
                self.requiredSkill1Level = attribute['value']
            elif attribute['attribute_id'] == 278:
                self.requiredSkill2Level = attribute['value']
            elif attribute['attribute_id'] == 279:
                self.requiredSkill3Level = attribute['value']
            elif attribute['attribute_id'] == 1286:
                self.requiredSkill4Level = attribute['value']
            elif attribute['attribute_id'] == 1287:
                self.requiredSkill5Level = attribute['value']
            elif attribute['attribute_id'] == 1288:
                self.requiredSkill6Level = attribute['value']

        return self


class ServerStatus(Base):
    __tablename__ = 'ServerStatus'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    players = Column(Integer)
    server_version = Column(String)
    vip = Column(String)
    last_seen = Column(DateTime)

    def setStatus(self, status=None, now=None):
        if status is None:
            self.start_time = None
            self.players = 0
            self.server_version = "unknown"
            self.vip = "unknown"
        else:
            self.start_time = status.start_time
            self.players = status.players
            self.server_version = status.server_version
            self.vip = status.vip

            if now is None:
                self.last_seen = status.last_seen
            else:
                self.last_seen = now

        return self


# Don't delete this!
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
