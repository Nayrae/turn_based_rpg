import random 
from character import *

class Enemy:
    def __init__(self, name, health, attack, heal_pot_count, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.heal_pot_count = heal_pot_count
        self.gold = gold
        
    def is_alive(self):
        return self.health > 0
    
    def attack_character(self, character):
        #physical attack, can crit
        crit = random.randint(1, 10)
        if crit == 10:
            character.health -= self.attack*2
            print(f'{self.name} has dealt {self.attack*2} DMG to {character.name} thanks to a critical hit!')
        elif crit == 1:
            character.health -= self.attack*0.5
            print(f'{self.name} has dealt {self.attack*0.5} DMG to {character.name} due to a critical failure!')
        else:
            character.health -= self.attack
            print(f'{self.name} has dealt {self.attack} DMG to {character.name}')
    
    def heal(self):
        if self.heal_pot_count > 0:
            rand_heal = random.uniform(1/2, 3/2)
            healing = self.attack * rand_heal
            # Ensure health does not exceed max_health
            self.health = min(self.health + healing, self.max_health)
            print(f'{self.name} has healed for a total of {int(healing)} HPs')
            self.heal_pot_count -= 1
        else:
            print(f'{self.name} forgot that they have no more potions, turn wasted!')

goblin = Enemy("Goblin", 30, 5, 0, 10)
orc = Enemy("Orc", 50, 10, 1, 25)
troll = Enemy("Troll", 70, 15, 1, 50)

enemies = [goblin, orc, troll]