#Python Program 03 - Strings and Loops (ENGR4)

#Written by Cole Lyman

#9.20.2021

#This is the ugliest garbage I've ever written.

#We define word as our input to call later on, replace spaces with - and pre-splitting it.
#Since the split function converts to a list, we can't just append a final - with +"-", it has
#to be + ["-"]; we do this because people normally don't end sentences with spaces and we don't want
#to waste any lines on print("-")
word = input("Enter your word: ").replace(" ", "-").split() + ["-"]

#Next we collapse two for loops into one line. It iterates through the list for as many words
#as there are in the list, and then print each character in that word.
words = [print(b) for i in range(len(word)) for b in word[i]]
