# -*- encoding: utf-8 -*-
import datetime

# -----------------------------------------------------
# Application configurations
# ------------------------------------------------------
DEBUG = True
SECRET_KEY = 'YouNeedToChangeThisToBeSecure!'
PORT = 5015
HOST = 'localhost'

# -----------------------------------------------------
# SQL Alchemy configs
# -----------------------------------------------------
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

# -----------------------------------------------------
# ESI Configs
# -----------------------------------------------------
ESI_DATASOURCE = 'tranquility'  # Change it to 'singularity' to use the test server
ESI_SWAGGER_JSON = 'https://esi.tech.ccp.is/latest/swagger.json?datasource=%s' % ESI_DATASOURCE
ESI_SECRET_KEY = "f7xMYMqSSvO9EpmS2FZtW9ZPKnQHvRhUQVkGfsBS"  # your secret key  ToDo: mask key per base64.b64encode
ESI_CLIENT_ID = '2e3ccffa023e4c9685ab8d549ffab9c8'  # your client ID
ESI_CALLBACK = 'http://%s:%d/sso/callback' % (HOST, PORT)  # the callback URI you gave CCP
ESI_USER_AGENT = 'pymon'
ESI_SCOPES = ['esi-characters.read_standings.v1',   # List of all needed Scopes
              'esi-wallet.read_character_wallet.v1']

# ------------------------------------------------------
# Session settings for flask login
# ------------------------------------------------------
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)

# ------------------------------------------------------
# DO NOT EDIT
# Fix warnings from flask-sqlalchemy / others
# ------------------------------------------------------
SQLALCHEMY_TRACK_MODIFICATIONS = True
