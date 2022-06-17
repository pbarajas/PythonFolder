# First solution
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
each_person_tip_total = (total_bill / people) * tip_percentage
each_person_tip_total_round = "{:.2f}".format(each_person_tip_total)
total_bill_plus_tip = (total_bill / people) + float(each_person_tip_total_round)
total = "{:.2f}".format(total_bill_plus_tip)

print(f"Each person should pay: ${total}")

# My second solution

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
each_person_tip_total = (total_bill / people) * tip_percentage
total_bill_plus_tip = "{:.2f}".format((total_bill / people) + each_person_tip_total)

print(f"Each person should pay: ${total_bill_plus_tip}")

# Angela's solution

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
