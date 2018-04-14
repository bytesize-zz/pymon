# Module for little tool Methods

from db.databaseHandler import DatabaseHandler
from db.databaseTables import Character, SkillQueueItem, SkillQueue

import datetime
import config


def getSkillRemainingTime(skill):
    # Calculate the timedelta between now and skill end, then return formatted string
    now = datetime.datetime.utcnow()
    then = skill.finish_date
    diff = (then - now)

    return formatTimeDelta(diff)


def offset(x):
    # returns a string wich contains x Spaces
    o = ""
    o += " " * x

    return o


def getQueueEndDate(skill):
    print("x")

def formatDateTime(dt):
    result = dt.strftime("%A %d.%m.%y %H:%M")
    return result

def formatTimeDelta(td):
    # Convert a datetime Timedelta into a formatted string
    days = td.days
    s = td.seconds
    hours = s // 3600
    s = s - (hours * 3600)
    minutes = s // 60
    seconds = s - (minutes * 60)

    return "%sd %sh %sm %ss" % (days, hours, minutes, seconds)
