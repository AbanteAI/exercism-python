def parse_hand(hand):
    return [card for card in hand.split()]

def rank_hand(hand):
    # This is a placeholder for the function that will evaluate the rank of a hand
    return 0  # Replace this with actual logic to rank the hand

def compare_hands(hand1, hand2):
    # This is a placeholder for the function that will compare two hands
    return 0  # Replace this with actual logic to compare the hands

def best_hands(hands):
    ranked_hands = [(rank_hand(parse_hand(hand)), hand) for hand in hands]
    highest_rank = max(ranked_hands, key=lambda x: x[0])[0]
    return [hand for rank, hand in ranked_hands if rank == highest_rank]