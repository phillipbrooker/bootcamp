"""
Programming with Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 2. 2. FLOW CONTROL (AND WHITESPACE)
"""

#Now we can compare things, we can get into more sophisticated stuff. Here is
#a script that takes a variable ("number") and runs various checks on it. If
#the number is evenly divisible by three (i.e. with no remainder), the code
#prints the string "Fizz". If the number is evenly divisible by five, the code
#prints the string "Buzz". If a number is evenly divisible by both three and
#five, the code prints "FizzBuzz".

number = 44

if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#First, run the script - what happens? Is that expected?

#Second, change the value of the variable "number" in line 15 to the following
#values:
    #3, 98, 75, 55, 45, 29853
#What happens? Is that expected?



#EXERCISE: Create a program which produces statements about numbers that you
#give it, with the following conditions:
    #if the number is over 100 print "Phew, that's a big number."
    #if the number is even, print "This one is even."
    #if the number is even and over 100 print "Stop. I can't even."
    #if the number doesn't satisfy any of these conditions, print the number.
    
#This program can be written in a new script.
#Check the program with a few values to see if it gives the results you expect.
#What do you think would happen if you change the AND to an OR? Try it out!
    
