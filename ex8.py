formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
# even if I pass in a different number of arguments into the format function
# I still get the first four arguments only and the program doesn't break
print(formatter.format("one", "two", "three", "four", "five"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))

# My guess is that this code is going to take the formaatter variable and plug in the values inside of 
# each respective format method.