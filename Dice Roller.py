## Version 1.0.4
## By Addison Djatschenko

##########################################################

## Allows random numbers to be used in the file
import random
## Allows time in between rolls
import time
## User inputs
while(True):
    times = int( input('Amount of rolls: '))
    if(times > 0):
        break
    else:
        print("The amount of rolls must be at least one")

while(True):
    sides = int( input('Amount of sides: '))
    if(sides > 3):
        break
    else:
        print("The dice needs to have at least four faces")
while(True):
    numberOfDices = int( input('Number of dices per roll:'))
    if(numberOfDices > 0):
        break
    else:
        print("The number of dice needs to be at least one")
while(True):    
    wait = float( input('Seconds in between each roll: '))
    if(wait >= 0):
        break
    else:
        print("The interval between each roll must be egual or greater than 0")
## Sets the dice rolls so far to zero
timesSoFar = int( 0)
## Runs until timesSoFar equals times
while timesSoFar != times:
    ## Displays current dice roll
    print([random.randint(1, sides) for ndice in range(0,numberOfDices)])
    ## Increments timesSoFar
    timesSoFar += 1
    ## Waits for wait seconds
    time.sleep(wait)
while timesSoFar == timesSoFar:
    ## Stops program without exiting
    time.sleep(1)
