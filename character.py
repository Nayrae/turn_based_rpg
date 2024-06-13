import random
from turns import combat

class Character:
    def __init__(self, name, health, attack, healing_potions_count, gold):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = health #stores starting health
        self.heal_pot_count = healing_potions_count
        self.gold = gold
        
    def is_alive(self):
        return self.health > 0
    
    def perform_attack(self, other):
        crit = random.randint(1, 10)
        if crit == 10:
            other.health -= self.attack*2
            print(f'{self.name} has dealt {self.attack*2} DMG to {other.name} thanks to a critical hit!')
        elif crit == 1:
            other.health -= self.attack*0.5
            print(f'{self.name} has dealt {self.attack*0.5} DMG to {other.name} due to a critical failure!')
        else:
            other.health -= self.attack
            print(f'{self.name} has dealt {self.attack} DMG to {other.name}')
    
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
