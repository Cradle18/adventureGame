#---Imports---#
from random import randint

class User():
    #user health, when depletes to 0, game over
    health = 50
    #users inventory, any items found are added to the list.
    inventory = []
    
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    
    #if user takes damage, removes the damage amount from total health.
    def lose_health(self, num):
        self.health = self.health - num
    
    #add to users inventory.
    def add_to_invent(self, item):
        self.inventory.append(item)

    #remove from users inventory.
    def remove_from_invent(self, item):
        self.inventory.remove(item)

    #adds a maximum of 5 health to user and removes potion from invent
    def use_potion(self, item):
        if item in self.inventory and self.health <= 5: #check to see if potion is in invent and health is less than 5, then adds 5 to health.
            self.health += 5
            self.remove_from_invent(item)
        elif item in self.inventory and self.health > 5 or self.health < 10: #same invent check as before, but also check the health if between 5 and 10.
            to_heal = 10 - self.health #10 - current health to work out how much we need to heal by.
            self.health = self.health + to_heal
            self.remove_from_invent(item) 
        else:
            print("You have no potions!")

    #attack funtion to be used in battles, rolls to hit and then selects damage at random.
    def attack(self):
        to_hit = False 
        roll = randint(1,6)
        damage = 0
        if roll > 2:
            to_hit = True
            while to_hit == True:
                #using a try except block just incase any unknown errors happen in the battle.
                try:
                    damage = randint(10,20)
                    print(f"Your attack did {damage} damage to the enemy!")
                    to_hit = False
                except Exception as e:
                    print(f"Oops there was an error {e}")
        else:
            print("Your Attack misses!")
        return damage #this will be used to decline the enemies health.
    
    #block function, user can select to block, rolls for success and then gives a 50/50 chance for counter, which calls the attack function, theres a chance the counter will miss
    def block(self):
        damage = 0
        counter_chance = randint(1,2)
        if counter_chance == 1:
            print("Block success, bonus counter attack!")
            damage = self.attack()
        else:
            print("Block success!")
        return damage
                    
            
    #prints you have died after a health check
    def death(self):
        if self.health <= 0:
            print("You have died!")


"""u1 = User("Tom", "Sword")
u1.attack()
u1.block()"""

