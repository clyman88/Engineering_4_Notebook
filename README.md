# Engineering 4 Notebook
Engineering is pretty cool. But, what if there were four of them?

We strive to answer that question here, and document our findings in a neat and orderly fashion.

## Table of Contents

- [Calculator](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#calculator)
- [Quadratic Solver](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#quadratic-solver)
- [Strings and Loops](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#strings-and-loops)
- [Man-Shaped Pinata]

## About Cole Lyman

What ISN'T there to say about Cole Lyman? A lot!

---

## Calculator

### Assignment Description

For the calculator assignment, the goal was to create a program that, when given two numbers, would output various mathematical functions between the two numbers. The required functions were a sum, difference, product, quotient, and modulo. The spicy version also required each number's factorial.

### Evidence 

![Calculator Output Screenshot](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Screenshot%202021-09-30%209.57.02%20AM.png)

### Wiring

N/A

### Reflection

At first, making all of the different mathematical operations fall into the same function and have that function return different outputs caught me off guard; however, after figuring out that passing a third argument that controls what operation is returned, the task was relatively straightforward.

```python
def calc(a,b,c):
    
    #sum
    if c==0:
        return(a+b)
        
    #difference
    elif c==1:
        return(a-b)
        
print("Sum: " + calc(x, y, 0))

print("Difference: " + calc(x, y, 1))

```
I also wasn't a fan of having massive print() statements taking up multiple lines, so I made it a bit more paletteable:

```python
spice = ["Sum: ", "Difference: ", "Product: ", "Quotient: ", "Modulo: ", "First Factorial: ", "Second Factorial: "]

for i in range(0,7):
    sleep(.5)
    print(spice[i] + str(calc(num1,num2,i)))
```

This would have each output be on different lines, but without having each print statement take up a line.

## Quadratic Solver

### Assignment Description

This assignment required a program that would calculate both the number of roots of a given quadratic and the actual roots themselves. The system then prompts the user to either exit the program or input more roots.

### Evidence 

![Quadratic Output Screenshot](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Screenshot%202021-09-30%2010.29.08%20AM.png)

### Wiring

N/A

### Reflection

"What the hell is a discriminant again?", my mind asks itself, vigorously rifling through crusty memories of freshman year Algebra 2 class. Luckily for it, Google is a thing.

On first glance, the assignment seemed challenging, but doing some preliminary research and reminding myself what the quadratic formula was again for the umpteenth time in my High School career, it was pretty straightforward. I also am a big fan of making multiple small functions, instead of one or two big functions. I find it easier on the eyes to look at this:

```python
def get_input(num):
    ans = input("Please enter coefficient " + prompt[num])
    return(int(ans))

def get_discriminant(a, b, c):
    return((b**2) - (4*a*c))

def get_roots(a, b, c, root_list):
    root_list.append((-b + sqrt(get_discriminant(a,b,c)))/(2*a))
    root_list.append((-b - sqrt(get_discriminant(a,b,c)))/(2*a))
    return(root_list) #returning the list so we can print it later
```

Instead of this:

```python
def find_roots(num, a, b, c, root list):
    for i in range(3):
        ans = input("Please enter coefficient " + prompt[num])
        if i == 1:
            a = ans
        if i == 2:
            b = ans
        if i == 3:
            c = ans
    root_list.append((-b + sqrt(((b**2) - (4*a*c)))/(2*a))
    root_list.append((-b - sqrt(((b**2) - (4*a*c)))/(2*a))
    return(root_list)
```

## Strings and Loops

### Assignment Description

The assignment was to create a program that would accept an input, and then output each letter of the string one-by-one, with words being separated by "-".

For example:

```python
Input: "Hello world"

Output:

H
e
l
l
o
-
w
o
r
l
d
-
```

### Evidence 

![Strings and Loops Demonstration](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Screenshot%202021-10-05%209.33.58%20AM.png)

### Wiring

N/A

### Reflection

This was a fun one. The spicy version of this assignment was to condense the program as much as possible. The bar was 4 lines. Here's my code:

```python
word = input("Enter your word: ").replace(" ", "-").split() + ["-"]

words = [print(b) for i in range(len(word)) for b in word[i]]
```
Yes, it's the ugliest piece of garbage. But it's *my* ugly piece of garbage.

The big thing for Future Cole Lyman to remember is **list comprehensions**, which is how this code is so condensed.

Here's a link, Future Cole Lyman: [List Comprehensions](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)


## Man-Shaped Pinata

### Assignment Description

This assignment required a program to written that would function as a game as hangman, where one user inputs a word and a second user must guess the word, letter by letter. 

```python
_____ _____
```

Each time a letter that is guessed is included in the first user's secret word, the location of that letter is revealed.

```python
_ello _orl_
```

Each time a letter that is guessed is **not** included in the secret word, a stick-figure starts to form under a pole.
```python
-----
    O
   /|\
   /
```

If the word is guessed, the second user wins. If the Man-Shaped Pinata is fully drawn, the first user wins.

### Evidence 

![MSP1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/P1.png)
![MSP2](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/P2.png)

![MSP3](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/P3.png)
![MSP4](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/P4.png)

### Wiring

N/A

### Reflection

Right off the bat, figuring out how to print out a MSP limb-by-limb was a bit of a head scratcher, but I eventually settled on this solution:

```python

incorrect_guesses = 0
pinata = ["---┐", "\n   o","\n  /","|", "\\", "\n  /"," \\"]

for i in range(0, (incorrect_guesses + 1)):
   print(pinata[i]) 

```

This surprised me by working correctly! Everything else was relatively straightforward, but here are some things that initially gave me pause (and my solutions to them):

**Problem:**
If an input was something like "Hello world" (i.e. has more than one word), the output will be:
```python
___________
```

Instead of:
```python
_____ _____
```
**Solution:**
Before the second user even has the opportunity to guess, the program will manually run through the guessing function with " " as the input. If the input has more than one word, it will automatically substitute the underscore for the space, as that "letter" has been "guessed". All of this was put into a function which was then called whenever the user first inputs a sentence:

```python
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

def spaces(letters, mystery):
    if check_if_correct(" ", letters, mystery) != False:
        mystery = check_if_correct(" ", letters, mystery)
        
```

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!
