# Deep Copy
from numpy import *
a = array([63, 75, 82, 40])
b = a.copy()  # Deep Copy
print("a")
print(a)
print("b")
print(b)
print("ID a")
print(id(a))
print("ID b")
print(id(b))
