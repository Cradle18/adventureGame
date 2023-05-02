#---Imports---#
from random import randint

class Monster():
    weapon = ""

    def __init__(self, name) -> None:
        self.name = name

    #deplete health function
    def lose_health(self, num):
        self.health = self.health - num

    #print a death statement for the monster.
    def death(self):
        print(f"{self.name} has died!")

#easy monster class, all easy monters will have random health and weapons generated from the same conditions.
class Monster_Easy(Monster):
    #class variables
    health = randint(1,5) #random health between 1 and 5
    weapon_damage = 2 #sets a value to weapon damage bas one its class
    inventory = []
    
    def __init__(self, name) -> None:
        super().__init__(name)

        #rolls a dice and selects weapon based on dice value.
        dice_roll = randint(1,6) #get a random number to match to a weapon
        if dice_roll >= 1 and dice_roll <= 3:
            self.weapon = "Rusty Sword"
        elif dice_roll >= 4 and dice_roll < 6:
            self.weapon = "Pitch Fork"
        else:
            self.weapon = "Shiny Knife"
        
        self.inventory.append(self.weapon)#stores it to the inventory of the monster.

#hard monster class, larger health poor selection and different weapons.  
class Monster_hard(Monster):
    #class variables
    health = randint(20,30)
    weapon_damage = 5 #sets a value to weapon damage bas one its class
    inventory = []

    def __init__(self, name) -> None:
        super().__init__(name)
        #rolls a dice and selects weapon based on dice value.
        dice_roll = randint(1,6) #get a random number to match to a weapon
        if dice_roll >= 1 and dice_roll <= 3:
            self.weapon = "Longsword"
        elif dice_roll >= 4 and dice_roll < 6:
            self.weapon = "Axe"
        else:
            self.weapon = "Crossbow"
        
        self.inventory.append(self.weapon)#stores it to the inventory of the monster.
        
#---testing---#
m1 = Monster_Easy("Skelebob")
m2 = Monster_hard("Skelechamp")
print(f"My name is {m1.name}\tHealth: {m1.health}")
print(f"I am holding a {m1.weapon}")
print(f"In my bag is:\n{m1.inventory}")
print(m1.death())

print(f"\nMy name is {m2.name}\tHealth: {m2.health}")
print(f"I am holding a {m2.weapon}")
print(f"In my bag is:\n{m2.inventory}")
m2.death()
