class HighScores:
    def __init__(self, scores):
    def latest(self):
        return self.scores[-1]
        return self.scores[-1]

    def get_highest_score(self):
        return max(self.scores)
        return max(self.scores)

    def get_last_added_score(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores)

    def get_three_highest_scores(self):
        sorted_scores = sorted(self.scores, reverse=True)
        return sorted_scores[:3]
        sorted_scores = sorted(self.scores, reverse=True)
    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
