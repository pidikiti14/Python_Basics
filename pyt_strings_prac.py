# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:59:46 2018

@author: Krishna
"""

""" Python strings """

# Learn about unicode characters and others as well 

s = " String can be in single quotes '' , double " " quotes "
print (s.strip())
print (s[0])
print (s[0:24])
print (len(s)) 
print (s.lower())
print (s.upper())
print (s.replace("double", "single")) 
# what if there are more than one string with same letter or name
print (s.split(","))

print ("Enter your name:")
i = input()
x = "Hello "
print (x + i )
