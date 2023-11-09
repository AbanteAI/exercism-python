class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1
        self.first_in_frame = True

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        if self.current_frame > 10 or (self.current_frame == 10 and len(self.rolls) >= 21):
            raise IndexError("Cannot roll after game is over")
        if not self.first_in_frame and self.rolls[-1] + pins > 10:
            raise ValueError("Pin count exceeds pins on the lane")
        self.rolls.append(pins)
        if self.current_frame < 10 and (pins == 10 or not self.first_in_frame):
            self.current_frame += 1
        elif self.current_frame == 10:
            if len(self.rolls) == 20 and self.rolls[-2] != 10 and self.rolls[-1] + self.rolls[-2] < 10:
                raise IndexError("No more rolls after the end of the tenth frame")
            if len(self.rolls) == 21 and self.rolls[-3] != 10:
                raise IndexError("No more rolls after the bonus roll for a spare")
        self.first_in_frame = not self.first_in_frame if pins < 10 else True

    def score(self):
        if not self.is_game_over():
            raise IndexError("Score cannot be taken until the end of the game")
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.rolls[roll_index] == 10:  # Strike
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:  # Spare
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:  # Open frame
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return score

    def is_game_over(self):
        return (self.current_frame > 10 or
                (self.current_frame == 10 and
                 ((self.rolls[-1] != 10 and len(self.rolls) >= 20) or
                  (self.rolls[-1] == 10 and len(self.rolls) >= 21))))
