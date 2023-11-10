class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must have a value from 0 to 10")
        if self.current_roll >= 20 and not self._is_extra_roll():
            raise IndexError("Cannot roll after game is over")
        if self.current_roll == 20 and self.rolls[18] != 10 and sum(self.rolls[18:20]) < 10:
            raise ValueError("No more rolls allowed after the 10th frame unless a strike or spare is scored")
        if self.current_roll > 20 and (self.rolls[18] != 10 and sum(self.rolls[18:20]) != 10):
            raise IndexError("Cannot roll after bonus roll for spare in the 10th frame")
        if self.current_roll > 21:
            raise IndexError("Cannot roll after bonus rolls for strike in the 10th frame")
        if self.current_roll % 2 == 0 and self.current_roll < 18 and self.rolls and self.rolls[-1] != 10 and self.rolls[-1] + pins > 10:
            raise ValueError("Pin count exceeds pins on the lane")
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        if not self._is_game_over():
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

    def _is_extra_roll(self):
        # Check if the last frame is a strike or a spare
        is_strike = self.rolls[18] == 10
        is_spare = self.rolls[18] != 10 and sum(self.rolls[18:20]) == 10
        # Allow for extra rolls if last frame is a strike or a spare
        return is_strike or is_spare

    def _is_game_over(self):
        # Game is over after 20 rolls, or after bonus rolls for strikes/spares in the 10th frame
        if self.current_roll < 20:  # Less than 20 rolls means game is not over
            return False
        if self.current_roll == 20 and self._is_extra_roll():  # 20 rolls and a spare or strike in the 10th frame
            return False
        if self.current_roll == 21 and self.rolls[18] == 10:  # 21 rolls and a strike in the 10th frame
            return False
        return True  # No more rolls allowed, game is over
