income=float(input("enter the income:"))
tax_income=income-150000
if tax_income<150000:
    print("no tax")
elif tax_income>150001 and tax_income<300000:
    tax=(tax_income-150001)*0.10

elif tax_income > 300001 and tax_income<500000:
    tax = (tax_income-300001) * 0.20

else:
    tax = income* 0.30
print("Tax:", tax)


