# Name: Kyler Drury Lab Partner: Patrick Boudreaux
#
# Course: CSE 1284 Sec 12 Date Assigned: 10-2-14
#
# File name: dicegame Date Due: 10-2-14.
#
# Program Description: A simple dice game.
# A meaningless comment
import random

SA = 1
SB = 1
playerOneturn = True
while SA <= 100 and SB <= 100:
    while playerOneturn == True:
        number = random.randint(1, 6)
        SA = SA + number
        if number == 2 or number == 3 or number == 4 or number == 5:
            playerOneturn = False
            print("A= ",number, "SA =", SA, "it is the turn of player B")
            input("Hit Enter to roll the die")
            if SA >= 100:
                break
        else:
            playerOneturn = True
            print("A= ",number, "SA =", SA, "it is the turn of player A")
            input("Hit Enter to roll the die")
        if SA == 99:
            SA = 6
        elif SA == 88:
            SA = 67
        elif SA == 71:
            SA = 29
        elif SA == 24:
            SA = 1
        elif SA == 55:
            SA = 13
        elif SA == 8:
            SA = 31
        elif SA == 15:
            SA = 97
        elif SA == 42:
            SA = 81
        elif SA == 66:
            SA = 87
        if SA >= 100:
            break
        if SB >= 100:
            break   
    while playerOneturn == False:
        number = random.randint(1, 6)
        SB = SB + number
        if number == 2 or number == 3 or number == 4 or number == 5:
            playerOneturn = True
            print("B= ",number, "SB =", SB, "it is the turn of player A")
            input("Hit enter to throw the die:")
        else:
            playerOneturn = False
            print("B= ",number, "SB =", SB, "it is the turn of player B")
            input("Hit enter to throw the die:")
        if SB == 99:
            SB = 6
        elif SB == 88:
            SB = 67
        elif SB == 71:
            SB = 29
        elif SB == 24:
            SB = 1
        elif SB == 55:
            SB = 13
        elif SB == 8:
            SB = 31
        elif SB == 15:
            SB = 97
        elif SB == 42:
            SB = 81
        elif SB == 66:
            SB = 87
        if SB >= 100:
            break
        if SA >= 100:
            break
if SA > SB:
    print("Player A has won!")
elif SB > SA:
    print("Player B has won!")
else:
    print("Its a tie!")
            
        

    
        
