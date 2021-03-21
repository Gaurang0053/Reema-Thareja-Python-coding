pos=neg=zero=0
print("..........enter -1 to exit........")
while(1):
    n=int(input("enter the number:"))
    if n == -1:
        break
    if n==0:
        zero=zero+1
    elif n>0:
        pos=pos+1
    else:
        neg=neg+1
print("count of positive numbers are:",pos)
print("count of  negative numbers are:",neg)
print("count of zeroes are:",zero)
