import random
# Functions
# def names_info():
#     name = input('What is your name? ')
#     age = int(input('What is your age? '))
#     phone_number = int(input('Enter your phone number: '))
#     return name, age, phone_number
#
#
# def name_of_function(name):
#     print("Hello " + name)
#
#
# def multiply_function(x, y):
#     return x * y
#
#
# num1 = int(input('Enter digit '))
# num2 = int(input('Enter digit '))
#
# result = multiply_function(num1, num2)
# print(result)

#
# def even_check(number):
#     return number % 2 == 0
#
#
# print(even_check(50))


def checkEvenList(num_list):
    # return all the even numbers in a list
    # placeholder variables
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
            # print('even', number)
            # return True
        # else:
        #     pass
        # print('pass', number)
    return even_numbers


# print(checkEvenList([1, 3, 2]))
even_list = checkEvenList(list(range(1, 101)))
print(even_list)


def checkEvenList(num_list):
    # Go through each number
    even_numbers = []
    for number in num_list:
        # Once we get a 'hit' on an even number, we return True
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# Tuple unpacking with Python functions

stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(ticker)

# Tuple unpacking with Python functions

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


print(employee_check(work_hours))

# result = employee_check(work_hours)
# print(result[0])
# print(result[1])
#
#
# name, hours = employee_check(work_hours)
# print(name)
# print(hours)
#
# name = employee_check(work_hours[0])
# hours = employee_check(work_hours[1])
# print(name)
# print(hours)




# Interactions between Python Functions
# Three Cup Monte
# Our simple game won't actually show the cups or ball, instead we will simply mimic the effect with a Python list
# Our simple version willa also not show the shuffle to the user, so the guess is completely random.

























