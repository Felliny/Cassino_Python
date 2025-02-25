import random
import time

from model.Player import Player

class GameController:
    players = []

    def menu(self):
        option = ""

        while option != "exit":
            print("Type 'exit' to leave")
            option = input("1 - Play \n2 - New Player \n3 - Deposit Cash \n")

            match option:
                case "1":
                    self.play()
                case "2":
                    self.new_player()
                case "3":
                    self.update_cash()
                case "exit":
                    print("Leaving...")
                case _:
                    print("Wrong option!!!")




    def new_player(self):
        player = Player()


        while True:
            player.name = input("Name: ")

            if self.player_exists(player) == True:
                print("This name already exist!")
            else:
                break


        player.password = input("Password: ")

        while True:
            try:
                player.cash = float(input("cash: "))
                break
            except ValueError:
                print("Invalid Number!!!")


        print("Success!!")

        self.players.append(player)




    def update_cash(self):
        player =  Player()
        option = ""

        while True:
            player.name = input("Name: ")

            if not self.player_exists(player):
                print("Player doesn't exist!!!")
                print("New Player?")
                option = input("yes or no: ")

                if option == "yes":
                    self.new_player()
                    break

            else:
                break


        while True:
            if option == "yes":
                break

            player.password = input("password: ")
            password_check, player = self.check_password(player)

            if password_check == False:
                print("Wrong password")
            else:
                break



        while True:
            if option == "yes":
                break


            try:
                new_cash = float(input("cash: "))
                break
            except ValueError:
                print("Invalid Number!!!")


        if option != "yes":
            player.cash += new_cash
            print("Success!")




    def play(self):
        player = Player()

        while True:
            player.name = input("Name: ")

            if not self.player_exists(player):
                print("Player doesn't exist!!!")
                print("New Player?")
                option = input("yes or no: ")

                if option == "yes":
                    self.new_player()

            else:
                break


        while True:
            player.password = input("Password: ")
            password_check, player = self.check_password(player)

            if not password_check:
                print("Wrong password")
            else:
                break


        while True:
            print("Type 'cancel' to exit or any key to play")
            print("cash: {}".format(player.cash))


            if player.cash <= 0:
                print("\n No money, no gambling")
                break

            option = input("option: ")

            if option != "cancel":
                print("\n\n Playing! \n")
                time.sleep(3)
            else:
                print("Closing...")
                break


            number1 = random.randint(1, 9)
            number2 = random.randint(1, 9)
            number3 = random.randint(1, 9)


            print("Result: {}{}{}".format(number1, number2, number3))

            if number1 == 1 and number2 == 1 and number3 == 1:
                player.cash = 0
                print("Lost all te cash!!!")
                break
            elif number1 == number2 and number2 == number3 and number1 != 9:
                player.cash += player.cash * 2
                print("WIN 2x")
            elif number1 == 9 and number2 == 9 and number3 == 9:
                print("WIN WIN WIN WIN x3")
                player.cash += player.cash * 3
            elif number1 == number2 or number3 == number1 or number2 == number3:
                print("LOST -5,00")
                player.cash -= 5
            else:
                print("LOST -10,00")
                player.cash -= 10







    def player_exists(self, player):
        playerExist = False

        for playerList in self.players:
            if player.name == playerList.name:
                playerExist = True

        return playerExist



    def check_password(self, player):
        password_correct = False

        for playerList in self.players:
            if player.password == playerList.password and player.name == playerList.name:
                password_correct = True
                player = playerList


        return password_correct, player