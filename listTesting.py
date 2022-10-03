# A program that uses methods/functions on lists using an example

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table",
             "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Checks the length of list
inventory_len = len(inventory)

# Allocates first item to first variable
first = inventory[0]

# Allocates last item to last variable
last = inventory[-1]

# Slices list starting at 2 and up to but not including 6
inventory_2_6 = inventory[2:6]

# Selects the first 3 items of inventory
first_3 = inventory[:3]

# Checks to see how many occurrences twin bed had
twin_beds = inventory.count("twin bed")

# Removes the 5th element of the list
removed_item = inventory.pop(4)

# Inserts a new item as the 11th element in the list
inventory.insert(10, "19th Century Bed Frame")

# Sorts the list into alphabetical order
inventory.sort()

# Prints inventory list
print(inventory)
