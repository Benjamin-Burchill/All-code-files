# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("fish")
int ("45")
str ("912")
x='blue'
y='green'
z='red'
print (x,y,z)
route=866
print(route,type(route))
len(('one',))
len([1,4,5,6,'pause',2])#[]is essential to stop argument error
x=['blub','catfish','drezden']
x.append('more')
print (x[0]) #notice it counts from 0 here
a=['retpally',3,'none']
b=['retpally',3,'none']
a is b # are the objects the same object (no they are not though content is
 #same)
b=a#once a=b then a is b will yield true not false
a is b
a='many paths'
b='many paths'
a is b#would yield false at this point
a==b # will yield true
a=9
0 <= a <= 10#in the Ipython console this yields true and is exampl of how
# operators may be linked
#'three'<4#this causes a type error
"""
if boolean_expression1:
    suite1
elif boolean_expression2:
    suite2
else:
    else_suite
 basic exception handling
s=input("enter an integer:")#try:
    i=int(s)
    print("valid integer entered:",i)
except ValueError as err:
    print(err)
"""
import pandas
#pandas
#grid.[move]
import time
name = input("What's your name")

age=int(input("how old are u"))
daysperyear = (365)
daysalive=daysperyear*age
time.sleep(1)
print("you are",daysalive,"days old since your birth")
    