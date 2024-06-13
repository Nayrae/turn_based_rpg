from character import Character
from turns import combat
from playsound import playsound


player = Character(input("How do you want to be rememebered?: "), 100, 100, 1, 10)
enemy = Character("Bruhv", 100, 15, 1, 50)
combat(player, enemy)
wait_time = input("")