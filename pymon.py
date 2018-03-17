from __future__ import print_function

import service.esi
import service.config
import swagger_client
from swagger_client.rest import ApiException
from swagger_client import Configuration

import time
from pprint import pprint

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
    api.api_client.set_default_header(service.config.ESI_USER_AGENT,
                'https://github.com/Kyria/EsiPy')  # Set a relevant user agent so we know which software is actually using ESI
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

    wallet_api.api_client.set_default_header(service.config.ESI_USER_AGENT,
                'https://github.com/Kyria/EsiPy')  # Set a relevant user agent so we know which software is actually using ESI
    wallet_api.api_client.host = "esi.evetech.net"
    wallet_api.api_client.configuration.access_token = access_token  # fill in your access token here

    try:
        wallet = wallet_api.get_characters_character_id_wallet(character_id)
        print("Balance: "+str(wallet))
    except ApiException as e:
        print("Exception when calling WalletApi->get_characters_character_id_wallet: %s\n" % e)


if __name__ == "__main__":

    print("Welcome to pymon. Input command or help for help.")

    while True:
        command = input()

        if command == "help":
            print("Available Commands:\n"
                  "help: see this help\n"
                  "login: Login to your Eve Account to get rights\n"
                  "standings: get list of standings after login\n"
                  "exit: Exit Program")
        elif command == "login":
            service.esi.login()

        elif command == "standings":
            getStandings()
        elif command == "wallet":
            getWallet()
        elif command == "exit":
            break