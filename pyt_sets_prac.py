# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:03:26 2018

@author: Krishna
"""

""" Python Collections - Sets """

""" Sets are unordered, items in sets are unchangeble, unindexedand no duplicates """

# Create a set

firstset = {"Apple", "Banana", "Mango"}
print (firstset)

dupset = {"Apple", "Banana", "Mango", "Apple", "Banana"}
print (dupset)
print (len(dupset))

# for loop for set

forset = {"Apple", "Banana", "Mango"}
for x in forset:
    print (x)
    
# check if value exist in the set
    
iflist = {"Apple", "Banana", "Mango"}
if "Apple" in iflist:
    print ("Yes, 'Apple' is in the list")
else:
    print ("You gave the wrong value")
    
# Change items - items in sets are unchangebvle but you can add items to it
    
addset = {"Apple", "Banana", "Mango"}
addset.add("Orange")
print (addset)

# add multiple items at a time

updset = {"Apple", "Banana", "Mango"}
# update should be in square brackets or it will take each alphabet as an item
# ex: updset.update("Orange", "Grapes")
updset.update(["Orange", "Grapes"])
print (updset)


# length of set

lenset = {1 , 2 , 3}
print (len(lenset))

# Remove Item - can remove items but cannot change
# Note: if item does not exist it will throw an error

remset = {1, 2, 3, 4}
remset.remove(4)
print (remset)

# discard will not throw an error if the item does not exist
disset = {1, 2, 3, 4, 5}
disset.discard(6)
print (disset)
    
#pop method can be used to discard the item in the set but it removes the last item

popset = {1, 2, 3, 4, 5}
x = popset.pop()
# sets are unordere so you will not know which items get removed
print (popset)

# Assigning variable for pop is not mandatory - Alternate way
altpopset = {1, 2, 3, 4, 5}
altpopset.pop()
print (altpopset)


#delete the set

"""
delset = {1, 2}
del delset
# this gives an error when you print
print (delset)
"""
#set constructor
# double round brackets
altset = set((1, 3, 5))
print (altset)