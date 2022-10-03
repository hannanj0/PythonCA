# A program that edits pizzas and their prices using list and the functions/methods to edit these

# Creates a list of toppings
toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]

# Creates a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Counts how many times 2 has occurred
num_two_dollar_slices = prices.count(2)

# Prints the amount of 2 in prices
print(num_two_dollar_slices)

# Gets the length of the list toppings
num_pizzas = len(toppings)

# Prints how many pizzas that can be sold
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Creates a 2D list storing the price and the pizza
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [
    3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sorts the list in terms of increasing price
pizza_and_prices.sort()

# Prints the 2D list
print(pizza_and_prices)

# Allocates the first item in the list as the cheapest
cheapest_pizza = pizza_and_prices[0]

# Prints the cheapest pizza
print(cheapest_pizza)

# Allocates the last item in the list as the priciest
priciest_pizza = pizza_and_prices[-1]

# Prints the priciest pizza
print(priciest_pizza)

# Removes the last pizza from the list
pizza_and_prices.pop(-1)

# Prints the list again
print(pizza_and_prices)

# Inserts a new item in the 2D list at index 4
pizza_and_prices.insert(4, [2.5, "sausage"])

# Prints the list again
print(pizza_and_prices)

# Allocates the 3 cheapest pizzas into a variable
three_cheapest = pizza_and_prices[:3]

# Prints the 3 cheapest pizzas
print(three_cheapest)
