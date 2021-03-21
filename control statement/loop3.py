n=int(input("enter the number"))
avg=0.0
s=0
for i in range(1,n+1):
    s=s+i
avg=s/i
print("the sum of first n natural numbers is:",s)
print("the avg of n  natural number is:",avg)