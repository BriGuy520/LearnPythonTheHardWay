# sys - This module provides access to some variables used or maintained by the interpreter and to functions 
# that interact strongly with the interpreter. It is always available.

# argv allows you to take in a list of arguments into your python script

# import argv from sys module
from sys import argv

# declare variable names for the script, should always be the first argument and any other additional
# arguments you want to pass into the script. In this case we are declaring a variable named filename
# which will take a txt file as the argument.
script, filename = argv

# opening the file passed into the script and opening it with the open function and storing it 
# to a variable named txt.
txt = open(filename)

# printing the name of the file on line 19 and reading the content of the file on line 20 using the read function.
print(f"Here's your file {filename}")
print(txt.read())

# gathering input from user to open and read another file. The file doesn't have to be the same one passed into the script 
# when loaded.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())