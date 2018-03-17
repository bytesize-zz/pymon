import service.esi
import service.config
import swagger_client
from swagger_client.rest import ApiException
from swagger_client import Configuration



def getInfos():
    api = swagger_client.CharacterApi()
    api.api_client.set_default_header(service.config.ESI_USER_AGENT,
                                      'my-test-agent')  # Set a relevant user agent so we know which software is actually using ESI
    api.api_client.host = "https://esi.tech.ccp.is"
    Configuration().access_token = "{access token}"  # fill in your access token here
    try:
        response = api.get_characters_character_id_standings(243749396)  # fill in the character id here
        print(response)
    except ApiException as e:
        print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)




if __name__ == "__main__":

    print("Welcome to pymon. Input command or help for help.")

    while True:
        command = input()

        if command == "help":
            print("Available Commands:\n"
                  "help: see this help\n"
                  "login: Login to your Eve Account to get rights\n"
                  "get: get some after login\n"
                  "exit: Exit Program")
        elif command == "login":
            service.esi.login()

        elif command == "get":
            print("Token:" + Configuration().access_token + "\n")
            # getInfos()
        elif command == "exit":
            break