import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_length = len(names)
name_random = names[random.randint(0, list_length - 1)]

print(f"{name_random} is going to buy the meal today!")


# or

person_will_pay = random.choice(names)
print(f"{person_will_pay} is going to buy the meal today!")



























