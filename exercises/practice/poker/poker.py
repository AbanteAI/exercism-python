from exercises.practice.poker.poker_utils import rank_hand
def best_hands(hands):
    # Sort hands in descending order based on hand rank
    hands.sort(key=rank_hand, reverse=True)
    
    # Get the highest rank of the first hand
    highest_rank = rank_hand(hands[0])
    
    # Filter hands with the highest rank
    best_hands = [hand for hand in hands if rank_hand(hand) == highest_rank]
    
    return best_hands
