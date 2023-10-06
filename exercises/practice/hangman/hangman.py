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
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif char not in self.word:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
        elif self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif char not in self.word:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
        elif self.get_masked_word() == self.word:
            self.status = STATUS_WIN

        masked_word = ""
        for letter in self.word:
            if letter in self.guesses:
                masked_word += letter
            else:
                masked_word += "_"
        return masked_word

        return self.status
