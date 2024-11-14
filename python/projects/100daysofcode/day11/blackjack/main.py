############### Blackjack Project #####################
############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

# Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """Draw a card from the deck."""
    return random.choice(cards)

def calculate_score(card_list):
    """Calculates the score from a list of cards."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0 # This is a blackjack
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def play_game():
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_should_deal = input("Type 'y' to hit or 'n' to stand: ").lower()
            if player_should_deal == 'y':
                player_cards.append(draw_card())
            else:
                game_over = True

    # Dealer's turn
    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    # Determine the winner
    if player_score > 21:
        print("You went over. You lose 😭")
    elif dealer_score > 21:
        print("Dealer went over. You win! 😁")
    elif player_score > dealer_score:
        print("You win! 😁")
    elif player_score < dealer_score:
        print("You lose 😭")
    else:
        print("It's a draw. 🤝")

# Start the game
play_game()

