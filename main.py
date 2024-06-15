from character import Character
from turns import combat
from enemy import *
from city import *

#  __init__(self, name, health, mp_count, attack, healing_potions_count, gold) #
player = Character(input("How do you want to be rememebered?: "), 100, 100, 50, 10, 100)
#enemy = Character("Bruhv", 100, 15, 1, 50, 200)
enemy = random.choice(enemies)

def main():
    while True:
        combat(player, enemy)
        travel_to_village(player)
        input("Press enter to exit")
        break
    
if __name__ == "__main__":
    main()