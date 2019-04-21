#Excercise 4
import random
import math
filename = ("Words.txt")

#Revision
#Q1
"""
words = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
randword = random.choice(words)
print(randword)
splitword = list(randword)
print (splitword)
hyphen = "-"
print (hyphen.join(splitword))
"""

#Functions
#Q1
"""
words = []
with open (filename) as f:
    for line in f:
        words = words + [line.strip()]
print(max(words, key=len))
"""
#Q2 (NEED HELP GETTING THE RIGHT FORMULA)
"""
def mean(numbers):
    return sum(numbers)/len(numbers)

def standarddeviation(numbers):
    length = len(numbers)
    m = mean(numbers)
    totalsum = 0
    for i in range(length):
        totalsum += ((numbers[i]-m)**2)
        return math.sqrt(totalsum/(length))

test = [10,2,38,23,38,23,21]
print (standarddeviation(test))
"""
#Q3
"""
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)
m = int(input("numerator: "))
n = int(input("denominator: "))

print("GCD:", gcd(m,n))
"""

#Reading Code
"""
def findPartial(start, end, container):
    store = []
    storing = False
    
    for c in container:
        if c == start:
            storing = True
        if storing:
             store = store + [c]
        if c == end:
             storing = False

    return store

print(findPartial(4, 8, [1, 3, 4, 6, 7, 8, 9]))
print(findPartial(5, 10, range(100)))
print(findPartial("owl", "chicken", ["bear", "ant", "owl", "bee", "chicken"]))
print(findPartial("t", "r", "Python is rad"))
"""

#Advanced: Map and Reduce
#Q1
"""
list = [2,4,6,8]

def square(list):
    return map(lambda x: x**2, list)

def double(list):
    return map(lambda x: x*2, list)

def halve(list):
    return map(lambda x: x/2, list)

def cubes(list):
    return map(lambda x: x**3, list)

print(square(list))
print(double(list))
print(halve(list))
print(cubes(list))
"""
""" (HOW THE EXAMPLE IS DONE, CANT UNDERSTAND HOW TO DO MULTIPLE CALCULATIONS)
def f(x):
    return x**2

def map(f, xs):
    ys = []
    for x in xs:
        ys = ys + [f(x)]
    return ys

print(map(f,xs))
"""
#Q2 (DIDNT DO, NEED HELP)
"""
def reduce(f, xs):
    y = xs[0]
    for i in range(1, len(xs)):
        y = f(y, xs[i])
    return y

def f(x):
    return *=x

xs = [2,4,6,8]
"""





































    
    
        