a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if a>b and a>c:
    print("The first number is the greatest:",a)
elif b > a and b > c:
    print("The second number is the greatest:",b)
else:
    print("The third number is the greatest:",c)