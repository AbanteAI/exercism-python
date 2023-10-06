class Character:
    def generate_character(self):
        abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        scores = []
        for _ in range(6):
            dice_rolls = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
            scores.append(sum(dice_rolls[:3]))
        self.abilities = dict(zip(abilities, scores))
        self.hitpoints = 10 + self.get_modifier('constitution')

    def get_modifier(self, ability):
        score = self.abilities.get(ability, 0)
        return (score - 10) // 2
