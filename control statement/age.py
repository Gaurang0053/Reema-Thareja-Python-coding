age=int(input("enter the person's age:"))
if age>18:
    print(age,":he is eligible to vote")
else:
    yrs=18-age
    print("no,he is nt eligible")
    print("But became eligible in",yrs,"years")