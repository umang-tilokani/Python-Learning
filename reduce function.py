# reduce() function
# without using lambda
from functools import reduce
def add_all(a, b):
    return a + b
num = [32, 74, 89, 53, 27, 94]
print("Num")
print(num)
sum = reduce(add_all, num)
print("Sum")
print(sum)

# using lambda
from functools import reduce
num = [32, 74, 89, 53, 27, 94]
print("Num")
print(num)
sum = reduce(lambda a, b: a + b, num)
print("Sum")
print(sum)
