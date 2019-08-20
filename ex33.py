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


def while_loop(first_int, last_int):

  numbers = []
  
  while first_int <= last_int:

    print(f"At the top is {first_int}")
    numbers.append(first_int)

    first_int += 1
    print("Numbers now: " , numbers)
    print(f"At the bottom i is {first_int}")

  print("The numbers: ")

  for num in numbers:
    print(num)
  
while_loop(5, 11)