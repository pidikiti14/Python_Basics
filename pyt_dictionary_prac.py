# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 08:42:16 2018

@author: Krishna
"""

""" Python Collections - Dictionary """

""" Unordered, changeble and indexed """

firstdic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
print (firstdic)

#Access the dic

accdic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }

x = accdic["brand"]
print (x)

y = accdic.get("model")
print (y)

# Prints all key names
for z in accdic:
    print (z)
    
#print all values
    
for w in accdic:
    print (accdic[w])
    
#Alternate way to print - values()

for a in accdic.values():
    print(a)
    
# loop through both keys and values
for b, c in accdic.items():
    print (b, c)
    
#check if key exist or not 
    
if "brand" in accdic:
    print ("Yes, 'brand' is one of the key in accdic")
else:
    print ("Don't know what brand it is")
    
# Change the values
    
chandic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
chandic["year"] = 1999
print (chandic)

# Len of dic

lendic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
print (len(lendic))

# adding an item to dic


adddic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
adddic["version"] = "SX"
print (adddic)

# , "ver_num" , 2.0 

# How to add multiple items to dic ???

# Remove items
# pop() removes specific item mentioned in the dict
# How to remove multiple items at a time ???
# If not specified any value it will throw an error

popdic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
popdic.pop("brand")
print (popdic)


# popitem() - removes the last item in the dict
popitdic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
popitdic.popitem()
print (popitdic)

deldic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
del deldic["brand"]
print (deldic)

# If not given any item del will delete entire dictionary and give an error when you print

"""
trydeldic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
del trydeldic
print (trydeldic)
"""

# Clear - will clear entire dic

clrdic = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2018
        }
clrdic.clear()
print (clrdic)


# Using dict constructor
# Keywords are not string literals 
# equal is used in place of colon

newdic = dict(brand = "Ford", model = "escape", year = 2018)
print (newdic)
