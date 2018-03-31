# https://github.com/Kyria/flask-esipy-example/blob/master/app.py
from service.callback_server import StoppableHTTPServer, AuthHandler

from service.esipy.app import App
from service.esipy.client import EsiClient
from service.esipy.security import EsiSecurity
from service.esipy.exceptions import APIException

from db.databaseTables import User
from db.databaseHandler import DatabaseHandler
from service.updateHandler import UpdateHandler

import webbrowser
import config
import hashlib
import hmac
import logging
import random
import time
import threading

# logger stuff
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logger.addHandler(console)

# -----------------------------------------------------------------------
# Database models
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# ESIPY Init
# -----------------------------------------------------------------------
# create the app
esiapp = App.create(config.ESI_SWAGGER_JSON)

#securityKey = EsiSecurity.getSecurityKey(config.ESI_SECRET_KEY)

# init the security object
esisecurity = EsiSecurity(
    app=esiapp,
    redirect_uri=config.ESI_CALLBACK,
    client_id=config.ESI_CLIENT_ID,
    secret_key=config.ESI_SECRET_KEY,
)

# init the client   ToDo: is this used ?
esiclient = EsiClient(
    security=esisecurity,
    cache=None,
    headers={'User-Agent': config.ESI_USER_AGENT}
)


# -----------------------------------------------------------------------
# Login / Logout Routes
# -----------------------------------------------------------------------
def generate_token():
    """Generates a non-guessable OAuth token"""
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    rand = random.SystemRandom()
    random_string = ''.join(rand.choice(chars) for _ in range(40))
    return hmac.new(
        config.SECRET_KEY.encode(),
        random_string,
        hashlib.sha256
    ).hexdigest()

class Esi():

    def __init__(self, callback=None):
        """
        A note on login/logout events: the character login events happen
        whenever a characters is logged into via the SSO, regardless of mod.
        However, the mode should be send as an argument. Similarily,
        the Logout even happens whenever the character is deleted for either
        mode. The mode is sent as an argument, as well as the umber of
        characters still in the cache (if USER mode)
        """
        # self.settings = CRESTSettings.getInstance()
        #self.scopes = ['characterFittingsRead', 'characterFittingsWrite', 'esi-characters.read_standings.v1']

        self.dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler
        self.updateHandler = UpdateHandler()    # ToDo: Dangerous to start an own instance of updateHandler

        self.mainWindowCB = callback

        # these will be set when needed
        self.httpd = None
        self.state = None
        self.ssoTimer = None

        self.login()

    def login(self):
        """ this redirects the user to the EVE SSO login """
        # token = generate_token()
        # requests.session['token'] = token

        self.startServer()
        return webbrowser.open(esisecurity.get_auth_uri(scopes=config.ESI_SCOPES))

    def logout(self):
        """Logout of implicit character"""
        print("Character logout")
        self.implicitCharacter = None

    def stopServer(self):
        print("Stopping Server")
        self.httpd.stop()
        self.httpd = None

    def startServer(self):
        print("Starting server")
        if self.httpd:
            self.stopServer()
            time.sleep(1)
            # we need this to ensure that the previous get_request finishes, and then the socket will close
        self.httpd = StoppableHTTPServer((config.HOST, config.PORT), AuthHandler)

        self.serverThread = threading.Thread(target=self.httpd.serve, args=(self.callback,))
        self.serverThread.name = "ESIServer"
        self.serverThread.daemon = True
        self.serverThread.start()
        return

    def callback(self, parts):
        """ This is where the user comes after he logged in SSO """
        # get the code from the login process
        code = str(parts['code'][0])
        # token = str(parts['code'][0])

        # compare the state with the saved token for CSRF check

        # now we try to get tokens
        try:
            auth_response = esisecurity.auth(code)
        except APIException as e:
            return print('Login EVE Online SSO failed: %s' % e)

        # we get the character informations
        cdata = esisecurity.verify()

        # if the user is already authed, we log him out
        #if current_user.is_authenticated:
        #   logout_user()

        # now we check in database, if the user exists
        # actually we'd have to also check with character_owner_hash, to be
        # sure the owner is still the same, but that's an example only...

        user = User()
        user.CharacterID = cdata['CharacterID']
        user.CharacterOwnerHash = cdata['CharacterOwnerHash']
        user.CharacterName = cdata['CharacterName']
        user.update_token(auth_response)


        if True:    # ToDO: Do we need to verify if user is valid?
            user.id = self.dbHandler.saveUser(user)
            if user.id is not None:     # We don't want DB Entrys without owner
                self.updateHandler.updateUser(user)
                # self.mainWindowCB() ToDo: Why isn't this working?

        self.dbHandler.close()
        # now the user is ready, so update/create it and log the user

