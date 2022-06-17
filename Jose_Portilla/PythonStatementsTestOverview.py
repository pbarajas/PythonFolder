# Statements Assessment Test

# Use for,.split and if to create a Statement that will print out words that start with 's'
# Method 1
st = 'print only the words that start with s in this sentence'
empty_list = []
for s_word in st.split():
    if s_word.startswith('s'):
        empty_list.append(s_word)
print(empty_list)
print('\n')

# Method 2
for s_word in st.split():
    if s_word.startswith('s'):
        print(s_word, '', end='')
print('\n')

# Method 3
# List Comprehension
empty_list = [s_word for s_word in st.split() if s_word.startswith('s')]
print(empty_list)
print('\n')

# Method 4
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10
for num in range(0, 11):
    if num % 2 == 0:
        print(f"Even {num}")

# List Comprehension
# Creates a list of even numbers
even_num = [num for num in range(0, 11) if num % 2 == 0]
print(even_num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

# for loop Solution
for num in range(1, 51):
    if num % 3 == 0:
        print(num)

# List Comprehension
divisible_by_three = [num for num in range(1, 51) if num % 3 == 0]
print(divisible_by_three)
print('\n')

# Go through the string below and if the length of a word is even print 'even!'
# for loop solution
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(f"{len(word)} {word} --> Even!")

print('\n')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz', num)
    elif num % 3 == 0:
        print('Fizz', num)
    elif num % 5 == 0:
        print('Buzz', num)
    else:
        print(num)

print('\n')
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
for letter in list(st.split()):
    print(letter[0])



first_letter = [letter[0] for letter in st.split()]
print(first_letter)