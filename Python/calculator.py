#Calculator Program
#Written by Cole Lyman

#importing time function so that people can follow what's happening
from time import sleep

#I truly hated the giant block of print statements so much, this was my solution
spice = ["Sum: ", "Difference: ", "Product: ", "Quotient: ", "Modulo: ", "First Factorial: ", "Second Factorial: "]

#welcome!
print('\n -- Calculator -- \n')

#chunky calculator function
def calc(a,b,c):
    
    #sum
    if c==0:
        return(a+b)
        
    #difference
    elif c==1:
        return(a-b)
        
    #product    
    elif c==2:
        return(a*b)
    
    #quotient
    elif c==3:
        return(a/b)
        
    #modulo
    elif c==4:
        return(a%b)
        
    #factorials
    elif c==5:
        d = 1
        for i in range(1,a+1):
            d = d*i
        return(d)
    
    elif c==6:
        e = 1
        for i in range(1,b+1):
            e = e*i
        return(e)

#main function. generally not a fan of spewing code everywhere w/o the
#inherent organization of functions.
def main():
    
    #gettin inputs
    sleep(1)
    num1 = input('Enter first integer: ')
    num2 = input('Enter second integer: ')
    
    #need to convert to int type. if the input is not convertable it will throw an Error
    #that will be caught
    
    num1 = int(num1)
    num2 = int(num2)
        
    #terrible, terrible print code that was so bad it has been commented out
    '''sleep(1)    
    print('Sum: ' + str(calc(num1,num2,1)))
    sleep(.5)
    print('Difference: ' + str(calc(num1,num2,2)))
    sleep(.5)
    print('Product: ' + str(calc(num1,num2,3)))
    sleep(.5)
    print('Quotient: ' + str(calc(num1,num2,4)))
    sleep(.5)
    print('Modulo: ' + str(calc(num1,num2,5)))
    sleep(.5)
    print('1st Factorial: ' + str(calc(num1,num2,6)))
    sleep(.5)
    print('2nd Factorial: ' + str(calc(num1,num2,7)))
    sleep(.5)'''
    
    #sexy, spicy print code
    for i in range(0,7):
        sleep(.5)
        print(spice[i] + str(calc(num1,num2,i)))
        
    #sometimes my genius...it almost frightens me
    
while True:
    
    #this try/except will hopefully catch all smartasses
    try:
        main()
        again = input("\nNew equation (y/n)? ")
        if again == "y":
            pass
            print("\n")
        elif again == "n":
            break
        else:
            break
            
    except ValueError:
        print('Error detected. Please enter an integer. Retrying...')
        
    
