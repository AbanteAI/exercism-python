class HighScores:
        self.scores = scores
        pass
    def highest(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def top_three(self):
        return sorted(self.scores, reverse=True)[:3]