# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
import self as self


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print(sleep_in(False, False))  # True
print(sleep_in(True, False))  # False
print(sleep_in(False, True))  # True

print('\n')


# Monkey Trouble


def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    elif a_smile == True and b_smile == False:
        return False
    elif a_smile == False or b_smile == True:
        return False


print(monkey_trouble(True, True))  # True
print(monkey_trouble(False, False))  # True
print(monkey_trouble(True, False))  # False
print(monkey_trouble(False, True))  # False

print('\n')


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


print(monkey_trouble(True, True))  # True
print(monkey_trouble(False, False))  # True
print(monkey_trouble(True, False))  # False
print(monkey_trouble(False, True))  # False
print('\n')


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


print(sum_double(1, 2))  # 3
print(sum_double(3, 2))  # 5
print(sum_double(2, 2))  # 8
print('\n')


def sum_double(a, b):
    sum = a + b

    if a == b:
        sum = sum * 2
    return sum


print(sum_double(1, 2))  # 3
print(sum_double(3, 2))  # 5
print(sum_double(2, 2))  # 8

# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

# 21 - n
# def diff21(n):
#     if n > 21:
#         return (21 - n) * -2
#     else:
#         if n <= 21:
#             return 21 - n

# print('\n')
# print(diff21(19)) # 2
# print(diff21(10)) # 11
# print(diff21(21)) # 0
# print(diff21(22)) # 2
print('\n')


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (21 - n) * -2


print(diff21(19))  # 2
print(diff21(10))  # 11
print(diff21(21))  # 0
print(diff21(22))  # 2


# First Solution
def diff21(n):
    if n > 21:
        return (21 - n) * -2
    else:
        return 21 - n

print('\n')
print(diff21(19))  # 2
print(diff21(10))  # 11
print(diff21(21))  # 0
print(diff21(22))  # 2
print('\n')


# My Solution
def parrot_trouble(talking, hour):
    # 0..23
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        if not talking or talking:
            return False

print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 7)) # False
print(parrot_trouble(False,6 )) # False
print(parrot_trouble(False,21)) # False
print(parrot_trouble(False,23)) # False
print('\n')




def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 7)) # False
print(parrot_trouble(False,6 )) # False
print(parrot_trouble(False,21)) # False
print(parrot_trouble(False,23)) # False








# Computer Solution
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +
print('\n')


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

# My Solution
def makes10(a, b):
    if a + b == 10:
        return True
    elif a == 10 or b == 10:
        return True
    else:
        return False


print(makes10(9, 10)) # True
print(makes10(9, 9)) # False
print(makes10(1, 9)) # True

#
# # Codingbat solution
# def makes10(a, b):
#   return (a == 10 or b == 10 or a+b == 10)



# Given an int n, return True if it is within 10 of 100 or 200. Note:
# abs(num) computes the absolute value of a number.

# def near_hundred(n):



print(abs(89- 20))

