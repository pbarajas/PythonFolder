dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

# append | add item to the end of the list
dirty_dozen.append("Takis")
print(dirty_dozen)

# extend | create a list and add it to the end of your list
dirty_dozen.extend(["tacos", "burritos", "cesadillas"])
print(dirty_dozen)

# insert | Insert an item at a given position
dirty_dozen.insert(0, "Avocados")
print(dirty_dozen)

# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
dirty_dozen.remove("Avocados")
print(dirty_dozen)

# You replaced the first item with "Jalapeno"
dirty_dozen[0] = "Jalapeno"
print(dirty_dozen)

# Remove any item you want | Remove the item at the given position in the list
dirty_dozen.pop(1)
print(dirty_dozen)

# Remove all items from the list
# dirty_dozen.clear()
# print(dirty_dozen)

# index function
index = dirty_dozen.index("Kale")
print('The index of kale is: ', index)

# count function | Return the number of times x appears in the list
x = dirty_dozen.count("Kale")
print(x)

# The sort() method sorts the elements of a given list in a specific ascending or descending order.
dirty_dozen.sort()
print(dirty_dozen)

# reverse function | you reverse the items in a list
dirty_dozen.reverse()
print(dirty_dozen)
# copy function | you can copy a list and add it to a different variable 
x = dirty_dozen.copy()
print(f"X: {x}")