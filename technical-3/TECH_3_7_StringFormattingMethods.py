"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 3. 7. STRING FORMATTING/METHODS
"""

#We already looked a little bit at this:
string1 = "First Bit."
space = " "
string2 = "Second Bit."
print(string1 + space + string2)
#This is called string concatenation.

new_string = "this IS a SliGhtly more ComplicaTed strINg"

new_string[1] #calls the letter at index position one (i.e. the second letter)
new_string[0:4] #calls the first four characters
new_string[5:] #calls everything including and after the fifth character
new_string[::2] #calls all characters in steps of 2 (i.e. every other character)
new_string[-1:-10:-1] #calls the last ten letters in steps of -1 (i.e. reverse)

len(new_string)
string1.lower() #makes it lower case
string1.upper() #makes it upper case
string1.split() #takes each item, puts it in a list as an individual item.
                #TRY THIS. See what happens.

#You can also put strings together via methods other than concatenation:
string4 = "is cool."
string5 = "Programming %s" %string4 #the %s denotes a placeholder for a string.
                                    #this is more useful than it looks.

"""
% STRING FORMATTING OPERATORS:
You can see the %s in line 31 above - that means that Python expects something
to be inserted that is a string type. Here are some other string formatting
symbols you can use:

%s string
%i or %d integer
%f float

So, run the following code and see what happens:
print("Hi, my name is %s and I'm %d years old." %("Phil", 32))

Play around with this way of constructing strings: try passing variables
to the operators, and experiment with the order of the arguments you pass to
the operators.
"""

"""
EXERCISE:
In the shell, can you get Python to produce a print of new_string that is
properly punctuated (i.e. capitals in the right place, full stop at the end)?

Can you then print it out backwards?
"""
