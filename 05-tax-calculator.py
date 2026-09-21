# Take inputs from the user for age and income

age = int(input("Enter your age in Years: "))
income = float(input("Enter the income: "))

if age >  60:
    print("Tax Slab information not available")
    exit(0)

if income > 4_00_000 and income <= 8_00_000:
    tax = (5/100) * income
elif income > 8_00_000 and income <= 12_00_000:
    tax = 20_000 + (income - 8_00_000) * (10/100)
elif income > 12_00_000 and income <= 16_00_000:
    tax = 60_000 + (income - 12_00_000) * (15/100)
# Other Slabs to be implemented
else:
    print(f"The tax amount is NIL for income of Rs. {income}")
    exit(0)

print(f"The tax amount is {tax} for income of Rs. {income}")