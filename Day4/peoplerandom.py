import random

names = ["Pedro", "Tania", "Charlie"]  # list
names_len = len(names)  # finding the length of the list
game = names[random.randint(0, names_len - 1)]
print(game)

person_will_pay = random.choice(names)
print(person_will_pay)
