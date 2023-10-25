# Searching
from array import *
a = array('i', [])
b = int(input("Enter the length of the array: "))
for i in range(b):
    c = int(input("Enter Element: "))
    a.append(c)
print(a)
d = int(input("Enter the value to be searched: "))
e = 0
for f in a:
    if f == d:
        print(e)
        break
    e+=1
