# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_chars = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game over")
        if char in self.guessed_chars or (char not in self.word and char not in self.guessed_chars):
            self.remaining_guesses -= 1
        self.guessed_chars.add(char)
            self.guessed_chars.add(char)
        if set(self.word).issubset(self.guessed_chars):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

        pass
    def get_masked_word(self):
        return ''.join(c if c in self.guessed_chars else '_' for c in self.word)
        pass

        return self.status
    def get_status(self):
        return self.status
        pass
