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

def getSkillTrainingProgress(SkillQueueItem, spPerMinute):
    '''
        Calculates the Skill Progress of the actual Level

    :param SkillQueueItem:
    :return: Percentage as int
    '''
    result = 0
    try:
        # Get the startdate of the skill training and compare it with the actual time
        if SkillQueueItem.start_date is not None:
            now = datetime.datetime.utcnow()
            timePassed = now - SkillQueueItem.start_date
            if timePassed is not None and timePassed > datetime.timedelta(0):
                progress = timePassed.total_seconds() * spPerMinute / 60
                result = int(progress)

    except Exception as e:
        print("Exception in tools.getSkillTrainingProgress: " + str(e))
    return result

def spPerMinute(primary, secondary):
    # Return the skillpoints per second for this attributes

    return primary + secondary/2

def getAttribute(attr_id):
    # returns a string of the character attribute name, for the dogma attribute value of a static skill data
    attr = None
    if attr_id == 164:
        return "Charisma"
    elif attr_id == 165:
        return "Intelligence"
    elif attr_id == 166:
        return "Memory"
    elif attr_id == 167:
        return "Perception"
    elif attr_id == 168:
        return "Willpower"


def getCharPrimaryValue(user_attribute, staticSkill):
    # returns the character attribute value for the skills primary attribute
    if staticSkill.primary_attribute == 164:
        return user_attribute.charisma
    elif staticSkill.primary_attribute == 165:
        return user_attribute.intelligence
    elif staticSkill.primary_attribute == 166:
        return user_attribute.memory
    elif staticSkill.primary_attribute == 167:
        return user_attribute.perception
    elif staticSkill.primary_attribute == 168:
        return user_attribute.willpower


def getCharSecondaryValue(user_attribute, staticSkill):
    # returns the character attribute value for the skills secondary attribute
    if staticSkill.secondary_attribute == 164:
        return user_attribute.charisma
    elif staticSkill.secondary_attribute == 165:
        return user_attribute.intelligence
    elif staticSkill.secondary_attribute == 166:
        return user_attribute.memory
    elif staticSkill.secondary_attribute == 167:
        return user_attribute.perception
    elif staticSkill.secondary_attribute == 168:
        return user_attribute.willpower


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