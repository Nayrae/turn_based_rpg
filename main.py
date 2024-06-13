from character import Character
from turns import combat


player = Character(input("How do you want to be rememebered?: "), 100, 100, 1, 10)
enemy = Character("Bruhv", 100, 15, 1, 50)

while True:
    combat(player, enemy)
    input("Press enter to exit")
    break