"""
Programming with Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 2. 1. COMPARING THINGS
"""

#It often helps for us to be able to compare things in Python, to see if a
#variable matches some criteria that we establish, etc (see other word doc
#on social science applications for more detail). This becomes especially
#powerful when we combine it with things like IF, ELIF and ELSE statements
#(which we will do later), but for now, here are a list of ways in which
#we can compare things in Python. I have declared three variables below -
#try typing the comparisons I've listed into the Python shell and see what
#happens.

a = 2
b = 3
c = 4

a == b #The double-equals signifies an "is the same as" comparison.
a != b #This signifies a "not the same as" comparison

b > a #"is greater than"
b >= a #"is greater than or equal to"

b < a #"is less than"
b <= a #"is less than or equal to"

c % a #This is called the "modulo", which effectively means the remainder.
      #So here, the value that will be given when you type this into the Python
      #shell will be the remainder that is left over when c is divided by a. The
      #modulo is more of a calculation than a comparator, but it's mainly
      #only relevant to us as a way of comparing things.


#QUESTION: You can also do calculations within comparisons. Can you guess what
#will result in the following cases? Have a guess, then type them into the
#Python shell to check.

a+1 == b

c-1 >= b

c/4 > a

a*2 == c

c % a == 0
