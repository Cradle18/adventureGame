#scene class setup and any function that will be used inside the class or out.

#---Imports---#
import time
from game_functions.print_slow import print_slow
from user import User
from monster import Monster_Easy, Monster_hard
from battle import battle

new_user = None

#scene class
class Scene:
    directions = ["left", "right", "forward", "backward"]
    def __init__(self, name):
        self.name = name

class Welcome(Scene):
    #start of welcome screen user inputs name and weapon
    def print_welcome(self):
        print("\t\t\t-------------------------------\n")
        print("\t\t\t\tAdventure Game\n")
        print("\t\t\t-------------------------------")

        print_slow("\n\tWELCOME!\n")
        print_slow("Before we begin our adventure, please tell me your name.")
        user = input() #holds users name
        print_slow("Wonderful, a worthy name for a young adventurer!")
        print_slow("Now, what weapon do you carry?")
        weapon = input() #holds user weapon choice
        global new_user
        new_user = User(user, weapon) #instantiates new user with the user and weapon inputs
        new_user.add_to_invent(weapon) #adding sword to inventory 
        print_slow(f"Excellent choice {new_user.name}, i hope this {new_user.weapon} keeps you safe, good luck!......")
        time.sleep(1)
        print_slow(f"\n\t\tWelcome Adventurer {new_user.name}!\n\nThe clock has struck midnight let our tale begin.\n")
        
        

class Part1(Scene):
    def print_part1(self):
        print_slow("The moon is bright and full above, the path before you lit, only by the moons reflection off your armor.")
        print_slow("You are surrounded by high tree's and thick bushes that flank ether side, blocking what you can see through the tree's, the forrest of HIGHRISE growls in the night.")
        print_slow(f"You follow a deralict road which leads towards nothing but darkness, gripping tight your {new_user.weapon}, ready for any surprise.")
        

        print_slow(f"\nA noise ahead, a distant roar, you ready your {new_user.weapon} as the sound of crashing feet grows closer, do you wish to investigate?(yes/no)")
        inspect_ahead = input()

        #if statement to check what the user decides to do, then prints the next scene.
        if inspect_ahead == "yes":
            captured = Captured("Captured")
            captured.print_captured()
        else:
            lost = Lost("Lost")
            lost.print_lost()
            

class Captured(Scene):
    def print_captured(self):
        print_slow(f"With one hand ready on your {new_user.weapon}, you move slowly towards the sound ahead, the thunderous clap hitting the ground getting louder!")
        new_user.lose_health(5)
        print("\n'ROAR!'")
        time.sleep(1)
        print("\n'CRASH!'")
        time.sleep(1)
        print_slow("\nNow all you see is black! As you crash into a tree with a 'CRACK!'.")
        print_slow("You lay slumbed, back against a broken a tree, a large shadow approaches over you and slings your lifeless body over it's shoulder and walks off back from where it came.")

class Lost(Scene):
    def __init__(self, name):
        super().__init__(name)

    def print_lost(self):
        print_slow("You see a gap in the bush to your left and dive through it, landing safely with a role and take cover behind a tree.")
        print_slow("You peer round and look back to the road, the ground shakes, as thunderous footsteeps from the path, pass you by.")
        print_slow("You sigh with relief, knowing that the danger has moved on, as the sound of footsteep disappear of into the distance.")
        print_slow("You turn around and realise that now all you can see is black, no light it peering through tree's, which direction do you wish to take?")
        print("(Left, Right, Forwards, Backwards)")
        direction = input()
        if direction.lower() == self.directions[0] or direction.lower() == self.directions[1]:
            print_slow("\nYou turn your head left and then right, you think you can see light, you turn and begin to walk forward.")
            print_slow("After what seems like hours, a little moonlight begins to peer through the tree's ahead and you pick up the pace hoping to reach the path again.")
            print_slow("A rustle from the bush ahead startles you, as two skeletons charge at you with there swords raised\n")
            mons1 = Monster_Easy("Skulldugery")
            mons2 = Monster_Easy("Skelebob")
            battle(new_user, mons1, mons2)
        elif direction.lower() == self.directions[2]:
            print("trap")
        elif direction.lower() == self.directions[3]:
            print("back to road captured")
        else:
            print("Invalid input!")
            