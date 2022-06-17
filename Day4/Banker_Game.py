import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split()

names_list_length = len(names)
random_name = names[random.randint(0, names_list_length - 1)]
print(f"{random_name} is going to buy the meal today!")


# random.choice()
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")
