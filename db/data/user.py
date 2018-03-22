from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    OwnerHash = Column(String(100), nullable=False)
    RefreshToken = Column(String(100))
    AccessToken = Column(String(100))
    AccessTokenExpire = Column(String(100))


class SkillQueue(Base):
    __tablename__ = 'SkillQueue'
    id = Column(Integer, primary_key=True)
    skillname = Column(String(100), nullable=False)
    queueposition = Column(Integer)
    UserID = Column(Integer, ForeignKey('User.id'))


class SkillCompleted(Base):
    __tablename__ = 'SkillCompleted'
    id = Column(Integer, primary_key=True)
    skillname = Column(String(100), nullable=False)
    UserID = Column(Integer, ForeignKey('User.id'))


class CorpHistory(Base):
    __tablename__ = 'CorpHistory'
    id = Column(Integer, primary_key=True)
    CorpName = Column(String(100), nullable=False)
    EntryDate = Column(DateTime)


engine = create_engine('sqlite:///pymon.db')
Base.metadata.create_all(engine)
