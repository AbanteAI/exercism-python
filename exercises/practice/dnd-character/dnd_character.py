import random
class Character:
    def __init__(self):
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()
        self.hitpoints = 10 + self.ability_modifier(self.constitution)
    @staticmethod
    def roll_dice():
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])

    @staticmethod
    def ability_modifier(ability):
        return (ability - 10) // 2
