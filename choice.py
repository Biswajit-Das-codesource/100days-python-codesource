import math
import random

lownumber=int(input("enter the low boundry......."))
highnumber=int(input("enter the highboundry......"))

gamechoice= int(random.randint(lownumber,highnumber))

userchoice=int(input("Enter the number......"))

while userchoice!=gamechoice:
   userchoice=int(input("reenter your choice: "))
print("congratulation you win the game..... ")

        
    


