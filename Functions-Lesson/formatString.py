name = input("what's your name?")

name = name.strip()
#remove whitespace from str

# name = name.capitalize()
#capitalize user's name (one word)

# name = name.title()
#capitalize user's name

name = name.strip().title()
#both functions return values and copy them into the name variable

print(f"Hello, {name}")
#f marks the special string