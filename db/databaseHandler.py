"""
    Database Handler

    The one Module that adresses the Database directly. Every DB request should go threw here

"""
from sqlalchemy import create_engine, desc, asc, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.databaseTables import User, Character, SkillQueue, SkillQueueItem, CharacterPortrait, CompletedSkillItem, \
    CompletedSkillList, StaticSkills, CharacterAttributes, StaticSkillGroups, CharacterNotifications, ServerStatus, \
    SkillPlan

import datetime
import config

class DatabaseHandler():
    def __init__(self, parent=None):
        super(DatabaseHandler, self).__init__()

        # ToDo: is 'check_same_thread':False the right solution ?
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False})
        self.Session = sessionmaker(bind=engine)  # once engine is available
        #session = self.Session()

        # ToDo: Create a Loop that periodicly updates the Database with EvE Informations


    def saveUser(self, newUser):
        session = self.Session()
        user = None
        try:
            dbUser = session.query(User).filter_by(CharacterID=newUser.CharacterID).first()  # ask DB for User with this ID
            if dbUser is None:
                session.add(newUser)
                session.flush()  # We do this, so the DB can give us the autogenerating id to return
                user = newUser
            elif dbUser.CharacterID == newUser.CharacterID:
                dbUser.AccessToken = newUser.AccessToken
                dbUser.RefreshToken = newUser.RefreshToken
                dbUser.AccessTokenExpire = newUser.AccessTokenExpire
                user = dbUser

            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveUser: " + str(e))
            session.rollback()
        #finally:
            #session.close()

        return user

    def getUser(self, cID):
        session = self.Session()
        user = None

        try:  # Get User from DB if already existing
            user = session.query(User).filter_by(CharacterID=cID).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getUser: " + str(e))
        finally:
            session.close()

        return user  # Might be an empty user. user is detached from Session

    def deleteUser(self, user_id):
        session = self.Session()

        try:
            self.deleteSkillQueue(user_id)
            self.deleteKnownSkills(user_id)
            self.deleteCharacterAttributes(user_id)
            self.deleteCharacterNotification(user_id)
            self.deleteCharacterPortrait(user_id)
            self.deleteCharacter(user_id)
            #self.deleteCorporateHistory(user_id)
            #self.deleteWallet(user_id)
            #self.deleteImplanets(user_id)

        except Exception as e:
            print("Exception in DatabaseHandler.deleteUser: " + str(e))
            session.rollback()
        finally:
            session.query(User).filter_by(id=user_id).delete(synchronize_session=False)
            session.commit()
            session.close()

    def getAllUser(self):
        session = self.Session()
        userList = None
        try:
            userList = session.query(User).order_by(User.id).all()
        except Exception as e:
            print("Exception in DatabaseHandler.getAllUser: " + str(e))
        finally:
            session.close()
        return userList

    def deleteCharacter(self, owner_id):
        session = self.Session()

        try:
            session.query(Character).filter_by(owner_id=owner_id).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.deleteCharacter: " + str(e))
        finally:
            session.close()

    def saveCharacter(self, newCharacter):
        session = self.Session()
        try:
            dbCharacter = session.query(Character).filter_by(owner_id=newCharacter.owner_id).first()  # ask DB for User with this ID
            if dbCharacter is None:
                session.add(newCharacter)
            elif dbCharacter.owner_id == newCharacter.owner_id:
                #print("Character already present, lets update him.")
                dbCharacter.setCharacter(newCharacter)
            else:
                print("Something is wrong at databaseHandler.saveCharacter()")
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCharacter: " + str(e))
        finally:
            session.close()


    def getCharacter(self, ownerID):
        session = self.Session()
        # Get Character from DB if already existing
        character = None
        try:
            character = session.query(Character).filter_by(owner_id=ownerID).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getCharacter: " + str(e))
        finally:
            session.close()
        return character  # Might be an empty character

    def saveCharacterAttributes(self, newAttributes):
        session = self.Session()
        #dbAttributes = None
        try:
            dbAttributes = session.query(CharacterAttributes).filter_by(owner_id=newAttributes.owner_id).first()

            if dbAttributes is None:
               session.add(newAttributes)
            elif dbAttributes.owner_id == newAttributes.owner_id:
                #print("Character found, update Skillpoints")
                dbAttributes.update(newAttributes)
            else:
                print("Something is wrong at databaseHandler.saveCharacterSP()")
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCharacterAttributes: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getCharacterAttributes(self, ownerID):
        session = self.Session()
        dbAttributes = None
        try:
            dbAttributes = session.query(CharacterAttributes).filter_by(owner_id=ownerID).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getCharacterAttributes: " + str(e))
        finally:
            session.close()

        return dbAttributes

    def deleteCharacterAttributes(self, ownerID):
        session = self.Session()

        try:  # Deleting old SkillQueueItems
            session.query(CharacterAttributes).filter_by(owner_id=ownerID).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.deleteCharacterAttributes: " + str(e))
            session.rollback()
        finally:
            session.close()

    def saveCharacterSP(self, ownerID, total_sp, unallocated_sp):
        session = self.Session()
        try:
            dbCharacter = session.query(Character).filter_by(owner_id=ownerID).first()  # ask DB for User with this ID
            if dbCharacter is None:
                print("No Character found, do nothing")
            elif dbCharacter.owner_id == ownerID:
                 dbCharacter.setSkillpoints(total_sp, unallocated_sp)

            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCharacterSP: %s\n" % e)
        finally:
            session.close()

    def saveCharacterAlliance(self, name):
        print("x")

    def saveCharacterCorporation(self, name):
        print("x")


    def saveCharacterBalance(self, balance, ownerID):
        session = self.Session()
        try:
            dbCharacter = session.query(Character).filter_by(owner_id=ownerID).first()  # ask DB for User with this ID
            if dbCharacter is None:
                print("No Character found, do nothing")
            elif dbCharacter.owner_id == ownerID:
                dbCharacter.setBalance(balance)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCharacterBalance: " + str(e))
            session.rollback()
        finally:
            session.close()

    def saveSkillQueue(self, newSkillQueue):
        session = self.Session()
        # Add or update the received skillqueue
        try:
            self.deleteSkillQueue(newSkillQueue.owner_id)   # First delete old SkillQueue
            for skill in newSkillQueue.items:               # Then add the new One
                session.add(skill)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveSkillQueue: " + str(e))
        finally:
            session.close()

    def getSkillQueue(self, ownerID):
        session = self.Session()
        # Get SkillQueue for this owner from DB if already existing
        skillQueue = None
        try:
            skillQueue = session.query(SkillQueueItem).filter_by(owner_id=ownerID).all()
        except Exception as e:
            print("Exception in DatabaseHandler.getSkillQueue: " + str(e))
        finally:
            session.close()

        return skillQueue  # Might be an empty skillqueue

    def getSkillQueueItem(self, owner_id, skill_id):
        # We want a specific skill queue item for this user, if it is there
        session = self.Session()
        skillQueueItem = None
        try:
            skillQueueItem = session.query(SkillQueueItem).filter_by(owner_id=owner_id, skill_id=skill_id).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getSkillQueueItem: " + str(e))
        finally:
            session.close()

        return skillQueueItem  # Might be an empty skillqueueitem


    def deleteSkillQueue(self, ownerID):
        session = self.Session()

        try:  # Deleting old SkillQueueItems
            session.query(SkillQueueItem).filter_by(owner_id=ownerID).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.getSkillQueueLast: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getQueueFirst(self, ownerID):
        '''
            Since the Skillqueue will hold already finished Skills, until the Player logs in,
            we need to check for the first skill in queue that is still running

            :param skillQueue:
            :return: first active skill
        '''
        #session = self.Session()
        queue = self.getSkillQueue(ownerID)
        now = datetime.datetime.utcnow()

        for skill in queue:
            then = skill.finish_date
            if then is None or (now < then):  # then is None if SkillQueue is paused
                return skill

    def getSkillQueueLast(self, ownerID):
        session = self.Session()
        # Ask for the Last Item in the SkillQueue
        skill = None
        try:
            skill = session.query(SkillQueueItem).filter_by(owner_id=ownerID).order_by(desc(SkillQueueItem.queue_position)).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getSkillQueueLast: " + str(e))
        finally:
            session.close()

        return skill

    def getSkillsAtV(self, user):
        session = self.Session()
        count = 0
        try:
            count = session.query(CompletedSkillItem).filter_by(owner_id=user.id, trained_skill_level=5).count()
        except Exception as e:
            print("Exception in DatabaseHandler.getSkillsAtV: " + str(e))
        finally:
            session.close()

        return count


    def getKnownSkillsCount(self, user):
        session = self.Session()
        count = 0
        try:
            count = session.query(CompletedSkillItem).filter_by(owner_id=user.id).count()
        except Exception as e:
            print("Exception in DatabaseHandler.getKnownSkills: " + str(e))
        finally:
            session.close()

        return count

    def saveKnownSkills(self, newSkillList):
        session = self.Session()
        # Add or update the received CompletedSkills
        try:
            self.deleteKnownSkills(newSkillList.owner_id)   # First delete old SkillList
            for skill in newSkillList.items:               # Then add the new One
                session.add(skill)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCompletedSkills: " + str(e))
        finally:
            session.close()

    def getKnownSkills(self, ownerID):
        session = self.Session()
        skillList = None
        try:
            skillList = CompletedSkillList().createCSL(session.query(CompletedSkillItem).filter_by(owner_id=ownerID).all(), ownerID)
        except Exception as e:
            print("Exception in DatabaseHandler.getKnownSkills: " + str(e))
        finally:
            session.close()

        return skillList  # Might be an empty skillqueue

    def deleteKnownSkills(self, ownerID):
        session = self.Session()
        #print("Deleting old List of Completed Skills from owner " + str(ownerID))
        try:  # Deleting old CompletedSkillItem's
            session.query(CompletedSkillItem).filter_by(owner_id=ownerID).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.deleteCompletedSkills: " + str(e))
        finally:
            session.close()

    def saveCharacterPortrait(self, newCharPortrait):
        # Add or update the received CharacterPortrait
        session = self.Session()

        try:
            dbCharPortrait = session.query(CharacterPortrait).filter_by(owner_id=newCharPortrait.owner_id).first()
            if dbCharPortrait is None:
                session.add(newCharPortrait)
            elif dbCharPortrait.owner_id == newCharPortrait.owner_id:
                dbCharPortrait.setCharacterPortrait(newCharPortrait, newCharPortrait.owner_id)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveCharacterPortrait: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getCharacterPortrait(self, ownerID):
        session = self.Session()
        # Get CharacterPortrait for this owner from DB if already existing
        characterPortrait = None
        try:
            characterPortrait = session.query(CharacterPortrait).filter_by(owner_id=ownerID).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getCharacterPortrait: " + str(e))
        finally:
            session.close()

        return characterPortrait  # Might be an empty CharacterPortrait

    def deleteCharacterPortrait(self, owner_id):
        session = self.Session()

        try:
            session.query(CharacterPortrait).filter_by(owner_id=owner_id).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in databaseHandler.deleteCharacterPortrait: " + str(e))
            session.rollback()
        finally:
            session.close()

    def saveCharacterNotification(self, newNotification):
        session = self.Session()

        try:
            # First Check if this Notification is already stored
            dbNotification = session.query(CharacterNotifications).filter_by(
                owner_id=newNotification.owner_id, notification_id=newNotification.notification_id).first()
            if dbNotification is None:
                session.add(newNotification)
            else:
                dbNotification.is_read = newNotification.is_read
            session.commit()
        except Exception as e:
            print("Exception in databaseHandler.saveCharacterNotification: " + str(e))
            session.rollback()
        finally:
            session.close()

    def deleteCharacterNotification(self, owner_id):
        session = self.Session()

        try:
            session.query(CharacterNotifications).filter_by(owner_id=owner_id).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in databaseHandler.deleteCharacterNotification: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getStaticSkillData(self, skill_id):
        session = self.Session()
        staticSkill = None
        try:
            staticSkill = session.query(StaticSkills).filter_by(skill_id=skill_id).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getStaticSkillData: " + str(e))
        finally:
            session.close()

        return staticSkill

    def getStaticSkillGroups(self):
        session = self.Session()
        skillGroups = None
        try:
            skillGroups = session.query(StaticSkillGroups).order_by(StaticSkillGroups.name).all()
        except Exception as e:
            print("Exception in DatabaseHandler.getStaticSkillGroups: " + str(e))
        finally:
            session.close()

        return skillGroups

    def getGroupSkills(self, user_id, group_id):
        session = self.Session()
        skills = []
        try:
            for staticSkill in session.query(StaticSkills, StaticSkills.skill_id).filter_by(group_id=group_id).\
                    order_by(StaticSkills.name).all():
                skill = session.query(CompletedSkillItem).filter_by(owner_id=user_id, skill_id=staticSkill.skill_id).first()
                if skill is not None:
                    skills.append(skill)

        except Exception as e:
            print("Exception in DatabaseHandler.getGroupSkills: " + str(e))
        finally:
            session.close()

        return skills

    def getGroupSkillsCount(self, user_id, group_id):
        #ToDo: Make it less ugly
        session = self.Session()
        total = 0
        known = 0
        try:
            for staticSkill in session.query(StaticSkills, StaticSkills.skill_id).filter_by(group_id=group_id).all():
                skill = session.query(CompletedSkillItem).filter_by(owner_id=user_id, skill_id=staticSkill.skill_id).first()
                total = total +1
                if skill is not None:
                    known = known +1

        except Exception as e:
            print("Exception in DatabaseHandler.getGroupSkillsCount: " + str(e))
        finally:
            session.close()

        return total, known

    def staticDumpPresent(self):
        session = self.Session()
        dump = None
        try:
            dump = session.query(StaticSkills).count()
        except Exception as e:
            print("Exception in DatabaseHandler.staticDumpPresent: " + str(e))

        #print(dump)
        if dump is None or dump < 433:
            return False
        elif dump >= 433:  # 433 is the actual count. ToDo: Check for client update and get a new dump
            return True

    def saveServerStatus(self, newStatus):
        session = self.Session()

        try:
            dbStatus = session.query(ServerStatus).first()
            if dbStatus is None:
                session.add(newStatus)
            else:
                dbStatus.setStatus(newStatus)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.saveServerStatus: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getServerStatus(self):
        session = self.Session()
        status = None

        try:
            status = session.query(ServerStatus).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getServerStatus: " + str(e))

        finally:
            session.close()

        return status

    def addPlan(self, newPlan):
        session = self.Session()
        try:
            session.add(newPlan)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.addPlan: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getPlan(self, plan_id):
        session = self.Session()
        plan = None
        try:
            plan = session.query(SkillPlan).filter_by(id=plan_id).first()
        except Exception as e:
            print("Exception in DatabaseHandler.getPlan: " + str(e))
        finally:
            session.close()

        return plan

    def updatePlan(self, newPlan):
        session = self.Session()

        try:
            dbPlan = session.query(SkillPlan).filter_by(id=newPlan.id).first()

            dbPlan.name = newPlan.name
            dbPlan.description = newPlan.description
            dbPlan.skill_list = newPlan.skill_list

            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.updatePlan: " + str(e))
            session.rollback()
        finally:
            session.close()

    def deletePlan(self, plan):
        session = self.Session()

        try:
            session.query(SkillPlan).filter_by(id=plan.id).delete(synchronize_session=False)
            session.commit()
        except Exception as e:
            print("Exception in DatabaseHandler.deletePlan: " + str(e))
            session.rollback()
        finally:
            session.close()

    def getCharacterPlans(self, owner_id):
        session = self.Session()
        plans = None

        try:
            plans = session.query(SkillPlan).filter_by(owner_id=owner_id).all()
        except Exception as e:
            print("Exception in DatabaseHandler.getPlan: " + str(e))
        finally:
            session.close()

        return plans


    def getAllianceData(self, alliID):
        session = self.Session()
        print("x")

        return ""

    def getCorporationData(self, corpID):
        session = self.Session()
        print("x")

        return ""
