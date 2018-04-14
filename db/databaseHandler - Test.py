"""
    Database Handler

    The one Module that adresses the Database directly. Every DB request should go threw here

"""
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db.databaseTables import User, Character, SkillQueue, SkillQueueItem, CharacterPortrait, CompletedSkillItem, \
    CompletedSkillList, StaticSkills, StaticSkillGroups, CharacterAttributes

import datetime
import config

class DatabaseHandler():
    def __init__(self, parent=None):
        super(DatabaseHandler, self).__init__()


        # ToDo: Create a Loop that periodicly updates the Database with EvE Informations
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False})
        self.Session = sessionmaker(bind=engine)  # once engine is available


    def saveUser(self, newUser):
        session = self.Session()
        id = None
        try:
            dbUser = self.getUser(newUser.CharacterID)  # ask DB for User with this ID

            if dbUser is None:
                session.add(newUser)
                session.flush()        # We do this, so the DB can give us the autogenerating id to return
                id = newUser.id
            elif dbUser.CharacterID == newUser.CharacterID:
                dbUser.AccessToken = newUser.AccessToken
                dbUser.RefreshToken = newUser.RefreshToken
                dbUser.AccessTokenExpire = newUser.AccessTokenExpire
                id = dbUser.id
            else:
                print("Something is wrong at databaseHandler.saveUser()")
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()
        return id

    def getUser(self, cID):
        # Get User from DB if already existing
        session = self.Session()
        try:
            user = session.query(User).filter_by(CharacterID=cID).first()
            session.expunge(user)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            user = User()
            user.CharacterID = cID
        finally:
            session.close()
        return user  # Might be an empty user

    def getAllUser(self):
        session = self.Session()
        userList = None
        try:
            userList = session.query(User).order_by(User.CharacterName)
            session.expunge(userList)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return userList

    def getCharacter(self, ownerID):
        # Get Character from DB if already existing
        session = self.Session()
        try:
            character = session.query(Character).filter_by(owner_id=ownerID).first()
            session.expunge(character)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print("NoResultFound")
            character = Character()
            character.owner_id = ownerID
        finally:
            session.close()

        return character  # Might be an empty character

    def saveCharacter(self, newCharacter):
        session = self.Session()

        try:
            dbCharacter = self.getCharacter(newCharacter.owner_id)  # ask DB for User with this ID

            if dbCharacter is None:
                session.add(newCharacter)
            elif dbCharacter.owner_id == newCharacter.owner_id:
                dbCharacter.updateCharacter(newCharacter)
            else:
                print("Something is wrong at databaseHandler.saveCharacter()")
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def saveCharacterSP(self, ownerID, total_sp, unallocated_sp):
        session = self.Session()
        try:
            dbCharacter = self.getCharacter(ownerID)  # ask DB for User with this ID
            if dbCharacter is None:
                print("No Character found, do nothing")
            elif dbCharacter.owner_id == ownerID:
                #print("Character found, update Skillpoints")
                dbCharacter.setSkillpoints(total_sp, unallocated_sp)
            else:
                print("Something is wrong at databaseHandler.saveCharacterSP()")

            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def saveCharacterAttributes(self, newAttributes):
        session = self.Session()
        dbAttributes = None
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
            print(e)
            session.rollback()
        finally:
            session.close()


    def saveCharacterBalance(self, balance, ownerID):
        session = self.Session()
        try:
            dbCharacter = self.getCharacter(ownerID)  # ask DB for User with this ID
            if dbCharacter is None:
                print("No Character found, do nothing")
            elif dbCharacter.owner_id == ownerID:
                #print("Character found, update Balance")
                dbCharacter.setBalance(balance)
            else:
                print("Something is wrong at databaseHandler.saveCharacterBalance()")
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()


    def saveSkillQueue(self, newSkillQueue):
        session = self.Session()
        # Add or update the received skillqueue
        try:
            #print("Updating Skillqueue...")
            self.deleteSkillQueue(newSkillQueue.owner_id)   # First delete old SkillQueue
            for skill in newSkillQueue.items:               # Then add the new One
                session.add(skill)

            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def deleteSkillQueue(self, ownerID):
        session = self.Session()
        #print("Deleting old Skill Queue from owner " + str(ownerID))
        try:  # Deleting old SkillQueueItems
            oldQueue = session.query(SkillQueueItem).filter_by(owner_id=ownerID).all()
            for skill in oldQueue:
                session.delete(skill)
                session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()


    def getSkillQueue(self, ownerID):
        session = self.Session()
        # Get SkillQueue for this owner from DB if already existing
        skillQueue2 = None
        try:
            skillQueue = SkillQueue().createSkillQueue(session.query(SkillQueueItem).filter_by(owner_id=ownerID).all(), ownerID)
            skillQueue2 = session.query(SkillQueueItem).filter_by(owner_id=ownerID).all()
            session.expunge(skillQueue2)
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

        return skillQueue2

    def getSkillQueueFirst(self, ownerID):
        session = self.Session()
        # Ask for the First Item in the SkillQueue
        skill = None
        try:
            skill =session.query(SkillQueueItem).filter_by(owner_id=ownerID).order_by(SkillQueueItem.queue_position).first()
            session.expunge(skill)
        except Exception as e:
            print(e)
        finally:
            session.close()
        #print(ownerID), print(skill)
        return skill

    def getQueueFirst(self, ownerID):
        '''
            Since the Skillqueue will hold already finished Skills, until the Player logs in,
            we need to check for the first skill in queue that is still running

        :param skillQueue:
        :return: first active skill
        '''
        queue = self.getSkillQueue(ownerID)
        now = datetime.datetime.utcnow()

        for skill in queue:
            then = skill.finish_date
            if now < then:
                return skill

    def getSkillQueueLast(self, ownerID):
        session = self.Session()
        # Ask for the Last Item in the SkillQueue
        #print(" Getting SkillQueueLast with ownerID: " + str(ownerID))
        skill = None
        try:
            skill = session.query(SkillQueueItem).filter_by(owner_id=ownerID).order_by(desc(SkillQueueItem.queue_position)).first()
            session.expunge(skill)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return skill

    def saveCompletedSkills(self, newSkillList):
        session = self.Session()
        # Add or update the received CompletedSkills
        try:
            #print("Updating completed Skills...")
            self.deleteCompletedSkills(newSkillList.owner_id)   # First delete old SkillList
            for skill in newSkillList.items:               # Then add the new One
                session.add(skill)

            print("Update complete.")
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def getCompletedSkills(self, ownerID):
        session = self.Session()
        # Get CompletedSkillList for this owner from DB if already existing
        skillList = None
        try:
            skillList = CompletedSkillList().createCSL(session.query(CompletedSkillItem).filter_by(owner_id=ownerID).all(), ownerID)
            session.expunge(skillList)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return skillList

    def deleteCompletedSkills(self, ownerID):
        session = self.Session()
        try:  # Deleting old CompletedSkillItem's
            session.query(CompletedSkillItem).filter_by(owner_id=ownerID).delete(synchronize_session=False)

            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def saveCharacterPortrait(self, newCharacterPortrait):
        session = self.Session()
        # Add or update the received CharacterPortrait
        try:
            dbCharacterPortrait = self.getCharacterPortrait(newCharacterPortrait.owner_id)  # ask DB for User with this ID

            if dbCharacterPortrait is None:
                session.add(newCharacterPortrait)
            elif dbCharacterPortrait.owner_id == newCharacterPortrait.owner_id:
                dbCharacterPortrait.setCharacterPortrait(newCharacterPortrait, newCharacterPortrait.owner_id)
            else:
                print("Something is wrong at databaseHandler.saveCharacterPortrait()")
            session.commit()
        except Exception as e:
            print(e)
        finally:
            session.close()


    def getStaticSkillData(self, skill_id):
        session = self.Session()
        staticSkill = None
        try:
            staticSkill = session.query(StaticSkills).filter_by(skill_id=skill_id).first()
            session.expunge(staticSkill)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return staticSkill

    def getStaticSkillGroups(self):
        session = self.Session()
        skillGroups = None
        try:
            skillGroups = session.query(StaticSkillGroups).order_by(StaticSkillGroups.name).all()
            session.expunge(skillGroups)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return skillGroups

    def getSkillsFromGroup(self, group):
        session = self.Session()
        skills = None
        try:
            skills = session.query(CompletedSkillItem).order_by(StaticSkillGroups.name).all()
            session.expunge(skills)
        except Exception as e:
            print(e)
        finally:
            session.close()

        return skills


    def staticDumpPresent(self):
        session = self.Session()
        dump = None
        try:
            dump =session.query(StaticSkills).first()
            session.expunge(dump)
        except Exception as e:
            print(e)
        finally:
            session.close()

        if dump is None:
            return False
        else:
            return True

    def getCharacterPortrait(self, ownerID):
        session = self.Session()
        # Get CharacterPortrait for this owner from DB if already existing
        try:
            characterPortrait = session.query(CharacterPortrait).filter_by(owner_id=ownerID).first()
            session.expunge(characterPortrait)
        except NoResultFound:      # ToDo: Find out, why this exception isn't triggering
            print(NoResultFound)
            characterPortrait = CharacterPortrait()
            characterPortrait.owner_id = ownerID
        #finally:
           # session.close()

        return characterPortrait  # Might be an empty CharacterPortrait

