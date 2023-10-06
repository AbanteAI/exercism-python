class BowlingGame:
    def __init__(self):
        self.rolls = []

        if pins < 0 or pins > 10:
            raise ValueError("Invalid roll: Pins knocked down must be between 0 and 10.")

        if len(self.rolls) >= 18 and self.is_strike(16) and (pins < 0 or pins > 10):
            raise ValueError("Invalid roll: Bonus roll after a strike in the last frame cannot score more than 10 points.")

        if len(self.rolls) >= 19 and self.is_spare(18) and (pins < 0 or pins > 10):
            raise ValueError("Invalid roll: Cannot roll after bonus roll for spare.")

        if len(self.rolls) >= 20 and self.is_strike(18) and (pins < 0 or pins > 10):
            raise ValueError("Invalid roll: Cannot roll after bonus rolls for strike.")

    def score(self):
        total_score = 0
        roll_index = 0

        for _ in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2

        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]