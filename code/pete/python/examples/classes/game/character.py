class Character:
    def __init__(self, name, weapon=None, ability=None):
        self.name = name
        self.hp = 100
        self.mana = 0
        self.weapon = weapon
        self.ability = ability
    
    def attack(self, enemy, weapon):
        print(f'{self} attacked {enemy}')
        enemy.hp -= weapon.damage
        if enemy.hp <= 0:
            enemy.hp = 0
            return enemy.die()
    
    def die(self):
        print(f'{self.name} died')
        return True

    def __str__(self):
        return f'{self.name} {self.weapon} hp: {self.hp}/100'
    
class Hero(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

class Villain(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

class Weapon:
    def __init__(self, name, damage, image='⚔️'):
        self.name = name
        self.damage = damage
        self.image = image
    
    def __str__(self):
        return f'{self.image}  {self.name}  {self.damage} damage'

class Ability(Weapon):
    def __init__(self, name, damage, cost):
        super().__init__(name, damage)
        self.cost = cost


if __name__ == '__main__':
    from time import sleep

    sword = Weapon('Greatsword', 30, '🗡️')
    dagger = Weapon('Dagger', 20, '🔪')
    axe = Weapon('Great Axe', 45, '🪓')

    print(sword)
    print(dagger)

    hero = Hero('Gawain', weapon=sword)
    villain = Villain('The Green Knight', weapon=axe)

    fighters = [hero, villain]

    turn = 0
    while True:
        sleep(1.5)
        attacker = fighters[turn % len(fighters)]
        attackee = fighters[(turn + 1) % len(fighters)]
        fight_over = attacker.attack(attackee, attacker.weapon)
        # print(f'{attacker} attacked {attackee}')
        if fight_over:
            print(f'Fight over, {attacker} wins')
            break
        turn += 1

