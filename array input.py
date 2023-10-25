# Inserting values in array by user (user defined)
from array import *
a = array('i', [])
b = int(input("Enter the length of the array: "))
for i in range(b):
    c = int(input("Enter Element: "))
    a.append(c)
print(a)
