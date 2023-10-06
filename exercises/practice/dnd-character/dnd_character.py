import random
def __init__(self):
    self.strength = self.ability()
    self.dexterity = self.ability()
    self.constitution = self.ability()
    self.intelligence = self.ability()
    self.wisdom = self.ability()
    self.charisma = self.ability()
    self.hitpoints = 10 + self.modifier(self.constitution)
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + self.modifier(self.constitution)

    def ability(self):
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.remove(min(dice))
        return sum(dice)

    def modifier(self, constitution):
        return (constitution - 10) // 2