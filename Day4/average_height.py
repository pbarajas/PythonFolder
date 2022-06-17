student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initializing sum
sum_ = 0
# Initializing counter
counter = 0
for student in student_heights:
    # Adding students to sum
    sum_ += student
    # incrementing counter
    counter += 1


average_height = round(sum_/counter)
print(average_height)


