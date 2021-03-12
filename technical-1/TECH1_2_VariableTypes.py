"""
Programming with Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 1. 2. DATA TYPES
"""

#an integer is a "whole number" (i.e. one with no decimal point)
my_integer = 12

#a float is a numerical value with a decimal point
my_float = 12.1

#a string is text
my_string = "This is my string."

#You can check the data type of variables using the "type" method
type(my_string)

"""
QUESTION 1: What type of variables do you think the following five are? DON'T use
type() until you've had a guess.
"""

var1 = "14"

var2 = 14 + 14

var3 = 14 + 14.2

var4 = "14 + 14.2"

var5 = 14.2 - 0.2

#There are WAY more variable types than these - integers, floats and strings
#are the three data types Python uses, but variables don't have to be used to
#store just data types - they can store all sorts of more complex data
#structures (i.e. things that collect bits of data together) like lists or
#dictionaries. But that's for later!

my_list = [var1, var2, var3, var4, var5]
my_dict = {"First Variable": var1, "Second Variable": var2, "Third Variable": var3, "Fourth Variable": var4, "Fifth Variable": var5}

"""
QUESTION 2: What do you think you will see if you use type() on my_list and
my_dict? Have a guess and see if you're right.
"""
