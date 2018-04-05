from __future__ import print_function

from pprint import pprint
import config

import swagger_client
from swagger_client.rest import ApiException
from service.updateHandler import UpdateHandler

# gui imports
from gui.mainwindow import GeneralMainDesign
from PyQt5.QtWidgets import QApplication

import threading
import sys
import datetime

def getAlliance():
    # create an instance of the API class
    api_instance = swagger_client.AllianceApi()
    datasource = 'tranquility'  # str | The server name you would like data from (optional) (default to tranquility)
    user_agent = 'user_agent_example'  # str | Client identifier, takes precedence over headers (optional)
    x_user_agent = 'x_user_agent_example'  # str | Client identifier, takes precedence over User-Agent (optional)

    try:
        # List all alliances
        api_response = api_instance.get_alliances(datasource=datasource, user_agent=user_agent,
                                                  x_user_agent=x_user_agent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AllianceApi->get_alliances: %s\n" % e)


def getStandings():
    with open('user.txt') as f:
        lines = f.readlines()
    character_id = int(lines[0])
    access_token = lines[1]

    api = swagger_client.CharacterApi()
    # Set a relevant user agent so we know which software is actually using ESI
    api.api_client.set_default_header(config.ESI_USER_AGENT, config.ESI_AGENT_DESCRIPTION)
    api.api_client.host = "esi.evetech.net"
    api.api_client.configuration.access_token = access_token  # fill in your access token here

    try:
        response = api.get_characters_character_id_standings(character_id)  # fill in the character id here
        print(response)
    except ApiException as e:
        print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)

def getWallet():
    with open('user.txt') as f:
        lines = f.readlines()
    character_id = int(lines[0])
    access_token = lines[1]

    wallet_api = swagger_client.WalletApi()

    wallet_api.api_client.set_default_header(config.ESI_USER_AGENT,
                'https://github.com/Kyria/EsiPy')  # Set a relevant user agent so we know which software is actually using ESI
    wallet_api.api_client.host = "esi.evetech.net"
    wallet_api.api_client.configuration.access_token = access_token  # fill in your access token here

    try:
        wallet = wallet_api.get_characters_character_id_wallet(character_id)
        print("Balance: "+str(wallet))
    except ApiException as e:
        print("Exception when calling WalletApi->get_characters_character_id_wallet: %s\n" % e)


if __name__ == "__main__":

    try:

        config.TIME_DIFFERENCE = datetime.datetime.now() - datetime.datetime.utcnow()

        app = QApplication(sys.argv)
        #updateHandler = UpdateHandler()
        #updateHandler.updateAll()
        mainwindow = GeneralMainDesign()


        updateThread = threading.Thread(target=UpdateHandler().updateAll())
        updateThread.name = "UpdateHandler"
        updateThread.daemon = True
        updateThread.start()


        #mainwindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
