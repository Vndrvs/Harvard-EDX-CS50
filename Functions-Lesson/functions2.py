def main():
    name = input("What's your name?")
    hello(name)

def hello(to="world"):
    print("hello", to)
# name does not exist in the scope of the hello function

main()