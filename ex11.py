print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print(f"So, you're {age} years old, {height} inches tall, and weigh {weight} pounds.")

# These will do the same thing and concat the values together
print(f"{age + height + weight}")
print(height + age + weight)