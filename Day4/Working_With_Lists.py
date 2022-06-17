pizzas = ['pepperoni', 'combo', 'barbecue chicken']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza.\n")

animals = ['dog', 'wolfe', 'coyote']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# Using the range()
for value in range(6):
    print(value)

# Using range() to make a List of Numbers

numbers = list(range(1, 6))
print(numbers, '\n')

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# for x in even_numbers:
#     if x % 2 == 0:
#         print(x)
print('\n')

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7]
print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')

# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Try It Yourself
counting_to_twenty = [value for value in range(1, 21)]
print(counting_to_twenty)

listS = list(range(1, 21))
for value in listS:
    print(value)

one_million = list(range(1, 1000))
print(one_million)
print(min(one_million))
print(max(one_million))
print(sum(one_million))
# for y in one_million:
#     print(y)

odd_numbers = list(range(1, 21, 3))
for i in odd_numbers:
    print(i)

odd_numbers = [value for value in range(1, 21, 3)]
print(odd_numbers)

threes = [value * 3 for value in range(3, 31)]
print(threes)

cubes = [value ** 3 for value in range(1, 11)]
print('cubes',cubes)

cubes = list(range(1, 11))
for value in cubes:
    cube = value**3
    print(cube)
