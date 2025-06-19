# Summary of core Python features

# 1. Variables & Types
name = "Alice"        # str
age = 30              # int
height = 1.70         # float
is_student = True     # bool

# 2. Data Structures
fruits = ["apple", "banana", "cherry"]           # List
grades = {"Math": 90, "English": 85}             # Dictionary
coordinates = (10.0, 20.0)                       # Tuple
unique_ids = {1, 2, 3}                           # Set

# 3. Control Flow
for fruit in fruits:
    if fruit.startswith("a"):
        print(f"Fruit starting with 'a': {fruit}")

# 4. Functions
def greet(person):
    return f"Hello, {person}!"

print(greet(name))

# 5. Classes & OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

p = Person("Bob", 25)
p.birthday()
print(p.age)

# 6. Error Handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 7. File I/O
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# 8. Modules
import math
print(math.sqrt(16))

# 9. List Comprehensions
squares = [x**2 for x in range(5)]

# 10. Lambda & Functional Tools
double = lambda x: x * 2
print(double(4))

# Python is known for: simplicity, readability, dynamic typing, and huge ecosystem.
