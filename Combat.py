from Player import *
import os
import time
from colours import *

class Combat:
    def __init__(self) -> None:
        self.team1 = []
        self.team2 = []
        self.clearcls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    def AddPlayer(self, player):
        self.team1.append(player)
    
    def ShowTeam(self, team):
        i = 0
        if team == 1:
            for player in self.team1:
                print(i,": ",end="")
                player.ShowStats()
                i+=1
        else:
            for player in self.team2:
                print(i,": ",end="")
                player.ShowStats()
                i+=1

    def AddOpponent(self, player):
        self.team2.append(player)

    def Fight(self):
        self.clearcls()
        switch2 = False
        while switch2 == False:
            print(Colors.BOLD + "-> 0 - New game" + Colors.ENDC)
            print(Colors.BOLD + "-> 1 - Load game" + Colors.ENDC)
            input_game = input("Enter the number: ")
            if input_game == "0":
                switch2 = True
                pass
            elif input_game == "1":
                switch2 = True
                file = open("save.txt", "r")
                f_line = file.readline().split(" ")
                n1 = f_line[0].strip()
                n2 = f_line[-1].strip()
                if int(n1) == 0 or int(n2) == 0:
                    print(Colors.FAIL + "There's no enough players in one of the teams!" + Colors.ENDC)
                    switch2 = False
                self.team1.clear()
                self.team2.clear()
                read_team1 = []
                read_team2 = []
                i = 0
                while i < int(n1):
                    read_team1.append(file.readline().strip())
                    i += 1
                i = 0
                while i < int(n2):
                    read_team2.append(file.readline().strip())
                    i += 1
                
                warrior = []
                for element in range(len(read_team1)):
                    warrior = read_team1[element].split(" ")
                    self.team1.append(Player(warrior[0], int(warrior[1]), int(warrior[2]), int(warrior[3]), Item(warrior[4], int(warrior[5]), int(warrior[6]), int(warrior[7]))))
                warrior = []
                for element in range(len(read_team2)):
                    warrior = read_team2[element].split(" ")
                    self.team2.append(Player(warrior[0], int(warrior[1]), int(warrior[2]), int(warrior[3]), Item(warrior[4], int(warrior[5]), int(warrior[6]), int(warrior[7]))))
                file.close()
            else:
                self.clearcls()
                print("Enter correct number!")
        while len(self.team1) > 0 and len(self.team2) > 0:
            self.clearcls()
            print(Colors.OKGREEN + "Your team:" + Colors.ENDC)
            self.ShowTeam(1)
            print(Colors.BOLD + "-------------------------------" + Colors.ENDC)
            print(Colors.FAIL + "Enemy team:" + Colors.ENDC)
            self.ShowTeam(2)
            playerIndex = int(input("Pick warrior: "))
            self.clearcls()
            print(Colors.OKGREEN + "Your warrior:" + Colors.ENDC)
            self.team1[playerIndex].ShowStats()
            print(Colors.BOLD + "-------------------------------" + Colors.ENDC)
            self.ShowTeam(2)
            opponentIndex = int(input("Pick Opponent: "))
            self.clearcls()
            print(Colors.OKGREEN + "Your warrior:" + Colors.ENDC)
            self.team1[playerIndex].ShowStats()
            print("-------------------------------")
            print(Colors.FAIL + "Your enemy:" + Colors.ENDC)
            self.team2[opponentIndex].ShowStats()
            print(Colors.BOLD + "-------------------------------" + Colors.ENDC)
            print("Players fighting...")
            time.sleep(3)
            playerDMG = self.team1[playerIndex].Attack()
            self.team2[opponentIndex].ModifyHP(playerDMG)
            print("Player deals: ", playerDMG, "damage to opponent")
            time.sleep(1)
            if self.team2[opponentIndex].HP > 0:
                self.team1[playerIndex].ModifyHP(self.team2[opponentIndex].dmg)
                print("Opponent deals", self.team2[opponentIndex].dmg)
            else:
                print("Opponent is dead")
                self.team2.pop(opponentIndex)
                self.team1[playerIndex].LevelUp()
            if self.team1[playerIndex].HP > 0:
                pass
            else:
                print("Player is dead")
                self.team1.pop(playerIndex)
                self.team2[opponentIndex].LevelUp()
            
            if len(self.team1) == 0:
                print(Colors.FAIL + "You lost!" + Colors.ENDC)
                quit()
            elif len(self.team2) == 0:
                print(Colors.OKGREEN + "Your win!" + Colors.ENDC)
                quit()
                
            print(Colors.BOLD + "-------------------------------" + Colors.ENDC)
            switch = False
            while switch == False:
                option = input("Continue?" + Colors.BOLD + "\n" + "-> 0 - Continue" + "\n" + "-> 1 - Save to file and quit" + "\n" + "-> 2 - Save to file and continue" + "\n" + "-> 3 - Quit" + Colors.ENDC + "\n" + "Enter the number: ")
                if option == "0":
                    switch = True
                    break
                elif option == "1":
                    switch = True
                    file = open("save.txt", "w")
                    file.write(str(len(self.team1)) + " " + str(len(self.team2)) + "\n")
                    i = 0
                    while i < len(self.team1):
                        file.write(str(self.team1[i].name) + " ")
                        file.write(str(self.team1[i].dmg) + " ")
                        file.write(str(self.team1[i].HP) + " ")
                        file.write(str(self.team1[i].exp) + " ")
                        file.write(str(self.team1[i].item.name) + " ")
                        file.write(str(self.team1[i].item.dmg) + " ")
                        file.write(str(self.team1[i].item.critDMG) + " ")
                        if i == len(self.team1)-1:
                            file.write(str(self.team1[i].item.critChance))
                        else:
                            file.write(str(self.team1[i].item.critChance) + "\n")
                        i += 1
                    i = 0
                    file.write("\n")
                    while i < len(self.team2):
                        file.write(str(self.team2[i].name) + " ")
                        file.write(str(self.team2[i].dmg) + " ")
                        file.write(str(self.team2[i].HP) + " ")
                        file.write(str(self.team2[i].exp) + " ")
                        file.write(str(self.team2[i].item.name) + " ")
                        file.write(str(self.team2[i].item.dmg) + " ")
                        file.write(str(self.team2[i].item.critDMG) + " ")
                        if i == len(self.team2)-1:
                            file.write(str(self.team2[i].item.critChance))
                        else:
                            file.write(str(self.team2[i].item.critChance) + "\n")
                        i += 1
                    print(Colors.FAIL + "You escaped!" + Colors.ENDC)
                    file.close()
                    quit()
                elif option == "2":
                    switch = True
                    file = open("save.txt", "w")
                    file.write(str(len(self.team1)) + " " + str(len(self.team2)) + "\n")
                    i = 0
                    while i < len(self.team1):
                        file.write(str(self.team1[i].name) + " ")
                        file.write(str(self.team1[i].dmg) + " ")
                        file.write(str(self.team1[i].HP) + " ")
                        file.write(str(self.team1[i].exp) + " ")
                        file.write(str(self.team1[i].item.name) + " ")
                        file.write(str(self.team1[i].item.dmg) + " ")
                        file.write(str(self.team1[i].item.critDMG) + " ")
                        if i == len(self.team1)-1:
                            file.write(str(self.team1[i].item.critChance))
                        else:
                            file.write(str(self.team1[i].item.critChance) + "\n")
                        i += 1
                    i = 0
                    file.write("\n")
                    while i < len(self.team2):
                        file.write(str(self.team2[i].name) + " ")
                        file.write(str(self.team2[i].dmg) + " ")
                        file.write(str(self.team2[i].HP) + " ")
                        file.write(str(self.team2[i].exp) + " ")
                        file.write(str(self.team2[i].item.name) + " ")
                        file.write(str(self.team2[i].item.dmg) + " ")
                        file.write(str(self.team2[i].item.critDMG) + " ")
                        if i == len(self.team2)-1:
                            file.write(str(self.team2[i].item.critChance))
                        else:
                            file.write(str(self.team2[i].item.critChance) + "\n")
                        i += 1
                    file.close()
                elif option == "3":
                    switch = True
                    print(Colors.FAIL + "You escaped!" + Colors.ENDC)
                    exit()
                else:
                    print("Enter correct number!")