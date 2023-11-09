from collections import Counter

# Poker hands ranked from highest to lowest
HAND_RANKS = {
    'Royal Flush': 10,
    'Straight Flush': 9,
    'Four of a Kind': 8,
    'Full House': 7,
    'Flush': 6,
    'Straight': 5,
    'Three of a Kind': 4,
    'Two Pair': 3,
    'One Pair': 2,
    'High Card': 1
}

def evaluate_hand(hand):
    # This function will evaluate the hand and return its rank and the highest card for comparison
    # Implementation of hand evaluation logic goes here
    pass

def compare_hands(hand1, hand2):
    # This function will compare two hands and return the better hand
    # Implementation of hand comparison logic goes here
    pass

def best_hands(hands):
    best_hand = hands[0]
    for hand in hands[1:]:
        best_hand = compare_hands(best_hand, hand)
    return [hand for hand in hands if hand == best_hand]