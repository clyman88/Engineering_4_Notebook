#Automatic Dice Roller
#Written by Cole Lyman

#importing my functions
from random import randint
from time import sleep

#making my variables that
sides = 6
modifier = 0 #unused modifier for your barb with +10 to athletics checks
quantity = 1
roll = ""
running = True #while condition

#welcome!
print(" --- Automatic Dice Roller --- ")

#settings function where you specify
def setup():
    
    #while loop that will keep going until integers have been inputted
    while True:
        
        global sides #making them global so that the function can directly alter them.
        global quantity #in hindsight I didn't really need to do this and could've had the function return the inputs. Oh well.
        sides = input("How many sides would you like on your di(c)e?")
        quantity = input("How many dice would you like to roll?")
        
        try:
            sides = int(sides)
            quantity = int(quantity)
            break
        except ValueError:
            print("Error detected. Non-integer answers are not allowed. Trying again...")
            sleep(1)
            
#calling that banger function
setup()

#main function requiring the arguments x and y, for # of sides and quantity
def main(x, y):
    
    global running #again, could've just returned True/False.
    
    roll = input("Press 'Enter' to roll. Press 'c' and then 'Enter' to change dice sides/quantity. Press 'x' and then 'Enter' to exit.")
    
    #if enter is selected:
    if roll == "":
        print("\n- Dice Values: -")
        sleep(.2)
        for i in range(0, y): #as many times as the quantity is, print a random integer 
            print("  " + str(randint(1,x))) #with the bounds 1 to side number
            sleep(.2)
        print("\n")
            
    #if c is selected:
    elif roll == "c":
        setup() #run previous setup function
        
    #if x is selected:
    elif roll == "x":
        print("Goodbye!")
        running = False #breaking out of that while loop
        
    # a secret command just for me :D
    elif roll == "1":
        print("Debugging:")
        print("Sides: " + str(x))
        print("Quantity: " +str(y))
        
    #catch-all
    else:
        print("That is not a valid answer. Trying again...")
        sleep(1)
        main(sides, quantity)
    
#actual while loop
while running:
    main(sides, quantity)
