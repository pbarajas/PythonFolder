def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)


def position_row():
    choice_list = [1, 2, 3]
    while True:
        try:
            choice_row = int(input('Choose a row: 1, 2, or 3 '))
            if choice_row not in choice_list:
                print('Warning! Invalid number')
                break
        except ValueError:
            print('Warning! Characters not allowed!')
            break
        return choice_row


number_row = position_row()


def position_index():
    choice_list = [1, 2, 3]
    while True:
        try:
            choice_index = int(input('Choose an Index: 1, 2, or 3 '))
            if choice_index not in choice_list:
                print('Warning! Invalid number')
                break
        except ValueError:
            print('Warning! Characters not allowed!')
            break
        return choice_index


number_index = position_index()


def main_():
    while True:
        if number_row == 1:
            row1[number_index - 1] = 'X'
            display(row1, row2, row3)
            break
        elif number_row == 2:
            row2[number_index - 1] = 'X'
            display(row1, row2, row3)
            break
        elif number_row == 3:
            row3[number_index - 1] = 'X'
            display(row1, row2, row3)
            break



main_()

#
# def position_row():
#     choice = 'WRONG'
#     while not choice.isdigit():
#         choice = input('Choose a row: 1, 2, or 3 ')
#
#     return int(choice)


while True:

    position_row = int(input('Choose row 1, row 2, or row 3: '))
    position_index = int(input('Choose an index position: '))

    try:
        if position_row not in range(1, 3 + 1) and position_index not in range(1, 3 + 1):
            print('Out of range! Exiting program.')
            break

        elif position_row == 1:
            row1[position_index - 1] = 'X'
            display(row1, row2, row3)
            break

        elif position_row == 2:
            row2[position_index - 1] = 'X'
            display(row1, row2, row3)
            break

        elif position_row == 3:
            row3[position_index - 1] = 'X'
            display(row1, row2, row3)
            break

    except IndexError:
        print('Out of range! Exiting program.')
        break

# print(position_row())

# while choice in range(1, 3+1) == False:
#     choice = int(input('Choose a row: 1, 2, or 3 '))
#
# return choice
