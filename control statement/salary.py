gender=str(input("enter the gender(m or f):"))
salary=int(input("enter the salary:"))
if gender=="m":
    bonus=0.05*salary
if gender=="f":
    bonus=0.10*salary
amt=salary+bonus
print("the salary is:",salary)
print("the bonus is",bonus)
print("**************************")
print("the amount  to be paid:",amt)
print("**************************")
