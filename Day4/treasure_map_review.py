# My Solution
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[1])-1
column = int(position[0])-1

map[row][column] = 'X'
print(f"{row1}\n{row2}\n{row3}")

# Angela's Solution
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
