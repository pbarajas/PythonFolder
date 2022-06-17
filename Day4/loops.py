sum_ = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_ += number

print(sum_)


sum_ = 0
for number in range(2, 101, 2):
    sum_ += number
print(sum_)

