"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 3. 5. DICTIONARIES AND DICTIONARY METHODS
"""

#Dictionaries are just as important as lists, but we're not going to go over the
#same things here - a lot of what we did with lists was about using commands
#to find our way around objects, and those same sort of ideas apply here; we
#don't need to go over them in the same depth. However, dictionaries are
#different objects than lists, which means they do have some unique
#attributes/methods that we do need to outline.

#The main difference: lists sort things by index position, but with dictionaries
#you can create your own names/labels for index positions. So, it's a different
#way of structuring data that may be more applicable for some tasks.

animal_dict = {"dog": "woof",
               "bird": "tweet",
               "cow": "moo",
               "pig": "oink",
               "turtle": "?"}

animal_dict["fish"] = "glub" #adds a new entry
del animal_dict["fish"] #removes an entry
animal_dict["bird"] = "squawk" #edits an entry
print(animal_dict["dog"]) #prints the value of the key
animal_dict.items() #breaks up dict into items, prints them #METADATA
animal_dict.keys() #prints keys
animal_dict.values() #prints values

"""
NOTE:
A lot of the methods we learned about with lists will work with dictionaries
too. Things like .pop() and len() we learned about, but given there are
so many more methods we can't cover, you'll find more overlaps the more you
look into it and try things out for yourself.
"""

"""
OTHER NOTE:
You can embed lists within dictionaries, dictionaries with dictionaries,
dictionaries within lists, tuples within dictionaries within lists within lists,
etc...complex data structures and hierarchies! Below, you can see an example of
how to put a dictionary within another dictionary, and how to pull information
out of it - this applies also to lists (except for lists, you will be using
numerical index positions rather than string keys).
"""
dict1 = {"first thing": 1, "second thing": 2, "third thing": 3}
dict2 = {"dict_within_dict": dict1}
#Now let's pull the value for "second thing" out of dict1, using dictionary
#methods to work with dict2:
dict2["dict_within_dict"]["second thing"]
