# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:19:46 2018

@author: Krishna
"""

""" Python Collections - List """

""" Ordered, changeble, indexed and allows duplicates """

firstlist = ['Apple', 'banana', 'Mango']

print (firstlist)

# Allows duplicates

duplist = ['Apple', 'banana', 'Mango', 'Apple']
print (duplist)

# to get the first value/data from the list
# Note: 0 gives you the first value always

print(firstlist[0])

# change the value

changelist = ['Apple', 'banana', 'Mango']
changelist[1] = 'Apple'

print (changelist)


# use for loop to print entire list one by one

for x in changelist:
     print (x)


if 'Mango' in changelist:
    print ("Yes, 'Mango' is in the fruits list")
    
#Alternative    
y = 'Mango'
if y in changelist:
    print ("Yes, 'Mango' is in the fruits list")

#to know the length of the list
    
print (len(changelist))

#Addlist

addlist = ["Apple", "Banana", "Mango", 1]
print (addlist)

# append will add at the end of the list
addlist.append(2)
print (addlist)

addlist.append("Banana")
print (addlist)

# insert - will insert a record in the required position
addlist.insert(1, 3)
print (addlist)

addlist[1] = "Orange"
print (addlist)

#Remove Item
#Only removes value/item in the first position

addlist.remove("Banana")
print (addlist)

# removes specified index and if not specified removes last value
addlist.pop()
print (addlist)

addlist.pop(4)
print (addlist)

# deletes specified index
del addlist[3]
print (addlist)

# deletes complete list if not specified the index
del addlist
#print (addlist)

changelist.clear()
print (changelist)


#Another way of creating list

athlist = list((1, 2, 3))
print (athlist)