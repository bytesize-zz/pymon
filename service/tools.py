# Module for little tool Methods

from db.databaseHandler import DatabaseHandler
from db.databaseTables import Character, SkillQueueItem, SkillQueue

import datetime
import config

import builtins

def getSkillRemainingTime(skill):
    # Calculate the timedelta between now and skill end, then return formatted string
    now = datetime.datetime.utcnow()
    then = skill.finish_date
    diff = (then - now)

    return formatTimeDelta(diff)

def getSkillTrainingTime(skill):
    # Calculate the timedelta between start-time and end-time of a skill
    now = datetime.datetime.utcnow()

    if now > skill.start_date:  # Skill is already started
        start = now  # remaining training time is counted from now on
    else:
        start = skill.start_date  # skill start lies in the future
    diff = skill.finish_date - start

    return formatTimeDelta(diff)

def getSkillTrainingProgress(SkillQueueItem):
    '''
        Calculates the Skill Progress of the actual Level

    :param SkillQueueItem:
    :return: Percentage as int
    '''

    all = SkillQueueItem.level_end_sp - SkillQueueItem.level_start_sp  # ToDo: better Name for "all"
    progress = SkillQueueItem.training_start_sp - SkillQueueItem.level_start_sp
    result = int((progress/all) * 100)

    #print(str(all))
    #print(str(progress))
    #print(str(result))

    return result


def offset(x):
    # returns a string wich contains x Spaces
    o = ""
    o += " " * x

    return o

def remapTime(dt):
    now = datetime.datetime.utcnow()
    then = dt
    if then is None:  # Character had never a Remap, so the cooldown is None
        return "Now"
    else:
        diff = (then - now)

    if diff < datetime.timedelta(0):
        return "Now"
    else:
        return formatDateTime(then)

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

def format(data):
    #TODo: switch commata and points
    result = builtins.format(data, ",")

    return result