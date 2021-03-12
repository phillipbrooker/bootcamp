"""
Programming with Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 1. 4. PLAYING AROUND WITH VARIABLES
"""

#Variables can be reassigned and overwritten:
#Can you guess the value of new_var?
original_var = 30
new_var = original_var + 20

#Can you guess the value of original_var2?
original_var2 = 10
original_var2 = original_var2 + 10

#Can you guess what string1 will contain?
string1 = "This is the first part of the string."
#Notice the space at the beginning of the reassigned string1 below: why is that
#there?
string1 = string1 + " This is the second part of the string."

#Try adding these two variables together, and explain what happens.
first_bit = 14
second_bit = "14"

"""
We can also convert variable types to different variable types, as follows.
In the shell, try assigning values to variables that you assign, and convert
them using these commands:
"""
#To 'stringify' something, we can use str(VARIABLE). Below, I'll declare a
#variable which is an integer, then I'll use str(VARIABLE) to write the
#'stringified' version to a new variable.
my_integer_variable = 30
my_stringified_variable = str(my_integer_variable)

#To 'integerify' something, we can use int(VARIABLE). Below, I'll declare a
#variable which is a number written out as a string, then I'll use
#int(VARIABLE) to write the 'integerified' version to a new variable.
my_string_variable = "30"
my_integerified_variable = int(my_string_variable)

#To 'floatify' an integer, we can use float(VARIABLE). Below, I'll declare an
#integer variable, then I'll use float(VARIABLE) to write the 'floatified'
#version to a new variable. Try this for yourself in the shell.
my_integer_variable = 30
my_floatified_variable = float(my_integer_variable)

#NOTE: one way to convert an integer to a float is to just add 0.0 to it, as
#you can see below. Try this out in the shell:
my_integer_variable = 30
my_floatified_variable = my_integer_variable + 0.0
type(my_floatified_variable)
#Because a float is just an integer with a decimal (i.e. 'floating') point, all
#we have to do to 'floatify' an integer is give it a decimal, even if that
#decimal has no numerical value. However, can you see a problem with this?
#What if you want to 'floatify' a string by adding 0.0 to it? It makes no sense
#to add a decimal point to a string in this way, and that will cause an error.
#Try this in the shell: >>> my_string_variable = "30" + 0.0
#Now try this: >>> float(my_string_variable)
#Hence, using float(VARIABLE) is a better way to handle variable type
#conversions as a general rule.

