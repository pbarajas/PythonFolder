from random import shuffle

# import random

# Interactions between Python Functions
# Three Cup Monte
# Our simple game won't actually show the cups or ball, instead we will simply mimic the effect with a Python list
# Our simple version willa also not show the shuffle to the user, so the guess is completely random.

# Example List
example = list(range(1, 8))


# Shuffle List Function
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)

my_list = [' ', 'O', ' ']


# Player Guess Function
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)


my_index = player_guess()

# Check Guess Function
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess')
        print(mylist)


# Initial List
my_list = [' ', 'O', ' ']
# Shuffle List
mixedup_list = shuffle_list(my_list)

# User Guess
guess = player_guess()
# Check Guess
check_guess(mixedup_list, guess)

# example = list(range(1, 8))


# random.shuffle(example)
# print(example)

#
# def shuffle_list(my_list):
#     random.shuffle(my_list)
#     return my_list
#
#
# result = shuffle_list(example)
# print(result)
