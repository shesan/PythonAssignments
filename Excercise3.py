#Excercise 3

#Revision
#Q1
#read the line count, words, and characters

"""
filename = ("C:/Users/Shesan/Desktop/BIF/Words.txt")
lines = 0
nchars = 0
words = 0

with open (filename) as f:
    for line in f:
        lines += 1
        nchars += len(line)
        words += len(line.split())
        
print("Lines", lines)
print("Chars", nchars)
print ("Words", words)
"""

filename = ("Words.txt")
import random
#Reading text files
#Q1
"""
words = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]

print("first:", words[0])
print("Last:", words[-1])
"""
#Q2
"""
words = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
print(random.choice(words))
"""
#Q3
"""
words = []
vowels = ("a","e","i","o","u")
curseword = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
randword = random.choice(words)
for eachLetter in randword:
        if eachLetter in ['a','e','i','o','u']:
                randword = randword.replace(eachLetter, '*')
print (randword)
"""
#Q4
"""
letter = input("Type the first letter of a word:")
print("Words starting with", '"' + letter + '"')
words = []
with open (filename) as f:
    for line in f:
        if line[0] == letter:
           print(line)
"""

#Games
#Q1
"""
print("I have thought of a number between 0 and 100")
number = random.randint(0,100)
print(number)
guess = int(input("Guess:"))
while guess != number:
    if guess > number:
        print("Too high")
        guess = int(input("Guess:"))
    elif guess < number:
        print("Too low")
        guess = int(input("Guess:"))
    else:
        break
if guess == number:
    print("Correct!")
"""
#Q2
"""
words = []
vowels = ("a","e","i","o","u")
curseword = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
randword = random.choice(words)
uncensored = randword
for eachLetter in randword:
        if eachLetter in ['a','e','i','o','u']:
                randword = randword.replace(eachLetter, '*')

print("Censored:", randword)
guessedword = input("guess the word:")
while guessedword != uncensored:
    if guessedword != uncensored:
        print("try again")
        guessedword = input("guess the word:")
    else:
        break
print("correct!")
"""

#Reading
"""
dicerolls = []
for i in range(100):
    dicerolls = dicerolls + [random.randint(1, 6)]
counts = [0, 0, 0, 0, 0, 0]
for d in dicerolls:
    counts[d-1] = counts[d-1] + 1
print(counts)
"""

#Advanced
#Hangman (NEED HELP)
"""
words = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
randword = random.choice(words)
censored = len(randword) * "*"
storage = ""
guess_word = []


print("Word:", censored)
print("Guessed:", '[' + storage + ']')
guess = input("Guess a letter:")

while "*" in censored:
    storage.append(guess)
    if guess in randword:
        for f in range (0, len(randword)):
            if randword[f] == guess:
                guess_word[f] = guess
                print (guess_word)
    else:
        break
"""
"""
for letters in randword:
   if letters in guessed:
         print (letters)
        guessed = input("Guess a letter:")
     else:
     print("_")    
guessed = input("Guess a letter:")
"""

#Advanced
#Estimating Pi Using Monte Carlo Methods
"""
radius = 1 unit
length = 2 units
1)  Circle 
    A = pi*r^2
    A = pi*(1)^2
    A = pi
    A = 3.14159
2) Square
    A = L^2
    A = (2)^2
    A = 4
3) probabily = pi/4 = 78.53%
4) if a random x and y cordinate is calculated, we know if it lies within the circle by checking if both the values are below 1. AKA. the area of the circle.
    - ALT
    circle probability could be calculated using a^2 + b^2 = c^2
5) the close the estimated calculations are to our predicted question 3 anwsers, the closer we get to the pi value. 


from math import sqrt

inside=0
n=1000000
for i in range(0,n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if sqrt(x**2 + y**2)<=1:
        inside+=1
pi=4*inside/n
print (pi)
"""


    












































