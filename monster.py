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
    def is_dead(self):
        if self.health <= 0:
            print(f"{self.name} has died!")

    #rolls a dice and selects weapon based on dice value.
    def weapon_select_easy(self):
        dice_roll = randint(1,6) #get a random number to match to a weapon
        if dice_roll >= 1 and dice_roll <= 3:
            self.weapon = "Rusty Sword"
        elif dice_roll >= 4 and dice_roll < 6:
            self.weapon = "Pitch Fork"
        else:
            self.weapon = "Shiny Knife"
        self.inventory.append(self.weapon)#stores it to the inventory of the monster.

    def weapon_select_hard(self):
        dice_roll = randint(1,6) #get a random number to match to a weapon
        if dice_roll >= 1 and dice_roll <= 3:
            self.weapon = "Longsword"
        elif dice_roll >= 4 and dice_roll < 6:
            self.weapon = "Greatsword"
        else:
            self.weapon = "Crossbow"
        self.inventory.append(self.weapon)#stores it to the inventory of the monster.

#easy monster class, all easy monters will have random health and weapons generated from the same conditions.
class Monster_Easy(Monster):
    #class variables
    health = randint(1,5) #random health between 1 and 5
    weapon_damage = 2 #sets a value to weapon damage bas one its class
    inventory = []
    
    def __init__(self, name) -> None:
        super().__init__(name)
        self.weapon_select_easy()
    
    def attack(self):
        to_hit = False 
        roll = randint(1,6)
        damage = 0
        if roll > 4:
            to_hit = True
            while to_hit == True:
                #using a try except block just incase any unknown errors happen in the battle.
                try:
                    damage = randint(5, 10)
                    print(f"{self.name} attacks!")
                    to_hit = False
                except Exception as e:
                    print(f"Oops there was an error {e}")
        else:
            print(f"{self.name} Attack misses!")
        return damage #this will be used to decline the enemies health.

#hard monster class, larger health poor selection and different weapons.  
class Monster_hard(Monster):
    #class variables
    health = randint(20,30)
    weapon_damage = 5 #sets a value to weapon damage bas one its class
    inventory = []

    def __init__(self, name) -> None:
        super().__init__(name)
        self.weapon_select_hard()
    
    def attack(self):
        to_hit = False 
        roll = randint(1,6)
        damage = 0
        if roll > 3:
            to_hit = True
            while to_hit == True:
                #using a try except block just incase any unknown errors happen in the battle.
                try:
                    damage = randint(10,20)
                    print(f"{self.name} attacks!")
                    to_hit = False
                except Exception as e:
                    print(f"Oops there was an error {e}")
        else:
            print(f"{self.name} Attack misses!")
        return damage #this will be used to decline the enemies health.
        
#---testing---#
"""m1 = Monster_Easy("Skelebob")
m2 = Monster_hard("Skelechamp")
print(f"My name is {m1.name}\tHealth: {m1.health}")
print(f"I am holding a {m1.weapon}")
print(f"In my bag is:\n{m1.inventory}")
m1.death()

print(f"\nMy name is {m2.name}\tHealth: {m2.health}")
print(f"I am holding a {m2.weapon}")
print(f"In my bag is:\n{m2.inventory}")
m2.death()"""
