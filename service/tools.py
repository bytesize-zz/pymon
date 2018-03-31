# Module for little tool Methods

from db.databaseHandler import DatabaseHandler
from db.databaseTables import Character, SkillQueueItem, SkillQueue

import datetime

def getSkillName(skill):
    print("x")
    skillname = "x"

    return skillname
def getSkillRemainingTime(skill):
    print("x")
    now = datetime.datetime.now()
    then = skill.finish_date
    diff = then - now
    print(diff)
    #formatDateTime(diff)
    return "x"

def getQueueRemainingTime(skill):
    print("x")

def getQueueEndDate(skill):
    print("x")

def formatDateTime(x):
    result = x.strftime("%d, %h, %m, %s")

    print(result)
    return "x"