# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.guessed_chars = set()
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game already finished.")
        
        if char in self.guessed_chars:
            self.remaining_guesses -= 1
        else:
            self.guessed_chars.add(char)
            if char not in self.word:
                self.remaining_guesses -= 1

        self.update_status()

    def get_masked_word(self):
        return ''.join([c if c in self.guessed_chars else '_' for c in self.word])

    def get_status(self):
        return self.status

    def update_status(self):
        masked_word = self.get_masked_word()
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif '_' not in masked_word:
            self.status = STATUS_WIN
        else:
            self.status = STATUS_ONGOING
from collections import Counter

class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.guessed_chars = set()
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game already finished.")
        
        if char in self.guessed_chars:
            self.remaining_guesses -= 1
        else:
            self.guessed_chars.add(char)
            if char not in self.word:
                self.remaining_guesses -= 1

        self.update_status()

    def get_masked_word(self):
        return ''.join([c if c in self.guessed_chars else '_' for c in self.word])

    def get_status(self):
        return self.status

    def update_status(self):
        masked_word = self.get_masked_word()
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif '_' not in masked_word:
            self.status = STATUS_WIN
        else:
            self.status = STATUS_ONGOING
