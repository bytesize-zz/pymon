import swagger_client

from db.databaseHandler import DatabaseHandler

class UpdateHandler():
    def __init__(self, parent=None):
        super(UpdateHandler, self).__init__()

        self.dbHandler = DatabaseHandler()

    def updateAll(self):

        # for each char in list do
        userList = self.dbHandler.getAllUser()
        for user in userList:
            self.updateCharacter(user)

    def updateCharacter(self, user):

        api = swagger_client.CharacterApi()


