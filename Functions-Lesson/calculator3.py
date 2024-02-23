x = float(input("What's x?"))
y = float(input("What's y?"))

z = round(x / y, 2)
# rounds to 2 decimals

print(z)

print(f"{z:.2f}")
#this is the fstring approach to the same problem