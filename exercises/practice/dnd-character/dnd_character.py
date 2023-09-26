import random

class Character:
    def __init__(self):
        self.strength = self._ability_score()
        self.dexterity = self._ability_score()
        self.constitution = self._ability_score()
        self.intelligence = self._ability_score()
        self.wisdom = self._ability_score()
        self.charisma = self._ability_score()

        self.hitpoints = 10 + self._modifier(self.constitution)

    def _ability_score(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.remove(min(dice_rolls))
        return sum(dice_rolls)

    def _modifier(self, score):
        return (score - 10) // 2
        self.dexterity = self._ability_score()
        self.constitution = self._ability_score()
        self.intelligence = self._ability_score()
        self.wisdom = self._ability_score()
        self.charisma = self._ability_score()

        self.hitpoints = 10 + self._modifier(self.constitution)

    def _ability_score(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.remove(min(dice_rolls))
        return sum(dice_rolls)

    def _modifier(self, score):
        return (score - 10) // 2
