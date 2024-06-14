## TODO
## village/city system, you come here after killing all enemies in the dungeon
## add various shops(inn+pub, flowershop for alchemy, blacksmith, central plaza + guild for quests, library for spell worldbuilding, church to counter curse or ressing )
##


def print_ascii_village():
    print(r"""
          
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
    """)
    

def travel_to_village():
    print("""
After vanquishing the last of the dungeon's denizens, you embark on a journey towards civilization. 
The dense forest gradually thins out, revealing the first signs of human habitation. 
A weathered sign, standing tall among the wildflowers, greets you with the words, 
'WELCOME TO THE VILLAGE', its letters carved deep into the wood.
    """)
    print("""As you enter the village, you're greeted by the lively sights and sounds of the village life.
To your left, the warm glow of the Inn invites weary travelers. 
Ahead, the central plaza bustles with villagers, surrounded by the Blacksmith's clangs,
the subtle scent of the Flower Shop, and the quiet wisdom of the Guild and Library.""")
    print_ascii_village()
    