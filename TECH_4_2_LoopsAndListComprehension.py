"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 4. 2. LOOPS AND LIST COMPREHENSION
"""

#So far, when we've been working with conditional logic and functions, we've
#had to pass arguments around "manually" (i.e. by typing commands in the
#shell). This is a little tedious and time-consuming. Wouldn't it be great if
#we could automate the process? This is the kind of thing we can do with loops.

#The below code is a "Fizzbuzz" script. You may have played "Fizzbuzz" in
#school, but if not, the rules are as follows: go through the numbers 1 to 100,
#and say them out loud. For every number that divides evenly (i.e. no
#remainder) by 3 say "Fizz", for every number that divides evenly by 5 say
#"Buzz" and for every number that divides by both 5 and 3 say "Fizzbuzz".
#"Uncomment" the code (i.e. get rid of the speech marks), run the script,
#and see what happens.

"""
for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
"""

#Can you see what the for loop does here? It iterates through a range of numbers
#from 1 to 101 (the last number in the range is not included), and calls each
#one "number" for the purposes of the logic that follows. Then, it moves to
#the next "number" and repeats until we've gone through all the numbers in the
#range we've set.

#Another way to do this is with a "While Loop", which can iterate a job for as
#long as a certain condition is satisfied. NOTE: when using while loops we have
#to also build in a way to CHANGE whether or not the condition is satisfied.
#Below I do this by building in "number = number + 1" to the loop. Can you see
#what sort of problem might arise if my "while" condition was "while 1 == 1:"?
#Try it! Uncomment this code, run it, see what happens, then make some tweaks
#to play around and explore how the while loop operates.

"""
number = 0
while number <= 99:
    number = number + 1
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
"""

#An added extra of for loops is the idea that we can use conditional logic and
#loops WITHIN lists, to create NEW lists based on objects that we can iterate
#through (i.e. strings, tuples, or even other lists). This is called "list
#comprehension", and it works as follows:

iterable_object = "A string is an example of an iterable object."
new_list = [item for item in iterable_object]

#In the above code, the "new_list" variable will be where the new list is
#stored. Then we tell Python that we're creating a list by using square
#brackets. Then the first "item" refers to the thing that we want to put
#in the list. "for item in iterable_object" means that for each item in
#the object we want to iterate through, we will call that item and drop
#it in "new_list". Try calling new_list to see what it contains.

#We can also use conditional logic within list comprehensions, as follows:

animal_list = ["dog", "owl", "fox", "snake", "mouse", "squirrel", "fish"]
animals_w_legs = [animal for animal in animal_list
                  if animal != "snake" and animal != "fish"]
