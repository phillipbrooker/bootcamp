"""
Programming in Python for Social Science
Phillip Brooker & Mark Carrigan

TECHNICAL 3. 2. LISTS AND LIST METHODS
"""
#Here is a simple list:
animals = ["dog", "cat", "bat"]
#Call animals in the shell. Why does it look like that? HINT: look at all the
#commands below that Python is enacting when we run this script - lines 15
#through 27 (and lines 57 nd 58) are performing tasks which are altering the
#original animals list.

#Here is a selection of list methods, with which you can play around with lists:
animals[2] #Calls the value at index position 2.
animals[0] #Calls the first entry in the list (because zero-indexing)
animals[-1] #Calls the last entry in the list
animals[2] = "rat" #replaces "bat" with "rat" (because zero-indexing)
animals.append("ibex") #appends "ibex" to the end of the list.
animals.sort() #sorts the list alphabetically (or numerically if integer/float)
animals.index("cat") #tells you what index position an item is at
animals.insert(1, "llama") #inserts "llama" into index position 1. Everything
                           #after that gets knocked on 1 place.
animals.pop(3) #removes the item at the denoted index and 'returns' it
del(animals[3]) #removes the item at the denoted index but doesn't return it
animals.remove("dog") #removes the item if it finds it
animals[0:1:1] #calls all the info at index positions from 0 to 1 (not including
               #1), in steps of 1. NOTE: if you don't set the step (i.e.
               #animals[0:1]) Python assumes you mean in steps of 1.

"""
NOTE: There's a difference between round and square brackets here. Round
brackets are what Python uses to accept an 'argument'
(i.e. animals.index("cat") needs the argument "cat" so it knows what index to
produce for you). Sometimes no argument is necessary - e.g. you don't need to
tell Python any extra information for animals.sort(), it just sorts the list.
Square brackets on the other hand are to do with index positions.
"""

#You can also have lists within lists:
mammals = ["dog", "cat", "bat"]
birds = ["parrot", "budgie", "eagle"]
reptiles = ["chameleon", "komodo dragon", "gecko"]
fish = ["sturgeon", "marlin", "shark"]
planet_earth =[mammals, birds, reptiles, fish]

#QUESTION: What do you think the following commands will return? Guess first,
#then type them out in the shell to verify.
planet_earth[1]
planet_earth[3]
planet_earth[1][1]
planet_earth[0][2]

#Each of these results can be stored - they're objects in and of themselves.
#So let's store an index position as a variable, then use that variable to do
#something with a list.
cat_index = animals.index("cat")
animals.insert(cat_index, "cobra")
#Can you see what we did in these two lines? We assigned the index position
#number of "cat" to a variable cat_index, then we used that variable as an
#argument in animals.insert() (which requires an index position, which we give
#by cat_index rather than by number, and a thing to insert, which we gave as
#the string "cobra").
