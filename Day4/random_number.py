import random

# randint(a,b)
# Python Module
#
random_integer = random.randint(1, 10)
print(random_integer)

# Random Float
random_float = round(random.uniform(0, 5),3)
print(random_float)

random_float = random.random() * 5
print(random_float)

# Quick Example | Love generator
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")