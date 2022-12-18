# A program that uses python dictionaries, zipping and altering entries along with adding new entries

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Zip the two lists songs and playcounts
zipped_plays = zip(songs, playcounts)

# Using dict comprehension
plays = {song: playcount for [song, playcount] in zipped_plays}

# Adding a new entry to plays
plays["Respect"] = 94

# Changing an entry that already exists in plays
plays["Purple Haze"] = 1

# Creating a dictionary called library, consisting of value plays and empty value
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# Printing library to the console
print(library)
