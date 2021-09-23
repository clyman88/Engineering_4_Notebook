from time import sleep

pinata = ["---┐", "\n   o","\n  /","|", "\\", "\n  /"," \\"]
missed_characters = []
guessed_characters = []
words = []
letters = []
mystery = []
word = ""
player1 = ""
player2 = ""
p1_score = 0
p2_score = 0

def opening():
    global player1
    global player2
    p1 = input("Player 1, enter username: ")
    p2 = input("Player 2, enter username: ")
    doc = open("players.txt", "r")
    print(doc.readlines())
    for i in doc.readlines():
        if p1 in doc.readlines()[i]:
            reading = doc.readlines()[i].split("~")
            player1 = reading[0]
            p1_score = reading[1]
            doc.close()
            print("welcome back!")
        else:
            doc.close()
            doc = open("players.txt", "a")
            doc.write("\n" + p1+"~0")
            print("created new player.")
    
    
def print_pinata(n):
    p = ""
    for i in range(0,n+1):
        p += pinata[i]
    print(p)
    
def assign(given,num, list1):
    letters = []
    list1.clear()
    for b in given:
        letters.append(b)
        list1.append("_")
    if num==2:
        return letters
    if num==3:
        return(list1)
        
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
    
    
def print_mystery(list1):
    b = ""
    for i in range(0,len(list1)):
        b += list1[i] + " "
    return b
        
def spaces(letters, mystery):
    if check(" ", letters, mystery) != False:
        mystery = check(" ", letters, mystery)
    
def check_win_condition(num1, list1):
    if num1 >= 7:
        return(3)
    
    if '_' not in list1:
        return(2)
        
    else:
        return(1)

def start():  
  global word
  global letters
  global mystery
  global missed_characters
  global guessed_characters
  word = input("Enter word(s): ")
  letters = assign(word, 2, mystery)
  mystery = assign(word, 3, mystery)
  spaces(letters, mystery)
  missed_characters = []
  guessed_characters = []

running = True
start()
while running:
    
    print("\n"*50)
    print_pinata(len(missed_characters))
    print("\n")
    print(print_mystery(mystery))
    print("\n")
    
    while True:
        guess = input("Guess: ")
        if guess in guessed_characters:
            print("You have already guessed that letter. Please try again.")
            sleep(1)
        elif len(guess) > 1:
          print("Please only input one-letter...letters.")
        else:
            break
        
    if check_if_correct(guess, letters, mystery) != False:
        mystery = check(guess, letters, mystery)
        guessed_characters.append(guess)
    else:
        missed_characters.append(guess)
        guessed_characters.append(guess)
        
        
    if check_win_condition(len(missed_characters), mystery) ==1:
        pass
    elif check_win_condition(len(missed_characters), mystery) == 2:
        print("Victory! Good game. You won in " + str(len(guessed_characters)) + " guesses.")
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            start()
        else:
          running = False
          break
    elif check_win_condition(len(missed_characters), mystery) == 3:
        print("Too bad! The word was " + word + ".")
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            start()
        else:
          running = False
          break
