# This program creates receipts for customers along with their descriptions

# Description for loveseat using multi-line string
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Sets price to a double for loveseat
lovely_loveseat_price = 254.00

# Description for settee using multi-line string
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

# Sets price to a double for settee
stylish_settee_price = 180.50

# Description for lamp using multi-line string
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

# Sets price to a double for lamp
luxurious_lamp_price = 52.15

# Sales tax at 8.8%
sales_tax = .088

# Defines variable for total setting it to 0
customer_one_total = 0

# Empty string where descriptions will go
customer_one_itemisation = " "

# Adds the contents of loveseat to total, along with the description
customer_one_total += lovely_loveseat_price
customer_one_itemisation += lovely_loveseat_description

# Adds the contents of lamp to total, along with the description
customer_one_total += luxurious_lamp_price
customer_one_itemisation += luxurious_lamp_description

# Calculates tax based on customer purchase(s)
customer_one_tax = customer_one_total * sales_tax

# Adds the calculated tax to the total
customer_one_total += customer_one_tax

# Prints the description of items bought
print("Customer One Items:")
print(customer_one_itemisation)


# Prints the customer total, which also includes tax, rounded to 2 decimal places
print("Customer One Total:")
print(round(customer_one_total, 2))
