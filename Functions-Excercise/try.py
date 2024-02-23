def get_guess():
    guess = input("Enter a guess:")
    return int(guess)

def main():
    for _ in range(1, float('inf')):  # Loop indefinitely until correct guess
        guess = get_guess()
        print("Your guess:", guess)

        if guess == 50:
            print("Correct!")
            break  # Exit the loop if the guess is correct
        else:
            print("Incorrect. Guess again!")

main()