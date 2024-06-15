## TODO
## village/city system, you come here after killing all enemies in the dungeon
## add various shops(inn+pub, flowershop for alchemy, blacksmith, central plaza + guild for quests, library for spell worldbuilding, church to counter curse or ressing )
##

import time



first_welcome = """
After vanquishing the last of the dungeon's denizens, you embark on a journey towards civilization. 
The dense forest gradually thins out, revealing the first signs of human habitation. 
A weathered sign, standing tall among the wildflowers, greets you with the words, 
'WELCOME TO THE VILLAGE', its letters carved deep into the wood.
    """

first_welcome2 ="""As you enter the village, you're greeted by the lively sights and sounds of the village life.
To your left, the warm glow of the Inn invites weary travelers. 
Ahead, the central plaza bustles with villagers, surrounded by the Blacksmith's clangs,
the subtle scent of the Flower Shop, and the quiet wisdom of the Guild and Library."""


def print_ascii_village():
    village_ascii = r"""
          
                ~         ~      /~
            ____________    __/   |      __________
          /             \__/      |     /  _______  \
         |                        |    |  /       \  |
         |   Inn       __ \       |    |  |Central|  |
         |                        |    |  | Plaza |  |
         |   ___       |_| \      |    |  |       |  |
         |  |   |      ___  \     |    |  |       |  |
         |  |   |     |   |  \    |    |  \_______/  |
         |  |   |     |   |   \   |     \           /
         |  |   |     |___|    \  |      ~~~~~~~~~~~
         |  |   |_______________\ |       
         |  |   |               |||      
         |  |   | Blacksmith    |||     ____________
         |  |   |               |||    /    ||      \
         |  |   |_______________|||   /     ||       \
         |  |   |               |||   |     ||       |
         |  |   | Flower Shop   |||   |Guild|Library |
         |  |___|_______________|||   |     ||       |
          || ||            || || |||   \    ||       /
          || ||            || || |||    ~~~~~~~~~~~~~
          || ||            || ||/  \             \ \
          || ||            || ||___/              \ \
          || ||            || ||                   \ \
        __||_||____________||_||____________________\ \
        \______________________________________________/
    """
    for line in village_ascii.split('\n'):
        print(line)
        time.sleep(0.1)  # Adjust the delay as needed
    

def travel_to_village():
    for line in first_welcome.split('\n'):
        print(line)
        time.sleep(1)  # Adjust the delay as needed
    
    time.sleep(0.5)
    
    for line in first_welcome2.split('\n'):
        print(line)
        time.sleep(1)  # Adjust the delay as needed
    
    time.sleep(3)
    print_ascii_village()
    time.sleep(1)
    player_move_in_village()

village_activities = [
    "1. Inn, rest and heal your wounds (also, there's some good ale)",
    "2. Blacksmith, upgrade your gear or purchase new equipment",
    "3. Flower Shop, buy flowers or special herbs",
    "4. Guild, find friends and accept quests",
    "5. Library, seek knowledge"
]

def player_move_in_village():
    print("Where would you like to go?:")
    for place in village_activities:
        print(place)
        time.sleep(0.5)
    choice = input("Enter the number of the activity you're going to do: ")
    if choice == 1:
        # Code for Inn
        pass
    elif choice == 2:
        # Code for Blacksmith
        pass
    elif choice == 3:
        # Code for Flower Shop
        pass
    elif choice == 4:
        # Code for Guild
        pass
    elif choice == 5:
        # Code for Library
        pass
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
travel_to_village()