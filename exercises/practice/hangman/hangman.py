# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.word = word
        self.guessed_chars = set()
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if char not in self.guessed_chars:
            if char in self.word:
                self.guessed_chars.add(char)
            else:
                self.remaining_guesses -= 1
        if set(self.word).issubset(self.guessed_chars):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join([char if char in self.guessed_chars else '_' for char in self.word])

    def get_status(self):
        return self.status
