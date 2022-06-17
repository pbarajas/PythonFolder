# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         i = 'FizzBuzz'
#     elif i % 5 == 0:
#         i = 'Buzz'
#     else:
#         if i % 3 == 0:
#             i = 'Fizz'
#     print(i)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    elif i % 5 == 0:
        i = 'Buzz'
    elif i % 3 == 0:
        i = 'Fizz'
    print(i)
