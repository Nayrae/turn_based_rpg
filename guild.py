from animations.dialogue import *
from  quest.quest import *

first_time_enter_guild = """As the guild's ancient doors creak open, a new world of adventure beckons. 
'Welcome, adventurer,' a voice booms, 'to where legends are born.'
"""
enter_guild_text = """You push open the heavy wooden doors and step into the bustling Guild Hall.
      The air is filled with the sounds of clinking glasses, laughter, and the occasional clash of swords as members spar in the corners.
      As you look around, you notice several interesting characters:"""



class Guild:
    def __init__(self, name):
        self.first_time_enter = True
        self.name = name
        self.members = []
        self.quests = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def list_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            print(member)

    def speak_to_people(self):
        print(f"Welcome to {self.name}!")
        print("You can speak to people here and obtain quests.")

    def accept_quest(self, quest):
        self.quests.append(quest)
        print(f"Quest '{quest}' accepted!")

    def enter_guild(self):
        if self.first_time_enter:
            typing_effect(enter_guild_text)
            self.first_time_enter = False
        else:
            guild.speak_to_people()
            guild.list_members()
            print("\nA board on the wall lists the quests that are currently available:")
            guild.list_quests()
            print("\nWho will you speak to first, or will you take on one of the quests listed on the board?")
 
def list_quests(quests):
        print(f"Quests available at {guild.name}:")
        header = f'    {"Number":<10}{"Name":40}{"Description"}'
        number = 0
        print(header)
        print('-' * len(header))
        for quest in quests:
            number += 1
            print(f'    {number:<10}{quest.name:40}{quest.description}')
    
 
guild = Guild("Guild")
guild.add_member("Franco")
guild.add_member("Kuzuma")
guild.add_member("Marika, the receptionist") # i might put the receptionist as the final boss, dont forget this comment #
#guild.speak_to_people()
#guild.accept_quest("Defeat the Dragon")
#guild.accept_quest("Retrieve the Lost Artifact")
#guild.list_quests()

