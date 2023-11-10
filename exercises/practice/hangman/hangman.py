# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word.lower()
        self.masked_word = '_' * len(word)
        self.guessed_letters = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        char = char.lower()
        if char in self.guessed_letters or char not in self.word:
            self.remaining_guesses -= 1
        else:
            self.guessed_letters.add(char)
            self.masked_word = ''.join([c if c in self.guessed_letters else '_' for c in self.word])
        self.update_status()

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

    def update_status(self):
        if '_' not in self.masked_word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING
