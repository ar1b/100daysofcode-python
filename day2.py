from typing import final


print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would like to give? "))
people = float(input("How many people to split the bill? "))

tip_decimal = tip_percent / 100
final_amount = (total_bill * tip_decimal) + total_bill
individual = round((final_amount / people), 2)

print(f"Each person should pay {individual}")