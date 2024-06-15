#from character import Character
import os, sys
import random 
import time
import winsound
from character import *
from city import *
from enemy import *

completed_quest_counter = 0

player = Character(input("How do you want to be rememebered?: "), 100, 100, 50, 10, 100)

turn_count = 1


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

win_audio_path = resource_path("win.wav")

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
    while player.is_alive() and active_quest[0].enemies[0].is_alive():
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
                enemy.attack_character(player)                
            elif random.randint(1,3) == 3:
                enemy.heal()
            else:
                enemy.attack_character(player)
            
        if player.is_alive and not enemy.is_alive():
            player.gold += enemy.gold
            print("You WON!")
            winsound.PlaySound(win_audio_path, winsound.SND_FILENAME)
            break
        elif not player.is_alive():
            print("You LOST!")
        else:
            time.sleep(0.5)
            print_grid(player, enemy)
            time.sleep(0.5)
            increment_turn()
            continue
      

       
       
class Quest:
    def __init__(self, name, description, enemies):
        self.name = name
        self.description = description
        self.enemies = enemies
    
    def start(self, player):
        print(self.description)
        for enemy in self.enemies:
            if player.is_alive() and enemy.is_alive():
                combat(player, enemy)
            if not player.is_alive():
                print("You have been defeated. Quest failed.")
                break
        else:
            self.complete_quest()
        
    def complete_quest(self):
        global completed_quest_counter
        self.is_completed = True
        completed_quest_counter += 1
        print("Quest completed succesfully!")
    #def start_quest(active_quest):
    #    completed_quest_counter = 0
    #    for enemy in active_quest.enemies:
    #        combat(player, active_quest.enemies[0])
    #        if enemy.health <= 0:
    #            active_quest.enemies.remove(enemy)
    #            print(f'{enemy.name} defeated!')
    #        if not active_quest.enemies:
    #            print(f'Quest "{active_quest.name}" has been completed!')
    #            completed_quest_counter += 1
       
        
tutorial_enemies = [Enemy("Goblin", 30, 5, 0, 0, 10), Enemy("Orc", 50, 10, 25, 1, 25), Enemy("Troll", 70, 15, 40, 2, 50)]
enemies = [Enemy("Goblin", 30, 5, 0, 0, 10), Enemy("Troll", 50, 10, 0, 0, 0), Enemy("Dragon", 100, 20, 0, 0, 0)]

tutorial = Quest("Escape the dungeon alive(optional)", "Defeat the enemies that appear in front of you", tutorial_enemies)
quest1 = Quest("Save the Village", "Defeat the enemies attacking the village.", enemies[:2])
quest2 = Quest("Dragon Slayer", "Defeat the dragon on the mountain.", [enemies[2]])

quests = [quest1, quest2]

active_quest = quests

     
            
            
            