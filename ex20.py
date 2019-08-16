# import argv which allows us to pass in argument parameters into the interpreter
# through the sys module
from sys import argv 

# unpacking tuples with argv. So, when I will first run the script and then
# pass in a file as an argument/parameter to the interpreter when running my 
# script
script, input_file = argv 


# defining three seperate functions

# this simply takes the input_file as an argument and reads the whole thing
def print_all(f):
  print(f.read())

# This will take the input_file as an argument and seek the beginning of the file.
# if I were to pass in say 11 into seek method, rewind would start at the eleventh 
# character of the file.
def rewind(f):
  f.seek(0)

# pass in the line number and the file. readline will print each line consecutively 
def print_a_line(line_count, f):
  print(line_count, f.readline())

# pass in the input_file into the open method to get the file.
current_file = open(input_file)

print("First let's print the whole file:\n")

# print all of the contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# use seek to start at the beginning of the file. If you do not do this 
# the print_a_line function will not pass anything into the 2nd argument.
rewind(current_file)

print("Let's print three lines:")

# basically printing each line of the file line by line.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)