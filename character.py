##TODO
## make savefile and load with pickle module 


import random
from turns import combat
from magic import *

class Character:
    def __init__(self, name, health, mp_count, attack, healing_potions_count, gold):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = health #stores starting health
        self.heal_pot_count = healing_potions_count
        self.gold = gold
        self.mp_count = mp_count
    
    def has_magic(self):
        if self.mp_count >0:
            return True
        else:
            return False
            
    def is_alive(self):
        return self.health > 0
    
    def magic_attack(self, other):
        #magic attack, can't crit
        print("Avaiable Spells: ")
        for index, spell in enumerate (all_spells, start = 1):   #Show spell grid(name, cost, dmg)
            print(f'{index}. {spell.name} - Mana Cost: {spell.cost}, Damage: {spell.damage}')
        
        choice = int(input("Which spell would you like to use(Number)?: "))
        selected_spell = all_spells[choice - 1]
        
        if self.mp_count >= selected_spell.cost:
            print(f'{self.name} used {selected_spell.name}!')
            other.health -= selected_spell.damage
            self.mp_count -= selected_spell.cost
            print(f'{selected_spell.name} dealt {selected_spell.damage} to {other.name}')
        else:
            print("Not enough mana to cast this spell.")
    
    def perform_attack(self, other):
        #physical attack, can crit
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
