import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


while True:
    try:
        ask_user = int(input('What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: '))
        # User choice
        rock_paper_scissors_user = [rock, paper, scissors]
        user_choice = rock_paper_scissors_user[ask_user]
        break
    except IndexError:
        print("Oops!  That was no valid number.  Try again...")

# Computer Random Choice
rock_paper_scissors_computer = [rock, paper, scissors]
computer_random_choice = random.choice(rock_paper_scissors_computer)

if user_choice == rock and computer_random_choice == scissors:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_random_choice}")
    print("User Wins")
elif user_choice == scissors and computer_random_choice == paper:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_random_choice}")
    print("User Wins")
elif user_choice == paper and computer_random_choice == rock:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_random_choice}")
    print("User Wins")
elif user_choice == computer_random_choice:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_random_choice}")
    print("Draw!")
else:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_random_choice}")
    print("Computer Wins")
