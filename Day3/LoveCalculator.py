print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name1 = name1.lower()
name2 = input("What is their name? \n")
name2 = name2.lower()

T = name1.count("t")
R = name1.count("r")
U = name1.count("u")
E = name1.count("e")
trueTotalOne = T + R + U + E

L = name1.count("l")
O = name1.count("o")
V = name1.count("v")
E = name1.count("e")
loveTotalOne = L + O + V + E
totalNameOne = str(trueTotalOne) + str(loveTotalOne)

T = name2.count("t")
R = name2.count("r")
U = name2.count("u")
E = name2.count("e")
trueTotalTwo = T + R + U + E

L = name2.count("l")
O = name2.count("o")
V = name2.count("v")
E = name2.count("e")
loveTotalTwo = L + O + V + E
totalNameTwo = str(trueTotalTwo) + str(loveTotalTwo)

total = int(totalNameOne) + int(totalNameTwo)

if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
