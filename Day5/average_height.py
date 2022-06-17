student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    # total = total + int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

final_height = round(total_height / len(student_heights))
print(f"The average height for this group of students is {final_height}cm.")
