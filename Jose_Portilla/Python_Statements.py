from random import randint

# from random import shuffle
# import random
# loc = 'Bank'
# if loc == 'Auto Shop':
#     print('Cars are cool')
# elif loc == 'Bank':
#     print('Money is cool!')
# else:
#     print('I do not know much')
#
# name = input('What is your name? ')
# if name == 'Pedro':
#     print('Python Developer')
# elif name == 'Tania':
#     print('Executive Admin')
# else:
#     new_name = input('You are not '
#                      'in the list. '
#                      'What is your name? ')
#     role = input('What is your role? ')
#     print(f'{new_name}\n {role}')


# for loops

# myList = list(range(1, 11))
# for i in myList:
#     # Check for even
#     if i % 2 == 0:
#         print(f"Even: {i}")
#     else:
#         print(f"Odd: {i}")

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
print('\n')
for letter in 'abcde':
    print(f"At index {index_count} the letter is {letter}")
print('\n')

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
print('\n')

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

print('\n')

myList1 = list(range(1, 4))
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]
for i in zip(myList1, myList2, myList3):
    print(i)
new_list = list(zip(myList1, myList2, myList3))
print('--', new_list[0][2])
print('\n')

list_ = list(range(1, 11))
# random.shuffle(list_)
# print(list_)
#
# shuffle(list_)
# print(list_)

print(randint(0, 100))
print('\n')

# Practice
# num = ["Hi", 4, 8.99, "apple", ('a','b')]
# for i in enumerate(num):
#     print(i)


# List Comprehension
myList = []
mystring = 'hello'
for letter in mystring:
    myList.append(letter)
print(myList)

mystring = 'hello'
myList = [letter for letter in mystring]
print(myList)

myList = [x for x in 'word']
print(myList)

myList = [num ** 2 for num in range(0, 11)]
print(myList)

myList = [x for x in range(0, 11) if x % 2 == 0]
print(myList)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

celcius = [0, 10, 20, 34.5]
fahrenheit = []

for temp in celcius:
    fahrenheit.append((9 / 5) * temp + 32)
print(fahrenheit)

myList = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        myList.append(x*y)
print(myList)