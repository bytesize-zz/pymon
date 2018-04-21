# -*- encoding: utf-8 -*-
import datetime

# -----------------------------------------------------
# Application configurations
# ------------------------------------------------------
DEBUG = True
SECRET_KEY = 'YouNeedToChangeThisToBeSecure!'
PORT = 5015
HOST = 'localhost'
APP_NAME = "PyMon"
APP_ICON = "icon5.png"



TIME_DIFFERENCE = 0  # Time difference between user timezone and eve time

# -----------------------------------------------------
# SQL Alchemy configs
# -----------------------------------------------------
SQLALCHEMY_DATABASE_URI = 'sqlite:///pymon.db'  # /// relative path, //// absolute path

# -----------------------------------------------------
# ESI Configs
# -----------------------------------------------------
ESI_DATASOURCE = 'tranquility'  # Change it to 'singularity' to use the test server
ESI_ESI_URL = 'https://esi.tech.ccp.is'     # Alternative: esi.evetech.net ?
ESI_SSO_URL = 'https://login.eveonline.com'
ESI_SWAGGER_JSON = 'https://esi.tech.ccp.is/latest/swagger.json?datasource=%s' % ESI_DATASOURCE
ESI_SECRET_KEY = 'gmv5MxaFvyqrbHiiXV5T3FxCuJ5wOH7YLChwrqD8'  # app secret key
ESI_CLIENT_ID = '53ae85c260ea4f77a3394edfbb9f4121'  # app client ID
ESI_CALLBACK = 'http://%s:%d/sso/callback' % (HOST, PORT)  # the callback URI you gave CCP
ESI_USER_AGENT = 'pymon'
ESI_AGENT_DESCRIPTION = 'https://github.com/bytesize-zz/pymon'
ESI_SCOPES = ['esi-skills.read_skills.v1',
              'esi-skills.read_skillqueue.v1',
              'esi-wallet.read_character_wallet.v1',
              'esi-characters.read_fatigue.v1',
              'esi-corporations.read_structures.v1',  # ToDO: remove in release version
              'esi-characters.read_notifications.v1']

# ------------------------------------------------------
# Session settings for flask login
# ------------------------------------------------------
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)

# ------------------------------------------------------
# DO NOT EDIT
# Fix warnings from flask-sqlalchemy / others
# ------------------------------------------------------
SQLALCHEMY_TRACK_MODIFICATIONS = True

# ------------------------------------------------------
# GUI Settings
# ------------------------------------------------------
