import random

# All possible card values in a deck. Face cards (J, Q, K) are worth 10; Ace is worth 11.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dictionary mapping each possible game outcome to its result message.
results = {
    "user_blackjack": "BLACKJACK. You win!",
    "user_bust": "BUST. You lose.",
    "dealer_blackjack": "BLACKJACK. The dealer wins!",
    "dealer_bust": "BUST. The dealer loses. You win!",
    "user_21": "You win!",
    "dealer_21": "The dealer wins!",
    "user_wins": "You win!",
    "dealer_wins": "The dealer wins!",
    "draw": "It's a draw!"
}

def pick_random_cards(list_of_cards):
    """Pick a random card from the deck."""
    chosen_card = random.choice(list_of_cards)
    return chosen_card

def sum_cards(list_of_cards):
    """Return the total value of a hand."""
    return sum(list_of_cards)

def adjust_for_ace(list_of_cards):
    """Convert Ace from 11 to 1 if the hand total exceeds 21."""
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return list_of_cards

def show_results(dict_of_results, user_score, dealer_score, list_of_user_cards, list_of_dealer_cards):
    """Determine and return the result message based on both players' final scores."""
    if dealer_score == 21 and len(list_of_dealer_cards) == 2:
        return dict_of_results["dealer_blackjack"]
    elif user_score == 21 and len(list_of_user_cards) == 2:
        return dict_of_results["user_blackjack"]
    elif user_score == 21:
        return dict_of_results["user_21"]
    elif dealer_score == 21:
        return dict_of_results["dealer_21"]
    elif user_score > 21:
        return dict_of_results["user_bust"]
    elif dealer_score > 21:
        return dict_of_results["dealer_bust"]
    elif user_score == dealer_score:
        return dict_of_results["draw"]
    elif user_score > dealer_score:
        return dict_of_results["user_wins"]
    else:
        return dict_of_results["dealer_wins"]

def play_blackjack():
    """Control the logic of a single Blackjack round."""

    # Deal two cards to both the user and the dealer.
    user_cards = []
    dealer_cards = []

    for card in range(2):
        user_cards.append(pick_random_cards(cards))
        dealer_cards.append(pick_random_cards(cards))

    user_total_score = sum_cards(user_cards)
    dealer_total_score = sum_cards(dealer_cards)

    # Show the user their cards and the dealer's first card (the second remains hidden).
    print(f"Your cards: {user_cards}. Current score {user_total_score}")
    print(f"The dealer's first card: {dealer_cards[0]}")

    # If the user's first two cards total 21, it's an immediate Blackjack — the round ends.
    if user_total_score == 21 and len(user_cards) == 2:
        print(show_results(results, user_total_score, dealer_total_score, user_cards, dealer_cards))
        return

    # If not, the user can keep requesting cards or choose to pass.
    while True:
        add_another_card = input("Do you want another card?\n"
                             "Type 'y' to get another card, type 'n' to pass: ").lower()

        if add_another_card == 'y':
            # Add a card to the user's hand and recalculate the total.
            user_cards.append(pick_random_cards(cards))
            adjust_for_ace(user_cards)
            user_total_score = sum_cards(user_cards)

            if user_total_score == 21:
                # The user hits exactly 21 — win.
                print(f"Your final hand: {user_cards}, final score: {user_total_score}")
                print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total_score}")
                print(show_results(results, user_total_score, dealer_total_score, user_cards, dealer_cards))
                return
            elif user_total_score > 21:
                # The user goes over 21 — bust.
                print(f"Your final hand: {user_cards}, final score: {user_total_score}")
                print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total_score}")
                print(show_results(results, user_total_score, dealer_total_score, user_cards, dealer_cards))
                return
            else:
                # The user is still under 21 — show the current state and ask again.
                print(f"Your cards: {user_cards}. Current score {user_total_score}")
                print(f"The dealer's first card: {dealer_cards[0]}")

        elif add_another_card == 'n':
            # The user passes. The dealer now draws cards until reaching a score of 17 or more.
            while dealer_total_score < 17:
                dealer_cards.append(pick_random_cards(cards))
                adjust_for_ace(dealer_cards)
                dealer_total_score = sum_cards(dealer_cards)

            # The dealer has finished drawing — show both hands and determine the winner.
            print(f"Your final hand: {user_cards}, final score: {user_total_score}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total_score}")
            print(show_results(results, user_total_score, dealer_total_score, user_cards, dealer_cards))
            return


# Ask the user if they want to play. If yes, start a new round. If no, exit the game.
while True:
    play_another_round = input("Do you want to play a game of Blackjack?\n"
                                "Type 'y' or 'n': ").lower()
    if play_another_round == 'y':
        print("\n" * 20)
        play_blackjack()
    elif play_another_round == 'n':
        print("See you later!")
        break