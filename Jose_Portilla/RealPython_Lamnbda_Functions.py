import dis

# How to Use Python Lambda Functions
# Syntax of Lambda Function in python
# lambda arguments: expression
# Lambda functions can have any number of arguments but only one expression.
# The expression is evaluated and returned. Lambda functions can be used wherever
# function objects are required.


def identity(x):
    return x


# EXAMPLE 1
# lambda
identity_ = (lambda x: x + 1)(2)
# (lambda x: x + 1)(2) = lambda 2: 2 + 1
#                      = 2 + 1
#                      = 3
print(identity_)

# EXAMPLE 2
add_one = lambda x: x + 1
print(add_one(2))


# The above lambda function is equivalent to writing this:
def add_one(x):
    return x + 1


# EXAMPLE 3
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'


# print(full_name(input('First Name: '),input('Last Name: ')))


def full_name(first, last):
    return f'Full name: {first.title()} {last.title()}'


def enter_names():
    return full_name(input('First Name: '), input('Last Name: '))


# print(enter_names())


# EXAMPLE 4
add = lambda x, y: x + y
print(type(add))

dis.dis(add)
print(add)


def add(x, y):
    return x + y


print(type(add))
dis.dis(add)
print(add)

# Single Expression
odd_or_even = (lambda x: x % 2 and 'odd' or 'even')(3)


# def odd_or_even(x):
#     if x % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
#
# print(odd_or_even(2))

# Decorators
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

print(decorated_function('Pyhton'))
print('\n')

#EXAMPLE
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, Kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))

print(list(map(trace(lambda x: x*2), range(3))))
print('\n')

# CLOSURE
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")



























