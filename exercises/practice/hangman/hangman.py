# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.masked_word = '_' * len(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if char in self.word and char not in self.masked_word:
            self.masked_word = ''.join([c if c == char else self.masked_word[i] for i, c in enumerate(self.word)])
        else:
            self.remaining_guesses -= 1
        self.status = self.get_status()

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        if self.remaining_guesses < 0:
            return STATUS_LOSE
        elif self.masked_word == self.word:
            return STATUS_WIN
        else:
            return STATUS_ONGOING
