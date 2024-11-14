import random

def run_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Loop until valid difficulty is given
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            guesses_remaining = 10
            break
        elif difficulty == "hard":
            guesses_remaining = 5
            break
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")
        
    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)

    # Function to make a guess
    def make_guess():
        while True:
            try:
                guess = int(input("Make a guess: "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("That number was not between 1 and 100, please try again.")
            except ValueError:
                print("Invalid input. Please type an integer.")
    
    # Game loop
    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} guesses remaining.")
        guess = make_guess()

        if guess == answer:
            print(f"You got it! The number was {answer}.")
            return
        elif guess < answer:
            print(f"Your guess is too low.")
        else:
            print(f"Your guess is too high.")

        guesses_remaining -= 1
        if guesses_remaining > 0:
            print(f"Guess again.")
        else:
            print(f"You ran out of guesses. The number was {answer}.")

run_game()