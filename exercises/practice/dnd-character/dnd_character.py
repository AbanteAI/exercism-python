import random
from dnd_character import modifier

class Character:
    def __init__(self):
        self.strength = self._roll_dice()
        self.dexterity = self._roll_dice()
        self.constitution = self._roll_dice()
        self.intelligence = self._roll_dice()
        self.wisdom = self._roll_dice()
        self.charisma = self._roll_dice()
        self.hitpoints = 10 + self._calculate_modifier(self.constitution)

    def _roll_dice(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.sort(reverse=True)
        return sum(dice_rolls[:3])

    def _calculate_modifier(self, ability_score):
        return (ability_score - 10) // 2
