class BowlingGame:
    def __init__(self):
        self.frames = [[] for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        self.frames[self.current_frame].append(pins)

    def score(self):
        total_score = 0
        for frame_index, frame in enumerate(self.frames):
            if frame_index < 9:
                if len(frame) == 2 and sum(frame) == 10:
                    total_score += sum(frame) + self.frames[frame_index+1][0]
                elif len(frame) == 1 and frame[0] == 10:
                    if len(self.frames[frame_index+1]) == 1:
                        total_score += sum(frame) + sum(self.frames[frame_index+1])
                    else:
                        total_score += sum(frame) + sum(self.frames[frame_index+1][:2])
                else:
                    total_score += sum(frame)
            else:
                total_score += sum(frame)
        return total_score