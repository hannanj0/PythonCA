import random

# This program is based on the Magic 8-Ball, using the random function to generate the random statement

# Assigns a name to variable name
name = "Hannan"

# Provides a question that will be answered
question = "Is Ronaldo better than Messi?"

# Answer set to empty string
answer = ""

# Generates random number 1 to 10 inclusive
random_number = random.randint(1, 10)

# If-elif statements for all the possible answers
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "This is not possible."
else:
    answer = "Error"

# Checks to see if a name was inputted or not and prints something depending on whether the name was given or not
if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)

# If there is no question, the Magic 8-Ball will not provide a fortune
if question == "":
    print("You need to type in a question otherwise the Magic 8-Ball cannot provide a fortune!")
else:
    print("Magic 8-Ball's answer: " + answer)
