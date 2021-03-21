i=0
while i<10:
    print(i ,end=" ")
    i=i+1

print("\n")

i=0
while i<10:
    print(i,end="\t")
    i=i+1

print("\n")

i=0
s=0
while i<10:
    s=s+i
    i=i+1
avg=float(s)/10
print("The sum is:",s)
print("The avg.is:",avg)

print("\n")

i=0
while i<20:
    print("*",end="")
    i=i+1

print("\n")

m=int(input("enter the value of m:"))
n=int(input("enter teh value of n:"))
s=0
while m<=n:
    s=s+m
    m=m+1
print("sum is:",s)
