## TODO
## add weapons(with respective damage)
## add more enemies
## add more playable characters
## dont forget to make sure that turns work decently
##
import random 

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.attack = attack
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def perform_attack(self, other):
        other.health -= self.attack
        print(f'{other.name} has taken {self.attack} DMG from {self.name}')
    
    def heal(self):
        # STILL HAVE TO CAP MAX HP
        rand_heal = random.uniform(1/2, 2)
        healing = self.attack * rand_heal
        self.health += healing
        print(f'{self.name} has healed for a total of {healing} HPs')
    
def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        action = input("Do you want to (A)ttack or (H)eal?: ")
        if action.lower() == "a":
            player.perform_attack(enemy)
        elif action.lower() == "h":
                player.heal()
        else:
            continue
            
        if enemy.is_alive():
            if random.choice(["attack", "heal"]) == "attack":
                enemy.perform_attack(player)
            else:
                enemy.heal()
                print(f'{enemy.name} has healed, {enemy.health} HPs left.')
            
        if player.is_alive and not enemy.is_alive():
            print("You WON!")
        elif not player.is_alive():
            print("You LOST!")
        else:
            continue
        
player = Character("Player", 100, 20)
enemy = Character("Enemy", 100, 15)
combat(player, enemy)