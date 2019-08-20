# This is how we set global variables

# i = 0
# numbers = []

# def while_loop(int):
    # Use global before varible to set it globally so we can use it inside of the function
#   global i

#   while i <= int:

#     print(f"At the top is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now: " , numbers)
#     print(f"At the bottom i is {i}")

#   print("The numbers: ")

#   for num in numbers:
#     print(num)
  
# while_loop(11)

# def while_loop(int):
  
#   i = 0
#   numbers = []

#   while i <= int:

#     print(f"At the top is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now: " , numbers)
#     print(f"At the bottom i is {i}")

#   print("The numbers: ")

#   for num in numbers:
#     print(num)
  
# while_loop(11)


# def while_loop(finish_int, increment):

#   i = 0
#   numbers = []
  
#   while i <= finish_int:

#     print(f"At the top is {i}")
#     numbers.append(i)

#     i += increment
#     print("Numbers now: " , numbers)
#     print(f"At the bottom i is {i}")

#   print("The numbers: ")

#   for num in numbers:
#     print(num)
  
# while_loop(30, 2)


def refactored_loop(finish_int, increment):

  i = 0
  numbers = []
  
  for num in range(i, finish_int):
    print(f"At the top is {num}")
    numbers.append(num)

    print("Numbers now: " , numbers)
    print(f"At the bottom i is {num}")

  print("The numbers: ")
  
refactored_loop(30, 2)