# Example Code

def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3(num1, num2):
  return num1 * num2

outputNum = maths2()
print(outputNum)

# How many functions are there in the code?
  # Answer  7

# How do you know that they are functions, not just subroutines?
  # Answer  They are functions because subroutines have the same name as a function

# Which functions have parameters?  How can you tell?
  # Answer 2 functions have parameters, the first one has 2 parameters, the second one has 1 parameter

# Which functions are called in the code?
  # Answer 2 functions are called in the code, 

# How do you know which lines of code belong to a function or subroutine?
  # Answer  The lines of code that belong to a function or subroutine are tabbed


def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print()

#what will displayed on console
result = add(num1, num2)
print("Addition result:", result)

result = subtract(num1, num2)
print("Subtraction result:", result)

result = multiply(num1, num2)
print("Multiplication result:", result)

result = divide(num1, num2)
print("Division result:", result)