# Without Lambda
# filter() function
def is_even(n):
    return n % 2 == 0
num = [32, 45, 80, 23, 8]
print("Num")
print(num)
evn = list(filter(is_even, num))
print("Even")
print(evn)

# With Lambda
# filter() function
num = [32, 45, 80, 23, 8]
print("Num")
print(num)
evn = list(filter(lambda n: n % 2 == 0, num))
print("Even")
print(evn)
