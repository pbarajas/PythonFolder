# My solution
year = int(input("Which year do you want to check? "))

if (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a Leap year.")
elif (year % 100 == 0) and (year % 400 == 0):
    print(f"{year} is a Leap year.")
else:
    print(f"{year} not a Leap year.")

# Angela's solution
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")   