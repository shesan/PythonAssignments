#Excercise 2

#Revision
#Q1
"""
num1 = int(input("First number:"))
num2 = int(input("Second number:"))
print(num1, "/", num2, "=", int(num1/num2), "remainder", (num1%num2))
"""
#Q2
"""
num1 = int(input("First number:"))
num2 = int(input("Second number:"))
integer = int(num1/num2)
remain = num1%num2
print(num1, "/", num2, "=", integer, "remainder", remain)
checkval = integer*num2
checktot = checkval+remain
print("Check:")
print(integer, "*", num2, "=", checkval)
print(checkval, "+", remain, "=", checktot)
"""

#Input and lists
#Q1, Word counter
"""
string = str(input("enter a string:"))
words = len(string.split())
print("Words:", words)
"""
#Q2
"""
val = (input("enter numbers (seperated by commas):"))
strings = val.split(",")
int_array = [int(s) for s in strings]
print(sum(int_array))
"""

#Accumulator
#Q1
"""
value = 0
array = list()
while True:
    number = int(input())
    array.append(number)
    value = value + number
    print(array, value)
"""
#Q2 (NEED HELP************************************ cant get the plus sign to display properly)
"""
value = 0
array = list()
while True:
    number = int(input())
    array.append(number)
    value = value + number
    print(array, value)
"""

#Word Count
#Q1
"""
count = 0
while True:
    string = str(input())
    count = count + 1
    words = len(string.split())
    length = len(string)
    print("Line:", count, "Words:", words, "Characters:", length)
    if str(input()) == "break":
        break
        
"""

#Reading Code
#Q1

    
    
    










