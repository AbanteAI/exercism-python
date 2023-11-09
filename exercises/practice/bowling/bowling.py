class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1
        self.frame_first_roll = True
        self.game_complete = False

    def roll(self, pins):
        if self.game_complete:
            raise ValueError("Cannot roll after game is complete")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must have a value from 0 to 10")
        if not (0 <= self.current_frame <= 10):
            raise ValueError("Rolls can only be made in frames 1 to 10")
        if self.frame_first_roll or self.current_frame == 10:
            self.rolls.append(pins)
            if pins == 10:
                if self.current_frame < 10:
                    self.current_frame += 1
                elif len(self.rolls) < 21:  # Allow for bonus rolls in the tenth frame
                    self.frame_first_roll = False
            else:
                self.frame_first_roll = False
        else:
            if self.rolls[-1] + pins > 10:
                raise ValueError("Pin count exceeds pins on the lane")
            self.rolls.append(pins)
            if self.current_frame < 10:
                self.current_frame += 1
                self.frame_first_roll = True
            elif len(self.rolls) == 21 or (len(self.rolls) == 20 and self.rolls[-2] != 10):
                self.game_complete = True

    def score(self):
        if not self.game_complete:
            raise ValueError("Score cannot be taken until the end of the game")
        score = 0
        roll_index = 0
        for frame in range(1, 11):
            if self.rolls[roll_index] == 10:  # Strike
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif sum(self.rolls[roll_index:roll_index + 2]) == 10:  # Spare
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                score += sum(self.rolls[roll_index:roll_index + 2])
                roll_index += 2
            if frame == 10:  # In the tenth frame, add bonus rolls
                score += sum(self.rolls[roll_index:roll_index + (21 - len(self.rolls))])
        return score
