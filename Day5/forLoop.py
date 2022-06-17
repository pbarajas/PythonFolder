# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     # print(fruit)
#     print(f"{fruit} Pie")


number_list = input("Enter a list of numbers: ").split() # Enter numbers to create a list
for number in range(0, len(number_list)): # loops through number list
    number_list[number] = int(number_list[number]) # makes the list int


maxi = number_list[0]
print(f"Maxi {maxi}\n")

for x in number_list:
    if x > maxi:
        print(f"if {x}")
        print(f"Maxi {maxi}")
        print(f"x {x}")
        maxi = x



print(maxi)

# 78 65 89 86 55 91 64 89
