## TODO                                                 ##                        
## add weapons(with respective damage)                  ##    
## add more enemies                                     ##
## add more playable characters                         ##
## dont forget to make sure that turns work decently    ##                    
## add an enemy class(dont forget about other. method)  ##
## add target choice                                    ##

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self, other):
        other.health -= self.damage
        print(f'{self.name} has dealt a total of {self.damage} DMG to {other.name}')
    
    def is_alive(self):
        return self.health > 0
    
    def game_loop(player, enemy):
        while player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(player)
            else:
                print(f'{enemy.name} has been defeated!')
                break
            if not player.is_alive():
                print(f'{player.name} has died!')
                
player = Character("Tomare", 100, 20)
enemy = Character("Goblin", 50, 15)