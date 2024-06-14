from character import Character
from turns import combat

#  __init__(self, name, health, mp_count, attack, healing_potions_count, gold) #
player = Character(input("How do you want to be rememebered?: "), 100, 100, 50, 10, 100)
enemy = Character("Bruhv", 100, 15, 1, 50, 200)

while True:
    combat(player, enemy)
    input("Press enter to exit")
    break