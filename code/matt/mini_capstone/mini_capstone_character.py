import mini_capstone_character_creation

mini_capstone_character_creation.main()
with open('character.txt', 'r') as file:
    stats = file.read().split('\n')

# human +1 all
# elf +2 dex +1 int
# dragonborn +2 str +1 cha
# tiefling +1 int +2 cha
# half-orc +2 str +1 con


class Character:

    def __init__(self, name, level, race, background) -> None:
        self.name = name
        self.level = level
        self.race = race
        self.background = background

    def mod(i):
        text = (stats[i])
        int_stat = int(text)
        return (int_stat - 10) // 2

    def strength(self):
        strength = [
            Character.mod(1),
            Character.mod(1)
        ]
        if stats[7] == 'Barbarian' or stats[7] == 'Fighter' or stats[7] == 'Monk' or stats[7] == 'Ranger':
            strength[0] += 2
        return strength

    def dexterity(self):
        dexterity = [
            Character.mod(2),
            Character.mod(2),
            Character.mod(2),
            Character.mod(2)
        ]
        if stats[7] == 'Bard' or stats[7] == 'Monk' or stats[7] == 'Ranger' or stats[7] == 'Rouge':
            dexterity[0] += 2
        return dexterity

    def constitution(self):
        if stats[7] == 'Barbarian' or stats[7] == 'Fighter' or stats[7] == 'Sorcerer':
            return Character.mod(3) + 2
        return Character.mod(3)

    def intelligence(self):
        intelligence = [
            Character.mod(4),
            Character.mod(4),
            Character.mod(4),
            Character.mod(4),
            Character.mod(4),
            Character.mod(4)
        ]
        if stats[7] == 'Druid' or stats[7] == 'Rouge' or stats[7] == 'Wizard':
            intelligence[0] += 2
        return intelligence

    def wisdom(self):
        wisdom = [
            Character.mod(5),
            Character.mod(5),
            Character.mod(5),
            Character.mod(5),
            Character.mod(5),
            Character.mod(5),
        ]
        if stats[7] == 'Cleric' or stats[7] == 'Druid' or stats[7] == 'Paladin' or stats[7] == 'Warlock':
            wisdom[0] += 2
        return wisdom

    def charisma(self):
        charisma = [
            Character.mod(6),
            Character.mod(6),
            Character.mod(6),
            Character.mod(6),
            Character.mod(6),
        ]
        if stats[7] == 'Bard' or stats[7] == 'Cleric' or stats[7] == 'Paladin' or stats[7] == 'Sorcerer' or stats[7] == 'Warlock':
            charisma[0] += 2
        return charisma

    def health(self):
        health = [
            ['hp', 15],
            ['ac', 14],
            ['temp_hp', 0],
            ['hit_dice', '1d12'],
            ['speed', '25ft'],
            ['initiative', 1]
        ]
        return health


character = Character(stats[0], 1, 'Dwarf', 'Criminal')
