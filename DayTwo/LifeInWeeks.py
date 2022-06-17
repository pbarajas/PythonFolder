# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
my_age = int(age)
days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12
live_until_age = 90


years_remaining = live_until_age - my_age
months_remaining = months_in_a_year * years_remaining
weeks_remaining = weeks_in_a_year * years_remaining
days_remaining = days_in_a_year * years_remaining

total_life_left = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(total_life_left)