# guess = int(input("Guess a number!"))
# print(guess)

def get_guess():
    guess = input("Enter a guess:")
    return guess

# after executing the get guess function, this prints the return value of it

def main():
    guess2 = get_guess()
    print("Your guess:",guess2)

    if guess2 == 50:
        print("Correct!")
    else:
        print("Incorrect")

# guess2 could be named as 'guess', like in the get function because they are in different functions
# I won't use this method in order to be distinguishable if someone is a beginner like me
    
main()

