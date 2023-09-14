class Character:
    def __init__(self):
        pass
import random

def modifier(score):
    return (score - 10) // 2

def ability():
    return sum(sorted(random.choices(range(1, 7), k=4))[-3:])

class Character:
    def __init__(self):
        self.strength = ability()
        self.dexterity = ability()
        self.constitution = ability()
        self.intelligence = ability()
        self.wisdom = ability()
        self.charisma = ability()
        self.hitpoints = 10 + modifier(self.constitution)
