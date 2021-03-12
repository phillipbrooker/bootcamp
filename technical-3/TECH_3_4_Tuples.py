"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 3. 4. TUPLES
"""

#In essence, just lists that are immutable (i.e. once assigned, there are no
#methods for fiddling with them - handy if you want to "write protect" your
#data).

my_tuple = (0, 10, 30)
my_tuple[1] #calls the item at index position 1.

#As with other data structures like lists and dictionaries, you can also build
#tuples from existing values, and these don't have to contain all the same
#types of data:
age = 32
location = "Manchester"
hairstyle = "bald"
energy_level = 0.1

Phil = (age, location, hairstyle, energy_level)

"""
That's about it...you can't do things like pop or remove things from tuples.
They're immutable. But, if you want to take bits from a tuple and play with them
you can always assign them to a variable: my_tuple_extract = my_tuple[1]. And,
some things like len(my_tuple) will work because they don't try to edit the
data (they just describe it as "metadata" - data about data).
"""
