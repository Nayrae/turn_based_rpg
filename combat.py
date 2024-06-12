import random 
#let's start with a player class
class player():
    def __init__(self): #and here i put the stats down
        self.hp = 100
        self.dmg = 10
        self.block = -5
        self.heal = 5

    def combat(self, action, enemy): #this is kinda messy, here's what the different actions do, plus i added a d3 roll for crits or failures
        match action:
            case 1:
                d3 = random.randint(1, 3)
                if d3 == 1:
                    self.hp -= self.dmg
                    print("\nYou're too high and accidentally hit yourself")
                
                if d3 == 3:
                    enemy.hp -= self.dmg*2
                    print("\nYou feel a sudden burst of power coming from yourself, you rush against the monster dealing a total of ", self.dmg*2," dmg!")
                
                elif d3 == 2:
                    print("\nYou attack the monster")
                    enemy.hp -= self.dmg
                    
            case 2: 
                enemy.dmg -= self.block
                print("\nYou block it's attack for a total of ", self.block, " reduced damage")
            case 3:
                self.hp += self.heal
                print("\nYou heal yourself for a total of ", self.heal, " hp")
            
        print("\nenemy current hp = ", enemy.hp,"\nyour current hp = ", self.hp) #always print the hps after the actions 

class enemy():
    def __init__(self, choice):#same things for the exception of choice(random number from 1 to 3)
        self.hp = 100
        self.dmg = 10
        self.block = -5
        self.heal = 5
        self.choice = choice

    def combat(self, player):
        if self.choice == 1:
            d3 = random.randint(1, 3)
            if d3 == 1:
                self.hp -= self.dmg
                print("\nIt's too high and accidentally hit itself")
                
            if d3 == 3:
                player.hp -= self.dmg*2
                print("\nIt feels a sudden burst of power coming from itself, it rushes against the you dealing a total of ", self.dmg*2," dmg!")

            elif d3 == 2:
                print("\nThe monster attacks you")
                player.hp -= self.dmg
            
        elif self.choice == 2: 
            player.dmg -= self.block
            print("\nIt blocks your attack for a total of ", self.block, " reduced damage")
        elif self.choice == 3:
            self.hp += self.heal
            print("\nIt heals itself for a total of ", self.heal, " hp")

        print("\nenemy current hp = ", self.hp,"\nyour current hp = ", player.hp)

        


action = int(input("\nWhat would you like to do?   1 = ATK   2 = BLOCK   3 = heal\f")) #first action goes to the player
while action == "" or action == " ":
    action = input("Invalid input. Please enter a valid action: ")
    
action = int(action)
choice = random.randint(1, 3)    

p = player() #stick value to player class
e = enemy(choice) #stick value to enemy class

while p.hp > 0 and e.hp > 0:
    p.combat(action, e)
    e.combat(p)
    if p.hp <= 0:
        print("You Died!")
        break
    elif e.hp <= 0: 
        print("You Won!")
        break
    action = input("\nWhat would you like to do?:   1 = ATK   2 = BLOCK   3 = heal\f")#keeps asking 'till one dies
    while action == "" or action == " ":
        action = input("Invalid input. Please enter a valid action: ")
    action = int(action)
    choice = random.randint(1, 3)#random choice everytime
    e.choice = choice