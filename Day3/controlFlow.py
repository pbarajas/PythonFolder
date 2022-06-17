print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 18:
        print("Child tickets are $ 5")
    elif 12 <= age <= 18:
        print("Youth tickets $7")
    elif (age >= 45) and (age <= 50):
        print("You can ride for free!")
    else:
        bill = 12
        print("Adult tickets are $12")

    photo = input("Do you want a photo? Y or N ").upper()
    if photo == "Y":
        photo_charge = 3
        bill += photo_charge
    print(f"Your total bill is {bill}")
else:
    print("You can't ride")




# # Angela's solution
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")