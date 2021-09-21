from time import sleep

pinata = ["---┐", "\n   o","\n  /","|", "\\", "\n  /"," \\"]
missed_characters = []
guessed_characters = []
words = []
letters = []
mystery = []

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
        
def check(guess, letters, output):
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
    else:
        missed_characters.append(guess)
    
    
word = input("Enter word(s): ")
letters = assign(word, 2, mystery)
mystery = assign(word, 3, mystery)

print(letters)
print(words)
spaces(letters, mystery)

while True:
    print("\n"*50)
    print_pinata(len(missed_characters))
    print("\n")
    print(print_mystery(mystery))
    print("\n")
    print(letters)
    print(mystery)
    guess = input("Guess: ")
    if check(guess, letters, mystery) != False:
        mystery = check(guess, letters, mystery)
    else:
        missed_characters.append(guess)
