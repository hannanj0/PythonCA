# Program that uses if-statements to calculate weight depending on planet

print("I have information for the following planets:\n")

# The planets along with their allocated numbers
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

# Variables created for weight and planet
weight = 185
planet = 3

# If-elif statement to calculate weight depending on planet
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19
else:
    print("Choose planet again.")

# Print statement to determine what weight will be on planet chosen
print("Your weight will be: ", weight)
