# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:14:27 2018

@author: Krishna
"""

""" Python Collections - Tuples """

""" ordered, unchangeble, indexed and allows duplicates """ 

firsttuple = ("Apple", "Banana", "Mango")
print (firsttuple)

# access tuples based on index number
print (firsttuple[1])

#Tuples are unchangeble

changetuple = ("Apple", "Banana", "Mango")
#changetuple[1] = "Orange"
# it will not change

print (changetuple)

# Loop tuple

looptuple = ("Apple", "Banana", "Mango")
for x in looptuple:
    print (x)
    
    
#If loop in tuple
    
existtuple = ("Apple", "Banana", "Mango")
if "Apple" in existtuple:
    # If you give tuple name in print it will not print anything
    #print(existtuple)
    #Casing of values is important
    print ("Yes, 'apple' is in the tuple")
    
    
lentuple = ("Apple", "Banana", "Mango")
print (len(lentuple))

"""

#Cannot add tuples once they are created
addtuple = ("Apple", "Banana", "Mango")
addtuple[3] = "Orange"
print (addtuple)

"""

#Remove items from tuple
#Cannot remove tuples from the list but can delete them

deltuples = ("Apple", "Banana", "Mango")
del deltuples
# print should throw an error as it does not exist
#print (deltuples)

# another way of doing tuple

anothertup = tuple(("Apple", "Banana", "Mango"))
print (anothertup)


# count the values in tuple

counttuple = ("Apple", "Banana", "Mango", "Apple")
x = counttuple.count("Apple")
print(x)
y = counttuple.index("Apple")
print (y)