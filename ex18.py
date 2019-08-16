# this one is like your scripts with argv
def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we van just do this
def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
  print("I got nothin'.")


print_two("Brian", "Falasz")
print_two_again("Robert", "McInerney")
print_one(11)
print_none()
