#Python Challenge - MSP (ENGR4)

#Written by Cole Lyman

#9.28.2021

from time import sleep

#defining all the variables I'll be using for the program
pinata = ["---┐", "\n   o","\n  /","|", "\\", "\n  /"," \\"] #This is each iteration of the MSP themselves!
numbers = ["0","1","2","3","4","5","6","7","8","9"] #A list of numbers; I use this to check if any numbers are used in the word given

missed_characters = [] 
guessed_characters = []
words = []
letters = []
mystery = []

word = ""

#I do not end up using these variables, but I keep them around because they've grown on me.
player1 = ""
player2 = ""
p1_score = 0
p2_score = 0
p2_guesser = True


#This was my attempt at saving users and the number of games they've won throughout rebooting the system.
'''
def opening():
    global player1
    global player2
    exists = False
    p1 = input("Player 1, enter username: ")
    p2 = input("Player 2, enter username: ")
    doc = open("players.txt", "r")
    document = doc.read().split("\n")
    for i in range(0,len(document)):
        test = document[i].split("~")
        if p1 in test:
            player1 = test[0]
            p1_score = test[1]
            doc.close()
            print("Welcome back! "+player1+", you have won "+p1_score+" games.")
            exists = True
            break
    if exists == False:
        doc = open("players.txt", "a")
        doc.write("\n" + p1+"~0")
        print("created new player.")
        doc.close()
    sleep(2)
    print(p1 +", you will enter the first word.")
    sleep(2)

opening()'''
#I decided it was lame once I couldn't figure out how to replace specific lines.

#Function for outputting the pinata! The argument it takes is how many incorrect guesses there have been.
def print_pinata(n):
    p = ""
    for i in range(0,n+1):
        p += pinata[i]
    print(p)
    
#assigning the word that will be guest to various lists and such.
def assign(given,num, list1):
    letters = []
    list1.clear()
    for b in given:
        letters.append(b) #adding each letter to a fun list.
        list1.append("_")
    if num==2:
        return letters
    if num==3:
        return(list1)
     
#checks if guesses are correct.
def check_if_correct(guess, letters, output):
    correct = False
    for i in range(0, len(letters)):
        if guess.lower() == letters[i].lower():
            output[i] = guess
            correct = True
    if correct:
        return(output)
    else:
        return(False)
    
#"mystery" is the term I coined for the "___" displayed.
def print_mystery(list1):
    b = ""
    for i in range(0,len(list1)):
        b += list1[i] + " "
    return b
        
#If the input is multiple words, this essentially "guesses" spaces so that the user doesn't have to. This way
#spaces will also be displayed as "___ _______ ___" or some iteration of that.
def spaces(letters, mystery):
    if check_if_correct(" ", letters, mystery) != False:
        mystery = check_if_correct(" ", letters, mystery)
    
#Checking if the game has been won or lost
def check_win_condition(num1, list1):
    if num1 >= 6:
        return(3)
    
    if '_' not in list1:
        return(2)
        
    else:
        return(1)

#function called to determine the word to be guessed
def start():  
  global word
  global letters
  global mystery
  global missed_characters
  global guessed_characters
  run_loop = True
  while run_loop:
    word = input("Enter word(s): ")
    for i in numbers:
      if i in word:
        print("Please do not include numbers.")
        run_loop = False
    if not run_loop:
      run_loop = True
    else:
      run_loop =False
  letters = assign(word, 2, mystery)
  mystery = assign(word, 3, mystery)
  spaces(letters, mystery)
  missed_characters = []
  guessed_characters = []

running = True
start()

#Big chunky while loop

while running:
    
    #clears screen, then prints EVERYTHING
    print("\n"*50)
    print_pinata(len(missed_characters))
    print("\n"*2)
    ml = ""
    for i in missed_characters:
      ml+=i
      ml += " "
    print("Missed letters: "+ml)
    print("\n")
    print(print_mystery(mystery))
    print("\n")

    #Another while loop to make sure the guess makes sense and isn't a number, more than one letter, or a previous guess.
    while True:
        guess = input("Guess: ")
        guess.lower()
        if guess in guessed_characters:
            print("You have already guessed that letter.")
            sleep(1)
        elif len(guess) > 1:
          print("Please only input one-letter...letters.")
          sleep(1)
        else:
          try:
            int(guess)
            print("Please only input letters.")
          except ValueError:
            break
        
    #I have two lists: missed_characters and guessed_characters. Missed_characters are used to be displayed and guessed_characters are used to catch repeats
    if check_if_correct(guess, letters, mystery) != False:
        mystery = check_if_correct(guess, letters, mystery)
        guessed_characters.append(guess)
    else:
        missed_characters.append(guess)
        guessed_characters.append(guess)
        
    #checking win conditions
    if check_win_condition(len(missed_characters), mystery) ==1:
        pass
    elif check_win_condition(len(missed_characters), mystery) == 2:
      print("\n"*50)
      print_pinata(len(missed_characters))
      print("\n"*2)
      ml = ""
      for i in missed_characters:
        ml+=i
        ml += " "
      print("Missed letters: "+ml)
      print("\n")
      print(print_mystery(mystery))
      print("\n")
      print("Victory! Good game. You won in " + str(len(guessed_characters)) + " guesses.")
      sleep(2)
      if p2_guesser == True:
        pass
      play_again = input("Play again? (y/n): ")
      if play_again == "y":
        start()
      else:
        running = False
        break
    elif check_win_condition(len(missed_characters), mystery) == 3:
        print("\n"*50)
        print_pinata(len(missed_characters))
        print("\n"*2)
        ml = ""
        for i in missed_characters:
          ml+=i
          ml += " "
        print("Missed letters: "+ml)
        print("\n")
        print(print_mystery(mystery))
        print("\n")
        print("Too bad! The word was " + word + ".")
        sleep(2)
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            start()
        else:
          running = False
          break
