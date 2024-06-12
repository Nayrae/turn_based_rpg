from turn import Character
from turn import combat


player = Character("Emily", 100, 15, 1)
enemy = Character("Bruhv", 100, 15, 1)
combat(player, enemy)
