# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    if category == YACHT:
        return calculate_yacht_score(dice)
    elif category == ONES:
        return calculate_ones_score(dice)
    elif category == TWOS:
        return calculate_twos_score(dice)
    elif category == THREES:
        return calculate_threes_score(dice)
    elif category == FOURS:
        return calculate_fours_score(dice)
    elif category == FIVES:
        return calculate_fives_score(dice)
    elif category == SIXES:
        return calculate_sixes_score(dice)
    elif category == FULL_HOUSE:
        return calculate_full_house_score(dice)
    elif category == FOUR_OF_A_KIND:
        return calculate_four_of_a_kind_score(dice)
    elif category == LITTLE_STRAIGHT:
        return calculate_little_straight_score(dice)
    elif category == BIG_STRAIGHT:
        return calculate_big_straight_score(dice)
    elif category == CHOICE:
        return calculate_choice_score(dice)
    else:
        return 0


def calculate_yacht_score(dice):
    # TODO: Implement the calculation for the YACHT category
    pass


def calculate_ones_score(dice):
    # TODO: Implement the calculation for the ONES category
    pass


def calculate_twos_score(dice):
    # TODO: Implement the calculation for the TWOS category
    pass


def calculate_threes_score(dice):
    # TODO: Implement the calculation for the THREES category
    pass


def calculate_fours_score(dice):
    # TODO: Implement the calculation for the FOURS category
    pass


def calculate_fives_score(dice):
    # TODO: Implement the calculation for the FIVES category
    pass


def calculate_sixes_score(dice):
    # TODO: Implement the calculation for the SIXES category
    pass


def calculate_full_house_score(dice):
    # TODO: Implement the calculation for the FULL_HOUSE category
    pass


def calculate_four_of_a_kind_score(dice):
    # TODO: Implement the calculation for the FOUR_OF_A_KIND category
    pass


def calculate_little_straight_score(dice):
    # TODO: Implement the calculation for the LITTLE_STRAIGHT category
    pass


def calculate_big_straight_score(dice):
    # TODO: Implement the calculation for the BIG_STRAIGHT category
    pass


def calculate_choice_score(dice):
    # TODO: Implement the calculation for the CHOICE category
    pass


def score(dice, category):
    pass
