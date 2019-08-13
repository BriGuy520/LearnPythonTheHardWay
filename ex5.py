convert_to_kilograms = 0.4535924
convert_to_centimeters = 2.54 

name = 'Brian E. Falasz'
age = 29 # not a lie
height = 67 # inches 
weight = 155 # pounds
eyes = 'Brown'
teeth = 'Somewhat White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not heavy at all.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


print(f"His height in centimeters is {height * convert_to_centimeters} and his weight in kilograms is {weight * convert_to_kilograms}")