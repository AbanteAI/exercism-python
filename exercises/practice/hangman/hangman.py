# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_letters = set()

    def guess(self, char):
        if char in self.guessed_letters:
            raise ValueError("You have already guessed this letter.")
        
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        self.guessed_letters.add(char)
        
        if char not in self.word:
            self.remaining_guesses -= 1

        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        
        if all(letter in self.guessed_letters for letter in self.word):
            self.status = STATUS_WIN

    def get_masked_word(self):
        masked_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        return masked_word

    def get_status(self):
        return self.status