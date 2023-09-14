class HighScores:
    def __init__(self, scores):
        self.scores = scores
    def scores_list(self):
        return self.scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]

    def difference_latest_highest(self):
        return self.highest_score() - self.latest_score()
