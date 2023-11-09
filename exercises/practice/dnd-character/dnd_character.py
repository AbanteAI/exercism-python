class Character:
    def __init__(self):
        pass
class Character:
    import random

    def ability(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice_rolls, reverse=True)[:3])

    def modifier(self, constitution):
        return (constitution - 10) // 2

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + self.modifier(self.constitution)
