# Watch out, this code is not part of the course task list and is rather dumb.

def get_guess():
    guess = input("Enter a guess:")
    return int(guess)

def main():
    while True:  # Indefinite loop
        guess = get_guess()
        print("Your guess:", guess)

        if guess == 50:
            print("Correct!")
            break  # Exit the loop if the guess is correct
        else:
            print("Incorrect. Guess again!")

main() 

# It simply asks for a guess and re-loops infinitely until the user enters the specific int we want