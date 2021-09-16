#importing math and sleep
from math import *
from time import sleep

#array definition
prompt = ["a: ", "b: ", "c: "] #this one's just so that I don't have to have a bunch of print statements
roots = []

#booleans
running = True

#integers
a = 1
b = 1
c = 0

#welcome!
sleep(1)
print(" -- Quadratic Calculator -- ")
sleep(2)
print("Enter the coefficients for ax^2 + bx + c = 0")
sleep(2)

#I broke everything down into their own functions so that debugging and finding
#things later would be easier

#getting those dang coefficients. it having its own function is a bit of a waste
#of space, but in case I want to add something that will affect the prompt I can find it here
def get_input(num):
    
    #the function takes the argument 'num' so that the prompt changes depending on which
    #coefficient it's requesting
    ans = input("Please enter coefficient " + prompt[num])
    return(int(ans))

#get_discriminant function using our trust quadratic formula
def get_discriminant(a, b, c):
    
    return((b**2) - (4*a*c)) #it returns the descriminant which the code will later use
    
#get_roots function to get those dang roots
def get_roots(a, b, c, root_list):
    #adding the roots to an array of roots 
    root_list.append((-b + sqrt(get_discriminant(a,b,c)))/(2*a))
    root_list.append((-b - sqrt(get_discriminant(a,b,c)))/(2*a))
    return(root_list) #returning the list so we can print it later

#calculate function that calls all the other functions! I'm pretty sure it's not
#great practice for functions to call other functions but I just want this calculate
#function to all be together as opposed to in the while loop
def calculate():
    
    #getting the inputs and assigning them to variables!
    a = get_input(0)
    b = get_input(1)
    c = get_input(2)
    
    #calling the get_discriminant function to test how many roots there are
    if get_discriminant(a,b,c) > 0:
        sleep(1)
        print("Root 1: "+str(get_roots(a,b,c,roots)[0])) #calling the roots and printing the first one
        sleep(.25)
        print("Root 2: "+str(get_roots(a,b,c,roots)[1])) # calling the roots and printing the second
        sleep(2)
        
    #if the discriminant is 0...
    elif get_discriminant(a,b,c) == 0:
        print("This quadratic has only one root. Here it is!")
        sleep(1)
        print("Root 1: "+str(get_roots(a,b,c,roots)[0]))
        sleep(2)
        
    #if the discriminant is less than 0 we don't do any math because that's some B.S.
    elif get_discriminant(a,b,c) < 0:
        print("This quadratic has no real roots.")
        sleep(2)

#function to ask user if they want to enter more variables
def loop():
    again = input("Press Enter to run again, or x to exit: ")
    if again == "":
        return(True)
    if again == "x":
        print("Goodbye!")
        sleep(1)
        return(False)
    else:
        print("Hm, I don't recognize that. Terminating program.") #was to lazy to make it loop
        sleep(1)
        return(False)
        
#bad boy while loop
while running:
    try:
        calculate()
    except ValueError: #catching those silly, silly users
        print("You goofy goober! Please only input integers.")
        sleep(2)
    roots = [] #CLEARING THE ROOTS LIST. VERY IMPORTANT.
    
    running = loop() #depending on what the loop() function returns, the while loop will or will not loop
    
    
