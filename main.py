from character import Character
from turns import combat


player = Character("Emily", 100, 15, 1, 10)
enemy = Character("Bruhv", 100, 15, 1, 50)
combat(player, enemy)