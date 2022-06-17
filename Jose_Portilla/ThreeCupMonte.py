from random import shuffle


# Shuffle List Function
def shuffle_list(list_items):
    shuffle(list_items)
    return list_items


# Player Guess Function
def player_guess():
    # Local Variable
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)


# Check Guess Function
def check_guess(x_list, guess):
    if x_list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess')
        print(x_list)


# Initial List
# Global Variable
my_list = [' ', 'O', ' ']

# Shuffle List
mixed_up_list = shuffle_list(my_list)
print('mixed List', mixed_up_list)

# User Guess
guess = player_guess()
print('guess', guess)

# Check Guess
check_guess(mixed_up_list, guess)
