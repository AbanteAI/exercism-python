class Character:
    def generate_character(self):
        abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        scores = []
        for _ in range(6):
            dice_rolls = [random.randint(1, 6) for _ in range(4)]
            dice_rolls.sort(reverse=True)
            score = sum(dice_rolls[:3])
            scores.append(score)
        
        self.strength = scores[0]
        self.dexterity = scores[1]
        self.constitution = scores[2]
        self.intelligence = scores[3]
        self.wisdom = scores[4]
        self.charisma = scores[5]
        
        self.hitpoints = 10 + (self.constitution - 10) // 2

    def modifier(self, score):
        return (score - 10) // 2