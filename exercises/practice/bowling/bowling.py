class BowlingGame:
    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        if self.current_roll < 20:
            raise IndexError("Incomplete or unstarted game")
        score = 0
        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return score
