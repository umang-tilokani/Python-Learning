# Array
from array import *
a = array('i', [5, 2, 67, 13, 23, 55])
print(a)
print("Address & Size: ", a.buffer_info())
print("Data Type: ", a.typecode)
print("Reverse")
a.reverse()
print(a)
print(a[0])
print(a[2])
