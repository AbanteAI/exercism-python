class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_score(self):
        if self.scores:
            return max(self.scores)
        else:
            return None

    def last_added_score(self):
        if self.scores:
            return self.scores[-1]
        else:
            return None

    def top_three_scores(self):
        sorted_scores = sorted(self.scores, reverse=True)
        return sorted_scores[:3]
