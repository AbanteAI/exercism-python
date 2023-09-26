from rx.subject import Subject
from rx import operators as op
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
        self.guessed_chars = subject.Subject()
        self.masked_word = self.guessed_chars.pipe(
            op.scan(lambda masked_word, char: "".join(c if c == char or c in self.guessed_chars else "_" for c in self.word)),
            op.start_with("".join("_" for _ in self.word))
        )
        self.status = self.guessed_chars.pipe(
            op.scan(lambda status, _: STATUS_WIN if self.masked_word.value == self.word else STATUS_ONGOING if self.remaining_guesses > 0 else STATUS_LOSE),
            op.start_with(STATUS_ONGOING)
        )

    def guess(self, char):
        if self.status.value == STATUS_ONGOING and char not in self.guessed_chars.value:
            self.guessed_chars.on_next(char)
            if char not in self.word:
                self.remaining_guesses -= 1

    def get_masked_word(self):
        return self.masked_word.value

    def get_status(self):
        return self.status.value
    def guess(self, char):
        if self.status == STATUS_ONGOING and char not in self.guessed_chars:
            self.guessed_chars.on_next(char)
            if char not in self.word:
                self.remaining_guesses -= 1

    def get_masked_word(self):
        return "".join(c if c in self.guessed_chars else "_" for c in self.word)

    def get_status(self):
        if self.remaining_guesses > 0 and "_" not in self.get_masked_word():
            return STATUS_WIN
        elif self.remaining_guesses <= 0:
            return STATUS_LOSE
        else:
            return STATUS_ONGOING
