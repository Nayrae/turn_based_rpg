## TODO
## add weapons(with respective damage)
## add more enemies
## add more playable characters
## dont forget to make sure that turns work decently
## add different actions(block, magic, curse)
## add items(i'm switching heal to potions)
import random 
import time


class Character:
    def __init__(self, name, health, attack, healing_potions_count):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = health #stores starting health
        self.heal_pot_count = healing_potions_count
        
    def is_alive(self):
        return self.health > 0
    
    def perform_attack(self, other):
        crit = random.randint(1, 10)
        if crit == 10:
            other.health -= self.attack*2
            print(f'{self.name} has dealt {self.attack*2} DMG to {other.name}')
        elif crit == 1:
            other.health -= self.attack*0.5
            print(f'{self.name} has dealt {self.attack*0.5} DMG to {other.name}')
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
            

def print_grid(player, enemy):
    header = f"{'Name':<10}{'Damage':<10}{'Health':<10}{'Health Pots':<10}"
    character_row = f"{player.name:<10}{player.attack:<10}{int(player.health):<10}{player.heal_pot_count:<10}"
    enemy_row = f"{enemy.name:<10}{enemy.attack:<10}{int(enemy.health):<10}{enemy.heal_pot_count:<10}"
    
    print("\n")
    print(header)
    print('-' * len(header))
    print(character_row)
    print(enemy_row)
    print("\n")
    
def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        action = input("Do you want to (A)ttack or (H)eal?: ")
        if action.lower() == "a":
            player.perform_attack(enemy)
        elif action.lower() == "h":
                player.heal()
        else:
            continue
        time.sleep(0.5)    
        if enemy.is_alive():
            if random.choice(["attack", "heal"]) == "attack":
                enemy.perform_attack(player)
            else:
                enemy.heal()
            
        if player.is_alive and not enemy.is_alive():
            print("You WON!")
        elif not player.is_alive():
            print("You LOST!")
        else:
            time.sleep(0.5)
            print_grid(player, enemy)
            time.sleep(0.5)
            continue
        
player = Character("Emily", 100, 20, 2)
enemy = Character("Bruhv", 100, 15, 1)
combat(player, enemy)
