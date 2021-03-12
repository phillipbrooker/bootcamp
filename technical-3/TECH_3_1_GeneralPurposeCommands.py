"""
Programming with Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 3. 1. GENERAL PURPOSE COMMANDS
"""

#Here are a few 'all-purpose' commands that can be used across lots of
#contexts/objects in Python e.g. lists, tuples, dictionaries, strings, etc).
#However, bear in mind that some of the 'arguments' you feed them might not
#make sense and might produce an error - for instance, what would the absolute
#value of a string be?).

#The arguments passed to the commands below are just examples to demonstrate
#the concepts. You should try out these commands with different types of
#variables and objects in the shell, to get a feel for how they work.

max(1, 2, 3, 4, 5) #gives the maximum value of the argument
min(1, 2, 3, 4, 5) #gives the minimum value of the argument
abs(-1) #gives the absolute value of the argument (i.e. turns negative numbers
        #to positive values) - applies to integers and floats only
type(-50.5) #gives the variable type
len("This is a string.") #gives the length of the argument

#You can also pass other objects to these commands:
var1 = (2, 3, 1, 6, 3, 6, 3, 5)

max(var1)
min(var1)
type(var1)
len(var1)

#There are LOADS more commands native to Python. LOADS. But this is just about
#getting used to the idea that objects have properties that you can call in
#Python. We'll be doing this as we get deeper into lists, dictionaries and
#string formatting/methods.

#EXERCISE: Try typing each of these commands into the shell and see what
#happens - can you understand why you see the output that results?
