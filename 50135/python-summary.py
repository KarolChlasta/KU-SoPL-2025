# Python Summary by Franciszek Ksionek (50135)

# Paradigm:
# Object-Oriented, Imperative, Functional

# Syntax Example:
print("Hello, world!")

# Features:
# - Easy to read and write
# - Interpreted language
# - Dynamically typed
# - Large community and libraries
# - Used for web development, data science, scripting, machine learning, scraping 

# Example: Variable and function
name = "Franek"
def greet(user):
    return "Hello, " + user + "!"

print(greet(name))

# Mini Game: Guess a number between 1 and 21
import random

secret = random.randint(1, 21)
guess = 10  # pretend this is a user guess

print("Secret number is:", secret)
print("Karol guessed:", guess)

if guess == secret:
    print("Correct! You win!")
else:
    print("Wrong guess. Try again!")