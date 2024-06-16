## TODO
## village/city system, you come here after killing all enemies in the dungeon
## add various shops(inn+pub, flowershop for alchemy, blacksmith, central plaza + guild for quests, library for spell worldbuilding, church to counter curse or ressing )
##

import time
from character import *
from animations.blacksmith_sign import *
from animations.dialogue import typing_effect

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

enter_inn = """
As you push open the heavy wooden door of the Inn, a wave of warmth and the rich aroma of stewed meat and fresh bread envelops you. 
The Innkeeper, a robust woman with a welcoming smile, notices your arrival and gestures towards a cozy corner by the fireplace.

Innkeeper: Welcome, traveler! You look like you've been on quite the journey. 
Here at our Inn, you can rest, eat, and replenish your strength. 
We have rooms available if you need rest, 
and our kitchen is always open to serve hearty meals that will heal your wounds and restore your spirit. 
What will it be for you today?:
    1. "I'd like to rent a room for the night."
    2. "I'm here to eat. What's on the menu?"
    3. "I'd like to buy some food to take with me."
"""
innkeeper_choice_answer = """The Innkeeper nods at your choice, ready to provide whatever you need to continue your adventures with renewed vigor."""

inn_rest_text = """"
You enter the cozy room and lay down on the comfortable bed.
The soft pillows and warm blankets envelop you, easing your tired muscles.
As you close your eyes, you feel a sense of peace and relaxation wash over you.
The sound of crackling fire from the fireplace lulls you into a deep and restful sleep.
You wake up the next morning feeling refreshed and ready to take on new adventures."""

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
        typing_effect(line, 0.005)
        

def travel_to_village(player):
    typing_effect(first_welcome)
    
    time.sleep(0.5)
    
    typing_effect(first_welcome2)
    
    time.sleep(2)
    print_ascii_village()
    time.sleep(1)
    player_move_in_village(player)

village_activities = [
    "   1. Inn, rest and heal your wounds (also, there's some good ale)",
    "   2. Blacksmith, upgrade your gear or purchase new equipment",
    "   3. Flower Shop, buy flowers or special herbs",
    "   4. Guild, find friends and accept quests",
    "   5. Library, seek knowledge"]

def inn_room_rent(character):
    typing_effect(inn_rest_text)
    character.inn_heal(character.max_health, character.max_mp_count)

def order_food(character):
    food_menu = {
        "   1": {"name": "Roasted Chicken", "price": 10, "healing": 20},
        "   2": {"name": "Beef Stew", "price": 15, "healing": 30},
        "   3": {"name": "Vegetable Soup", "price": 8, "healing": 15},
        "   4": {"name": "Bread and Cheese", "price": 5, "healing": 10},
    }
    
    typing_effect("Here's our menu(Number):")
    for item in food_menu:
        typing_effect(f"{item}. {food_menu[item]['name']} - {food_menu[item]['price']} gold")
    
    choice = input("Enter the number of the food you'd like to order: ")
    
    # Convert choice to integer if food_menu keys are integers
    try:
        choice = int(choice)
    except ValueError:
        typing_effect("Please enter a valid number.")
    else:
        if choice in food_menu:
            food = food_menu[choice]
            if character.gold >= food["price"]:
                character.gold -= food["price"]
                character.add_to_storage(choice)  # Ensure this method exists and works as expected
            else:
                typing_effect("You don't have enough gold to order that.")
        else:
            typing_effect("Invalid choice. Please enter a number from the menu.")

def inn(character):
    typing_effect(enter_inn)
    inn_choice = input("Enter the number of the activity you're going to do: ")
    if inn_choice == "1":
        typing_effect(innkeeper_choice_answer)
        inn_room_rent(character)
    elif inn_choice == "2":
        # Code for ordering food from the menu
        typing_effect(innkeeper_choice_answer)
        order_food(character)

        def inn(character):
            typing_effect(enter_inn)
            inn_choice = input("Enter the number of the activity you're going to do: ")
            if inn_choice == "1":
                typing_effect(innkeeper_choice_answer)
                inn_room_rent(character)
            elif inn_choice == "2":
                order_food(character)
            elif inn_choice == "3":
                # Code for buying food to take with you
                typing_effect(innkeeper_choice_answer)
                pass
            else:
                typing_effect("The innkeeper seems not to understand your gibberish, please select a valid option!")
                inn(character)  # Call the inn() function again to prompt for a valid choice
    elif inn_choice == "3":
        # Code for buying food to take with you
        typing_effect(innkeeper_choice_answer)
        pass
    else:
        typing_effect("The innkeeper seems not to understand your gibberish, please select a valid option!")
        inn(character)  # Call the inn() function again to prompt for a valid choice


def player_move_in_village(player):
    typing_effect("Where would you like to go?:")
    for place in village_activities:
        print(place)
        time.sleep(0.5)
    while True:
        choice = input("Enter the number of the activity you're going to do: ")
        if choice == "1":
            inn(player)
            continue
        elif choice == "2":
            # Code for Blacksmith
            animate_message(message)
        elif choice == "3":
            # Code for Flower Shop
            continue
        elif choice == "4":
            # Code for Guild
            continue
        elif choice == "5":
            # Code for Library
            continue
        else:
            typing_effect("Invalid choice. Please enter a number between 1 and 5.")
            continue
