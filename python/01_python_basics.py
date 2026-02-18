# =========================
# Python 3.10+ Basic Syntax and Data Types
# =========================

# -------------------------
# Variables 
# -------------------------

val = 5
name = "siva"
is_valid = True

# -------------------------
# If Statements 
# -------------------------

if val > 5:
    print("Value is greater than 5")
elif val == 5:
    print("Value is equal to 5")
else:
    print("Value is less than 5")

# -------------------------
# Switch Case (match-case)
# -------------------------

day = "Monday"

match day:
    case "Monday":
        print("Start of the week: ", day)
    case "Friday":
        print("End of the week: ", day)
    case _:
        print("Midweek day: ", day)

# -------------------------
# Loops
# -------------------------

# For loop - Values only 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop - Index and Values
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}") # Evaluate the f-string to print index and fruit
    print(index, fruit) # Print index and fruit without f-string

# For loop - Range
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and Continue
for i in range(10):
    if i == 3:
        print("Skipping i = 3")
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        print("Breaking the loop at i = 7")
        break  # Exit the loop when i is 7
    print(i)

# -------------------------
# Functions 
# -------------------------

def greet(name):
    return f"Hello, {name}!"

print(greet("Siva"))

# -------------------------
# Multiple Return Values
def calculate(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product
result_sum, result_product = calculate(5, 3)
print(f"Sum: {result_sum}, Product: {result_product}")

def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([3, 1, 4, 5, 9])
print(f"Min: {low}, Max: {high}")

