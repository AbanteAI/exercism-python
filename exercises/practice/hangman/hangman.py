# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

def guess(self, char):
    if char not in self.word:
        self.remaining_guesses -= 1
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
    else:
        self.word = self.word.replace(char, '')
        if not self.word:
            self.status = STATUS_WIN
        pass

def get_masked_word(self):
    return ''.join(c if c not in self.word else '_' for c in self.word)

def get_status(self):
    return self.status