"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 4. 1. FUNCTIONS
"""

#Functions are a core concept of Python. Let's see how they work. Try calling
#myFunction() by typing "myFunction()" in the shell:

def myFunction():
    print("Thanks for printing myFunction()!")

#Now let's build something a little more complex - let's build a function
#that can take numbers that we pass it and check if they're even (and, if
#they're even, store them in a list).

even_numbers = []
def isEven(num):
    if num % 2 == 0:
        even_numbers.append(num)
        return("This number is even. I'll add it to the list.")
    else:
        return("This number is odd.")

#Can you explain in words what this function is doing, line-by-line? Try
#writing it out and "reverse engineering" the function, to better understand
#how it works and what it does.

#Try using isEven(num) with different numbers in place of "num" to see what
#happens. Throw a selection of numbers at this function, then check to see
#what's in the even_numbers list to see if it's working as you'd expect.

"""
EXERCISE:
I'm hungry - will you order me a pizza? Create a function for checking whether
or not I like various ingredients on a pizza, and return the results as a
string. As part of your checking, you should also check to see if the input is
actually a string or not (since I defintely DON'T like integers and floats on
my pizza). I'll give you a few hints:

* It will DEFINITELY help if you plan out your code in advance - what do you
  want this function to do, step-by-step?
* topping_list below contains details of all the ingredients I like.
* You can use "in" as a way to see if something appears within any given list
  (i.e. "if THING in LIST" etc). 
* Think about the various techniques you'll need to use to do all this work -
  you DO know all these already, but may need to review earlier sections to
  refresh your memory.
"""

topping_list = ["cheese", "pepperoni", "sausage", "bacon", "anchovies",
                "salami", "chorizo", "ham", "jalapenos", "pineapple",
                "olives", "tomatoes"]
