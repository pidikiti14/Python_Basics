# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:00:23 2018

@author: Krishna
"""


""" Python Operators """

# Arthimetic operators

g=3
h=4
print (g+h)
print (g-h)
print (g*h)
print(g/h) 
print(g%h) #Modulus - refresh your memory
print(g**h) #exponential
print(g//h) #Floor divison - look for what ios it is
# what to do when we have multiple print operator in same file and if there is an input field before that

# Assignment Operators

x = 4
x += 4
x -= 5
x *= 4
x /= 4
x %= 1.3
#x //= 1
x **=3

print(x)


#Comparision operators

y = 3
z = 2

print(y==z)
print(y!=z)
print(y>z)
print(y<z)
print(y<=z)
print(y>=z)


#Logical Operators

w = 5
print (w<6 and w>10)
print (w<6 or w>10)
print (not(w<6 or w>10))


#Python Identity Operators

a = ["apple", "banana"]
b = ["apple", "banana"]
c = a
print (c is a)
print (c is not a)
print (a is b) #output is false but in case if variable is int then it returns true


d = ["apple", "banana"]
e = "banana"
f = 'Corona'
#print (x in y) #when the data types are different it will not work
print (e in d)
print (f not in d)

g = 32
g &= 5
print (g)

o = 29
o |= 3
print (o)
