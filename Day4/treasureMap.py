row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_list =[int(x) for x in position]
position_ = map[position_list[0] - 1][position_list[1] - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")



