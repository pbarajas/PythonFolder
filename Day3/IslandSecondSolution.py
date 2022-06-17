import PizzaOrder

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()

if left_or_right == "right":
    print("Fall into a hole. Game Over.")
elif left_or_right == "left":
    swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait"'
                         ' to wait for a boat. Type "swim" to swim across. ').lower()
    if swim_or_wait == "swim":
        print("Attacked by trout. Game Over.")
    elif swim_or_wait == "wait":
        which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red,"
                           " one yellow and one blue. Which colour do you choose? ").lower()
        if which_door == "red":
            print("Burned by fire. Game Over.")
        elif which_door == "blue":
            print("Eaten by beasts. Game Over.")
        elif which_door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over!")
else:
    print("Game Over!")

print(PizzaOrder)

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# left_or_right = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()
#
# if left_or_right == "right":
#     print("Fall into a hole. Game Over.")
# elif left_or_right == "left":
#     swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait"'
#                          ' to wait for a boat. Type "swim" to swim across. ').lower()
# else:
#     print("Game Over")
#
# if swim_or_wait == "swim":
#     print("Attacked by trout. Game Over.")
# elif swim_or_wait == "wait":
#     which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red,"
#                        " one yellow and one blue. Which colour do you choose? ").lower()
# else:
#     print("Game Over")


