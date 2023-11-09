import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + self.modifier(self.constitution)

    def ability(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice_rolls, reverse=True)[:3])

    def modifier(self, constitution):
        return (constitution - 10) // 2

    def strength(self):
        return self.strength

    def dexterity(self):
        return self.dexterity

    def constitution(self):
        return self.constitution

    def intelligence(self):
        return self.intelligence

    def wisdom(self):
        return self.wisdom

    def charisma(self):
        return self.charisma

    def hitpoints(self):
        return self.hitpoints
