from art import logo,vs
from game_data import data
import random

def format_data(account):
    """ Takes the account data and returns it into printable format. """
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    """ Takes the user's guess and the follower counts and returns if they got it right. """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Display art.
print(logo)
score = 0

# Make the game repeatable.
# should_continue = True
# while should_continue:


# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# Ask the user for a guess.
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
## Get follower count of each account.
a_follower_count = account_a['follower_count']
b_follower_count = account_b['follower_count']
is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Give user feedback on their guess.
if is_correct:
    score += 1
    print(f"You're right! Current score: {score}\n")
else:
    print(f"You're wrong! Final score: {score}\n")

## Make previous B the next A if user is correct.

# Clear the screen.