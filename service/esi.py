from service.callback_server import StoppableHTTPServer, AuthHandler

from datetime import datetime

from service.esipy import App
from service.esipy import EsiClient
from service.esipy import EsiSecurity
from service.esipy.exceptions import APIException

import webbrowser
import requests
import service.config
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
class User():
    # our ID is the character ID from EVE API
    character_id = ""
    character_owner_hash = ""
    character_name = ""

    # SSO Token stuff
    access_token = ""
    access_token_expires = ""
    refresh_token = ""

    def get_id(self):
        """ Required for flask-login """
        return self.character_id

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security
        """
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires_in': (
                self.access_token_expires - datetime.utcnow()
            ).total_seconds()
        }

    def update_token(self, token_response):
        """ helper function to update token data from SSO response """
        self.access_token = token_response['access_token']
        self.access_token_expires = datetime.fromtimestamp(
            time.time() + token_response['expires_in'],
        )
        if 'refresh_token' in token_response:
            self.refresh_token = token_response['refresh_token']

# -----------------------------------------------------------------------
# ESIPY Init
# -----------------------------------------------------------------------
# create the app
esiapp = App.create(service.config.ESI_SWAGGER_JSON)

# init the security object
esisecurity = EsiSecurity(
    app=esiapp,
    redirect_uri=service.config.ESI_CALLBACK,
    client_id=service.config.ESI_CLIENT_ID,
    secret_key=service.config.ESI_SECRET_KEY,
)

# init the client
esiclient = EsiClient(
    security=esisecurity,
    cache=None,
    headers={'User-Agent': service.config.ESI_USER_AGENT}
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
        service.config.SECRET_KEY.encode(),
        random_string,
        hashlib.sha256
    ).hexdigest()


def login():
    """ this redirects the user to the EVE SSO login """
    # token = generate_token()
    # requests.session['token'] = token
    server = esi()
    server.startServer()
    return webbrowser.open(esisecurity.get_auth_uri(scopes=['esi-characters.read_standings.v1']))



class esi():

    def __init__(self):
        """
        A note on login/logout events: the character login events happen
        whenever a characters is logged into via the SSO, regardless of mod.
        However, the mode should be send as an argument. Similarily,
        the Logout even happens whenever the character is deleted for either
        mode. The mode is sent as an argument, as well as the umber of
        characters still in the cache (if USER mode)
        """

        # self.settings = CRESTSettings.getInstance()
        self.scopes = ['characterFittingsRead', 'characterFittingsWrite', 'esi-characters.read_standings.v1']

        # these will be set when needed
        self.httpd = None
        self.state = None
        self.ssoTimer = None

        self.eve_options = {
            'loginServer' : "https://login.eveonline.com",
            'client_id': "2e3ccffa023e4c9685ab8d549ffab9c8",
            'api_key': "",
            'redirect_uri': "http://localhost:6461",
            'testing': "false"
        }

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
        self.httpd = StoppableHTTPServer((service.config.HOST, service.config.PORT), AuthHandler)

        self.serverThread = threading.Thread(target=self.httpd.serve, args=(self.callback,))
        self.serverThread.name = "ESIServer"
        self.serverThread.daemon = True
        self.serverThread.start()
        return

    def callback(self, parts):
        """ This is where the user comes after he logged in SSO """
        # get the code from the login process
        code = parts.args.get('code')
        token = parts.args.get('state')

        # compare the state with the saved token for CSRF check
        sess_token = requests.session.pop('token', None)
        if sess_token is None or token is None or token != sess_token:
            return 'Login EVE Online SSO failed: Session Token Mismatch', 403

        # now we try to get tokens
        try:
            auth_response = esisecurity.auth(code)
        except APIException as e:
            return 'Login EVE Online SSO failed: %s' % e, 403

        # we get the character informations
        cdata = esisecurity.verify()

        # if the user is already authed, we log him out

        # now we check in database, if the user exists
        # actually we'd have to also check with character_owner_hash, to be
        # sure the owner is still the same, but that's an example only...

        user = User()
        user.character_id = cdata['CharacterID']

        user.character_owner_hash = cdata['CharacterOwnerHash']
        user.character_name = cdata['CharacterName']
        user.update_token(auth_response)

        # now the user is ready, so update/create it and log the user

