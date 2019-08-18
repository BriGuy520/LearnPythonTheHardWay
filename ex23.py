# importing sys module and instead of extracting argv with import 
# we are attaching argv as a method to the sys module
import sys 
script, input_encoding, error = sys.argv


# defining a function that takes three arguments 
def main(language_file, encoding, errors):
  # using readline mehtod to read each line in the languages.txt file line by line
  line = language_file.readline()

  # if line is not blank. Said another way, if line is True.
  if line: 
    # call the print_line function and pass in current line of languages.txt
    # encode the file into utf-8 and errors 
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
  # take the line and strip any whitespace
  next_lang = line.strip()
  # using encode method to encode the line into utf-8 format and
  # using default parameters to set the third parameter and setting
  # it equal to 'strict' which will raise a unicodeError if there is one.
  raw_bytes = next_lang.encode(encoding, errors=errors)
  # use decode method to turn into utf-8
  cooked_string = raw_bytes.decode(encoding, errors=errors)

  print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)