## TODO
## add Magic system 
## add various magic types
## add at least 2 magics per type
## 

from player_character import *

class Magic:
    def __init__(self, name, magic_type, cost):
        self.name = name
        self.magic_type = magic_type
        self.cost = cost

class FireMagic(Magic):
    def __init__(self, name, cost, damage):
        super().__init__(name, cost, damage) # Call the parent class's constructor
        self.damage = damage # Additional attribute specific to FireMagic
        
class DarkMagic(Magic):
    def __init__(self, name, cost, damage):
        super().__init__(name, cost, damage) 
        self.damage = damage
    
#Sample Spells

fireball = FireMagic("Fireball", 10, 25)
fire_tornado = FireMagic("Fire Tornado", 30, 50)

shamak = DarkMagic("Shamak", 3, 15 )
invisible_slap = DarkMagic("Invisible Slap", 15, 35)

all_spells = [fireball, fire_tornado, shamak, invisible_slap]