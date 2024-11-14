# Imports
import random
from art import logo, vs
from game_data import data as game_data

# Function to get a random entity from the dictionary
def get_random_entity(exclude = None):
    entity = random.choice(game_data)
    while entity == exclude:
        entity = random.choice(game_data)
    return entity

# Run game function
def run_game():
    # Initalizing score and getting options using rand function created above
    score = 0
    option_a = get_random_entity()
    option_b = get_random_entity(exclude=option_a)

    game_continue = True

    while game_continue:
        print(logo)
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

        guess = input(f"Who has more followers? Type 'A' or 'B': ").upper()
        correct_answer = 'A' if option_a['follower_count'] > option_b['follower_count'] else 'B'

        if guess == correct_answer:
            score += 1 
            print(f"You're right! Current score: {score}.\n")
            # Make B the new A if guess was correct. Otherwise keep A and Change B.
            option_a = option_b if guess == 'B' else option_a
            option_b = get_random_entity(exclude=option_a)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False

run_game()