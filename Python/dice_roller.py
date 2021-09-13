#Automatic Dice Roller
#Written by Cole Lyman

from random import randint
from time import sleep

sides = 6
modifier = 0
quantity = 1
roll = ""
running = True

print(" --- Automatic Dice Roller --- ")

def setup():
    while True:
        global sides
        global quantity
        sides = input("How many sides would you like on your di(c)e?")
        quantity = input("How many dice would you like to roll?")
        
        try:
            sides = int(sides)
            quantity = int(quantity)
            break
        except ValueError:
            print("Error detected. Non-integer answers are not allowed. Trying again...")
            sleep(1)

setup()

def main(x, y):
    
    global running
    roll = input("Press 'Enter' to roll. Press 'c' and then 'Enter' to change dice sides/quantity. Press 'x' and then 'Enter' to exit.")
    
    if roll == "":
        print("\n- Dice Values: -")
        sleep(.2)
        for i in range(0, y):
            print("  " + str(randint(1,x)))
            sleep(.2)
        print("\n")
            
    elif roll == "c":
        setup()
        
    elif roll == "x":
        print("Goodbye!")
        running = False
        
    elif roll == "1":
        print("Debugging:")
        print("Sides: " + str(x))
        print("Quantity: " +str(y))
        
    else:
        print("That is not a valid answer. Trying again...")
        sleep(1)
        main(sides, quantity)
    
while running:
    main(sides, quantity)
