height = float(input("enter your height in m: "))  # 1.75)
weight = float(input("enter your weight in kg: "))  # 230 lb = 104)

BMI_formula = round(weight / (height * height))
print(BMI_formula)

if BMI_formula < 18.5:
    print(f"Your BMI is {BMI_formula}, you are underweight.")
elif 18.5 < BMI_formula < 25:
    print(f"Your BMI is {BMI_formula}, you are normal weight.")
elif 25 < BMI_formula < 30:
    print(f"Your BMI is {BMI_formula}, you are slightly overweight.")
elif 30 < BMI_formula < 35:
    print(f"Your BMI is {BMI_formula}, you are obese")
else:
    print(f"Your BMI is {BMI_formula}, you are clinically obese.")


# # Angelas Solution
# height = float(input("enter your height in m: "))  # 1.75)
# weight = float(input("enter your weight in kg: "))  # 230 lb = 104)
#
# BMI_formula = round(weight / (height * height))
# print(BMI_formula)
# # 12 <= age <= 18:
#
# if BMI_formula < 18.5:
#     print(f"Your BMI is {BMI_formula}, you are underweight.")
# elif BMI_formula < 25:
#     print(f"Your BMI is {BMI_formula}, you are normal weight.")
# elif BMI_formula < 30:
#     print(f"Your BMI is {BMI_formula}, you are slightly overweight.")
# elif BMI_formula < 35:
#     print(f"Your BMI is {BMI_formula}, you are obese")
# else:
#     print(f"Your BMI is {BMI_formula}, you are clinically obese.")