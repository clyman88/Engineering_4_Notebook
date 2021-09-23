file1 = open("log.txt", "a")

def determine():
	det = input("Would you like to sign in or sign up? (in/up)")
	if det == "in":
		signi()
	elif det == "up":
		pass
	else:
		print("Please type 'in' or 'up'")
		determine()

def signi():
	username = input("Please enter the username you will use:")
	password = input("Please enter the password you will use:")
	file1.write(username + "," + password + "~ \n")
	file2 = open("count.txt", "r")
	new_line_count =str(int(file2.read())+1)
	file2.close()
	file2 = open("count.txt","w")
	file2.write(new_line_count)
	file2.close()
	print("Thank you for signing up!")
def signu():
	pass

determine()
file1.close()

file1 = open("log.txt","r")
file2 = open("count.txt","r")
print(file1.read())
print(file2.read())
file1.close()
file2.close()
