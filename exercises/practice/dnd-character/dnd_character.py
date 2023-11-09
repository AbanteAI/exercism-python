import random
class Character:
    def __init__(self):
        pass
def modifier(constitution):
    return (constitution - 10) // 2
    def ability(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls, reverse=True)[:3])


    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
