from character import Character
from enemy import *
from city import *
from quest.quest import *

#  __init__(self, name, health, mp_count, attack, healing_potions_count, gold) #

#enemy = Character("Bruhv", 100, 15, 1, 50, 200)
#enemy = random.choice(enemies)

def main():
    while True:
        if completed_quest_counter == 0:
            Quest.start(tutorial, player)
            travel_to_village(player)
        else:   
           #combat(player, enemy)
            travel_to_village(player)
            input("Press enter to exit")
            break
    
if __name__ == "__main__":
    main()