from time import sleep

from colorama import *

print(" ")

for i in range(0,10):
	print(str(i+1) + ". Hello, world!")
	sleep(.125)

def game():
	sleep(1)
	print(" ")
	name = str(input('Please input name: '))
	if name == 'Cole Lyman':
		sleep(.125)
		print(" ")
		print("Welcome back, user. It's good to see you again.")
		print(" ")
		sleep(.5)
	else:
		sleep(.125)
		print(" ")
		print("Wow, nice name! Great to meet you, " + name + ".")
		print(" ")
		sleep(.5)
game()

