# if-else-if (nested if-else)
# WAP to input three numbers and print the largest among them.
a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))
if a>b:
    if a>c:
        print(a," is the largest among",a,",",b,"&",c)
    else:
        print(c, " is the largest among", a, ",", b, "&", c)
else:
    if b>c:
        print(b, " is the largest among", a, ",", b, "&", c)
    else:
        print(c, " is the largest among", a, ",", b, "&", c)