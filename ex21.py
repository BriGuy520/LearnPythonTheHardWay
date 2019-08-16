def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 3)
height = subtract(59, 10)
weight = multiply(5, 30)
iq = divide(190, 10)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

