import service.esi

if __name__ == "__main__":

    print("Welcome to deppster. Input Command or Help for Help.")

    while True:
        command = input()

        if command == "Help":
            print("Available Commands:\nlogin: Login to your Eve Account to get rights\nexit: Exit Program")
        elif command == "login":
            service.esi.login()
        elif command == "exit":
            break