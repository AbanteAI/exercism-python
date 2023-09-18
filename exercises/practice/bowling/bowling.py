class BowlingGame:
    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

        frames_played = 0
        frame_index = 0
        while frame_index < self.current_roll and frames_played < 10:
            if self.rolls[frame_index] == 10:  # Strike
                frame_index += 1
            else:
                frame_index += 2
            frames_played += 1

        if frames_played < 10:
            raise ValueError("Incomplete game")
        total_score = 0
        frame_index = 0
        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return total_score
