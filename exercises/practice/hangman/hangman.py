# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = set()
        self.masked_word = "_" * len(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
    def guess(self, char):
        if self.status != STATUS_ONGOING or char in self.guessed_letters:
            return
        if char in self.word:
            self.masked_word = "".join([char if c == char else self.masked_word[i] for i, c in enumerate(self.word)])
            if "_" not in self.masked_word:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
        self.guessed_letters.add(char)

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
