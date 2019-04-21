#Excercise 5

import random
import csv

#DESKTOP filename = ("C:/Users/Shesan/Desktop/BIF/holmes.txt")
#DESKTOP filename1 = ("C:/Users/Shesan/Desktop/BIF/cockney.csv")
filename1 = ("cockney.csv")
filename2 = ("holmes.txt")

#Revision
#Q1
"""
lines = []
with open (filename) as f:
    for line in f:
        lines += [line.strip()]
randline = random.choice(lines)
print(randline)
print("characters:", len(randline))
"""
#Q2
"""
lines = []
with open (filename) as f:
    for line in f:
        lines += [line.strip()]
randline = random.choice(lines)

while len(randline) == 0:
    randline = random.choice(lines)
    
print(randline)
print("characters:", len(randline))
"""
#Q3
"""
lines = []
with open (filename) as f:
    for line in f:
        lines += [line.strip()]
randline = random.choice(lines)

while len(randline) == 0:
    randline = random.choice(lines)

randword = randline.split()

print(random.choice(randword))
"""

#Dictionaries
#Q1
"""
votes = {}
while True:
    animal = input("What is your fav animal? ")
    if animal == "a":
        break
    if animal in votes.keys():
        votes[animal] += 1
    else:
        votes[animal] = 1
    for animal in votes:
        print(animal, "got", votes[animal], "votes")
"""
#Q2
"""
votes = {"choco": 6, "vanilla":0, "strawberry": 4, "mint": 2}
print(votes["choco"])
for key in votes:
    print(key, "."*(12-len(key)), "|", "#" * votes[key])
"""
#Q3 (CANT GET THE OUTPUT TO DISPLAY PROPERLY)
#"""
words = {}
sen = []
newsen = []
sentence = input("enter a sentence to be converted")
sen = sentence.split()

print(sen)

with open (filename1) as f:
    words = dict(filter(None, csv.reader(f)))
   
for i in range(len(sen)):
    if sen[i] in words.keys():
        newsen = (words[sen[i]])
    else:
        newsen = (sen[i])
    print(newsen)
#"""

#Objects and Classes
#Q1 POKEMON
#To learn about self and _init_
#https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
"""
class PocketMonster:
    def __init__(self, name, health, attack, defence):
       self.name = name
       self.health = health
       self.attack = attack
       self.defence = defence

    def describe(self):
        return self.name, self.health

pika = PocketMonster("Pikachu", 10, 10, 5)
mudkip = PocketMonster("Mudkip", 9, 12, 4)

print(pika.describe(), "vs.", mudkip.describe())
"""
#Q2
"""
class PocketMonster:
    def __init__(self, name, health, attack, defence):
       self.name = name
       self.health = health
       self.attack = attack
       self.defence = defence

    def describe(self):
        return self.name,  self.health
    
    def hit(self, opponent):
        valueatk = random.randint(0, self.attack)
        valuedef = random.randint(0, opponent.defence)
        print("atk", valueatk)
        print("def", valuedef)
        if valueatk >= valuedef:
            opponent.health= opponent.health - (valueatk - valuedef)
            print("Attack Sucessful")
        else: 
            opponent.health= opponent.health
            print("Attack failed :(")
        return opponent.health
    

pika = PocketMonster("Pikachu", 10, 10, 5)
mudkip = PocketMonster("Mudkip", 9, 12, 4)

print (pika.describe(), "vs.", mudkip.describe())
print (pika.name, "( HP =", (pika.health), ") uses attack on", mudkip.name, "( HP =", (pika.hit(mudkip)), ")")
print (mudkip.name, "( HP =", (mudkip.health), ") uses attack on", pika.name, "( HP =", (mudkip.hit(pika)), ")")
"""
#Q3
"""
class PocketMonster:
    def __init__(self, name, health, attack, defence):
       self.name = name
       self.health = health
       self.attack = attack
       self.defence = defence

    def describe(self):
        return self.name,  self.health
    
    def hit(self, opponent):
        valueatk = random.randint(0, self.attack)
        valuedef = random.randint(0, opponent.defence)
        print("atk", valueatk)
        print("def", valuedef)
        if valueatk >= valuedef:
            opponent.health= opponent.health - (valueatk - valuedef)
            print("Attack Sucessful")
        else: 
            opponent.health= opponent.health
            print("Attack failed :(")
        return opponent.health

    def dead(self):
        if self.health < 0.1:
            return False
        else:
            return True
        
#Name, health, attack, defence
pika = PocketMonster("Pikachu", 10, 10, 5)
mudkip = PocketMonster("Mudkip", 9, 12, 4)

print (pika.describe(), "vs.", mudkip.describe())

while pika.dead() and mudkip.dead():
    print (pika.name, "( HP =", (pika.health), ") uses attack on", mudkip.name, "( HP =", (pika.hit(mudkip)), ")")
    print (mudkip.name, "( HP =", (mudkip.health), ") uses attack on", pika.name, "( HP =", (mudkip.hit(pika)), ")")

print("\n")
if pika.health > mudkip.health:
    print("Winner = Pikachu, HP = ", pika.health)
else:
    print("Winner = Mudkip, HP = ", mudkip.health)
"""

#Advanced: Word Clouds
#Q1
"""
words = []
with open(filename2) as f:
    for line in f:
        words += [line.strip()]
newwords = words.strip()
print(newwords)
"""




























