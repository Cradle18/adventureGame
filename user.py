#---Imports---#

class User():
    #user health, when depletes to 0, game over
    health = 10
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
    
    #prints you have died after a health check
    def death(self):
        if self.health <= 0:
            print("You have died!")

