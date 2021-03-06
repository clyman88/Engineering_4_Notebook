# Engineering 4 Notebook
Engineering is pretty cool. But, what if there were four of them?

We strive to answer that question here, and document our findings in a neat and orderly fashion.

## About Cole Lyman

What ISN'T there to say about Cole Lyman? A lot!

## Table of Contents

### [Python](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#python-1):

- [Calculator](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#calculator)
- [Quadratic Solver](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#quadratic-solver)
- [Strings and Loops](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#strings-and-loops)
- [Man-Shaped Pinata](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#man-shaped-pinata)

### [CAD](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#cad-1):

- [Swing Arm](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#swing-arm)
- [Skateboard](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#skateboard)
- [Duck!](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#duck)

### [Raspberry Pi](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#raspberry-pi-1):

- [GPIO Pin Intro](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#gpio-pin-intro)
- [Shutdown Button](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#shutdown-button)
- [GPIO - I2C](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#gpio---i2c)
- [Headless Accelerometer](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#headless-accelerometer)
- [Pi Camera](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#pi-camera)
- [Copypasta](https://github.com/clyman88/Engineering_4_Notebook/blob/main/README.md#copypasta)
---

# Python

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

On first glance, the assignment seemed challenging, but after doing some preliminary research and reminding myself what the quadratic formula was again for the umpteenth time in my High School career, it was pretty straightforward. I also am a big fan of making multiple small functions, instead of one or two big functions. I find it easier on the eyes to look at this:

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
Yes, it's an ugly piece of garbage. But it's *my* ugly piece of garbage.

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
pinata = ["---???", "\n   o","\n  /","|", "\\", "\n  /"," \\"]

for i in range(0, (incorrect_guesses + 1)):
   print(pinata[i]) 

```

This surprised me by working correctly! Everything else was relatively straightforward, but there was one other issue that stumped me for a bit:

**Problem:**
If an input was something like "Hello world" (i.e. has more than one word), the output will be:
```python
___________
```

Instead of:
```python
_____ _____
```

This is because I have a function that affects the variable "mystery_word", which is a version of the input that is what the display is. It functions by iterating through each letter in the input, and if the letter has been guessed, it writes out the letter instead of an underscore. However, it counts spaces as letters.

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

And that's that!

---

# CAD

## Swing Arm:

### Assignment Description

This assignment required the creation of a Swing Arm designed from four provided drawings. The mass was then to be determined based off of what variables were used for certain measurements.

### Evidence 

![SwingArm1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Swing1.png)

![SwingArm2](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Swing2.png)

### Part Link

[Swing Arm Link](https://cvilleschools.onshape.com/documents/e4445f3ab6feb2ff96de333b/w/a02469bef9b80549469e5eff/e/1414e574cc4eda8197f87c96)

### Reflection

Getting back into CAD after taking more than a year's worth of a break took a significant amount of adjusting, especially considering that this was my first time using Onshape. Fortunately, as soon as I got started, I found the program to be intuitive and efficient, and completing this assignment (with the help of the walkthrough) was an important first step to getting CAD back into my system. The first time that I changed the dimensions of the A, B, and C variables the entire sketch definitely broke, so fixing that and dissecting the relations between lines was a good challenge to solve.

## Skateboard

### Assignment Description

This assignment required the creation of a skateboard, using the creation of multiple parts and the eventual assembly of those parts.

### Evidence 

![Skateboard_First_Parts](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Skateboard_no_wheels.png)

![Skateboard_Wheel_and_Bearings](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Wheel_bearings.png)

![Full Skateboard](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Skateboard_full.png)

### Part Link

[Skateboard_Assembly_Link](https://cvilleschools.onshape.com/documents/e53223de13228aa3105cf500/w/5b68eba53bef752ac0b97fc0/e/b5fc67f3114f74169da27832)

### Reflection

Cranking on the tunes and having one window on the instructions and the other on my Part Studio was definitely the way to go about this assignment. It reinforced a lot of the fundamentals that I learned in the prior CAD assignment, and understanding how parts are creating together and then independently joined in an assembly was an old concept that was (for me) relearned in this new program. Creating parts relative to others was a new concept that I learned using the "Use" button, and will definitely be something I need to continue to entirely understand and be able to incorporate into my future constructions. My favorite part was making the skateboard colorful. The method of creating the deck was relatively straightforward, but defining all of the other parts required more brainpower and resulted in a lot of switching between tabs. Using the revolution tool was pretty intuitive, and went relatively smoothly, and it got to the point where I would just have to read exactly what the step required (plus dimensions) and I would be able to complete it without going micro-step by micro-step.

## Duck!

### Assignment Description

This assignment required the creation of configurations of different sizes of bricks that would eventually be used to construct a duck.

### Evidence 

![Brick](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Brick.png)

![Duck_Assembly](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Duck_Assembly.png)

![Drawing](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Drawing.png)

### Part Link

[Duck_Assembly_Link](https://cvilleschools.onshape.com/documents/275f311a397b70555b367d23/w/c731c5d5c955a1a3b9d4d4e8/e/e8f8e55053248e8d2a6fb8be)

### Reflection

This project was the most fun CAD assignment that I have done in a long time; something about creating Legos and building them virtually gave me an immense amount of joy. I learned a bunch about configurations, and exploding the duck I made made me equally as happy as building it in the first place. Snapping the studs into place took a little bit of practice at first, but I got the hang of it eventually. I also made a lot of other colors, because the more the merrier. I think it would be interesting to try to configure some slanted bricks...

---

# Raspberry Pi


## GPIO Pin Intro:


### Assignment Description

This assignment required coding LEDs connected to a raspberry pi to flash on and off in sequence, alternating which LED was turned on while the others were turned off. It required use of a T-Cobbler and GPIO pins, making the main point of this assignment to become familiar with using both aforementioned materials.

### Evidence 

![Blinking Lights](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/GPIO-video.gif)

### Wiring

![Blinking Lights_Wiring](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/GPIO-wiring.JPG)

### Reflection

Since this was the introduction of an entirely new concept, the most difficult part was getting accustomed to the syntax of the new code and conceptually understanding what was going on. There have been a few "blinking" assignments in the past, so the structure of designing a piece of code that blinks LEDs one at a time was familiar to me. Incorporation of the GPIO pins is demonstrated here:

```python3

  
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

channel_list = [5, 12, 21]

GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.LOW)

```

## Shutdown Button:


### Assignment Description

This assignment required the creation of a button that would automatically shut down the raspberry pi without having a user manually input a shutdown command.

### Evidence 

![Shutdown Button in action](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/shutdown.MOV)

### Wiring

![Shutdown Button wiring](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/shutdown.JPG)

### Reflection

Right off the bat, here's the code for making a button be able to work:

```python3
import RPi.GPIO as GPIO 

reset_shutdown_pin = 4

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Use built-in internal pullup resistor so the pin is not floating
# if using a momentary push button without a resistor.
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
```

I always find it difficult to work with other people's code, since typically everything makes more sense to the individual who writes it, and this was no exception; working with a piece of code that (in parts) was a bit above my current level of understanding was challenging, to say the least. Luckily, I had to make very little alterations to get it to work. 

The main hardship lied in making this code run in the background without prompting. Putting a line in the bootup code didn't suffice for my machine, oddly enough, so the solution was to make the program a "service", similar to how we accomplished the headless accelerometer in an upcoming assignment.

## GPIO - I2C:


### Assignment Description

For this assignment, we had to display an accelerometer output on a micro-LCD using I2C communication.

### Evidence 

![I2C-Evidence1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/I2C-Evidence1.JPG)
![I2C-Evidence1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/I2C-Evidence2.JPG)

### Wiring

![I2C-Wiring](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/HeadAccel-Wiring.JPG)

### Reflection

Once again, this project was difficult mainly due to getting used to new functions and ways of interacting with new programs and libraries previously unknown to me. Trouble-shooting involved a lot of making small alterations to several lines, testing it, and then sighing in frustration as my changes yielded... no visible change. Eventually, I was able to display accelerometer data on the micro-LCD.

Here's the rather lengthy process for showing text on the screen:

```python3

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width,height))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

while True:

  disp.clear()
  
  draw.rectangle((0,0,width,height), outline=0, fill=0)

  draw.text((2, 2), "Test", font=font, fill=255)

  disp.image(image)

  disp.display()
  
  time.sleep(.2)

```

## Headless Accelerometer:


### Assignment Description

This assignment is an extension of the previous one; we had to make the device battery-operated without relying on computer input, as well as having a graphic displaying accelerometer stats.

### Evidence 

![I2C-Evidence1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/HeadAccel-Evidence.JPG)

### Wiring

![I2C-Evidence1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/HeadAccel-Wiring.JPG)

### Reflection

This assignment was surprisingly easy from a code-based standpoint, as a lot of the foundations created in the last assignment were used again in this project. The only difference was displaying shapes:

```python3

draw.ellipse((x, y, x+15, y+15), outline=255, fill=0)

```

I briefly attempted to make the ellipse displayed (being affected by the acceleration of the unit) act as something for the user to interact with for a game, where they would have to collide with other, smaller ellipses to get points. However, collision code is difficult, so this plan quickly fell through.

## Pi Camera:


### Assignment Description

There were two assignments in one for this project:

1.) Design a program that takes a picture, then prints "Done" when completed.

2.) Design a program that takes five pictures, each with a different effects.

### Evidence 

![Effect1](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pics/effect_1.jpg)
![Effect2](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pics/effect_2.jpg)
![Effect3](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pics/effect_3.jpg)
![Effect4](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pics/effect_4.jpg)
![Effect5](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pics/effect_5.jpg)

### Wiring

![Camera_connecter](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Camera%20(1).JPG)

### Reflection

This assignment was straightforward and enjoyable. Here is new code that is helpful to know in the future:

```python3

import picamera

effects = []
i = c_effect

with picamera.PiCamera() as camera:

    camera.resolution = (1024, 768)
    camera.start_preview()
    
    camera.image_effect = effects[i]
    
    camera.capture('effect_' + str(i+1) + '.jpg')

```

In terms of the creative process for taking thrilling pictures, I thought that my intriguing and mysterious face would be the perfect figurehead; a subject to flaunt its mystique in this magnum opus.

## Copypasta:


### Assignment Description

This assignment required designing a program that would take a picture each time a button was pressed, and creating a stop-motion video using the pictures taken using this program.

### Evidence 

![Epic GIF](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/stopmotion.gif)

### Wiring

![Camera_connecter](https://github.com/clyman88/Engineering_4_Notebook/blob/main/Pictures/Camera%20(1).JPG)

### Reflection

The coding, wiring and photographic process for this was all pretty easy; the one hiccup was actually uploading all 83 (yes, 83) pictures to the github, as well as actually viewing the pictures while taking them (this was difficult mainly because it's impossible). Instead of pushing to the github, I manually inserted my SD into the computer and uploaded from files.

Putting the video together was as simple as putting all of the pictures together in DaVinci Resolve and exporting as a GIF.
