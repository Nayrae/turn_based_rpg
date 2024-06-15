## TODO
## add weapons(with respective damage)
## add more enemies
## add more playable characters
## dont forget to make sure that turns work decently
## add different actions(block, magic, curse)
## add items(i'm switching heal to potions)
## adding gold with a SHOP system 
##adding ress system

import os, sys
import random 
import time
import winsound
from character import *
from city import *
from enemy import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

win_audio_path = resource_path("win.wav")




turn_count = 1

def increment_turn():
    global turn_count  # Declare turn_count as global to modify the global variable
    turn_count += 1

def print_grid(player, enemy):
    header = f"{'Name':<15}{'Damage':<15}{'Health':<15}{'Mana':<15}{'Health Pots':<15}{'Gold':<15}"
    character_row = f"{player.name:<15}{player.attack:<15}{int(player.health):<15}{player.mp_count:<15}{player.heal_pot_count:<15}{player.gold:<15}"
    enemy_row = f"{enemy.name:<15}{enemy.attack:<15}{int(enemy.health):<15}{enemy.mp_count:<15}{enemy.heal_pot_count:<15}{enemy.gold:<15}"
    
    print("\n")
    print("TURN ", turn_count, " HAS ENDED!")
    print("\n")
    print(header)
    print('-' * len(header))
    print(character_row)
    print(enemy_row)
    print("\n")
    
def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        action = input("Do you want to (A)ttack, (H)eal or use a (M)agic?: ")
        if action.lower() == "a":
            player.perform_attack(enemy)
        elif action.lower() == "h":
                player.heal()
        elif action.lower() == "m":
                player.magic_attack(enemy)
        else:
            continue
        time.sleep(0.5)    
        if enemy.is_alive():
            if turn_count == 1:
                enemy.perform_attack(player)                
            elif random.randint(1,3) == 3:
                enemy.heal()
            else:
                enemy.perform_attack(player)
            
        if player.is_alive and not enemy.is_alive():
            player.gold += enemy.gold
            print("You WON!")
            winsound.PlaySound(win_audio_path, winsound.SND_FILENAME)
            travel_to_village()
        elif not player.is_alive():
            print("You LOST!")
        else:
            time.sleep(0.5)
            print_grid(player, enemy)
            time.sleep(0.5)
            increment_turn()
            continue
       