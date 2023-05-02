#scene class setup and any function that will be used inside the class or out.

#---Imports---#
import time


#type writer effect, as if the words are being typed as they are presented
def print_slow(text):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(0.09)
    print()
   
#scene class
class Scene:
    directions = ["left", "right", "forward", "backward"]
    def __init__(self, name):
        self.name = name

class Welcome(Scene):
    def print_welcome(self):
        print("\t\t\t-------------------------------\n")
        print("\t\t\t\tAdventure Game\n")
        print("\t\t\t-------------------------------")

        print_slow("\n\tWELCOME!\n")
        print_slow("Before we begin our adventure, please tell me your name.")
        global user 
        user = input()
        print_slow("Wonderful, a worthy name for a young adventurer!")
        print_slow("Now, what weapon do you carry?")
        global weapon
        weapon = input()
        print_slow(f"Excellent choice {user}, i hope this {weapon} keeps you safe, good luck!......")
        time.sleep(1)
        print_slow(f"\n\t\tWelcome Adventurer {user}!\n\nThe clock has struck midnight let our tale begin.\n")
        

class Part1(Scene):

    def print_part1(self):
        print_slow("The moon is bright and full above, the path before you lit, only by the moons reflection off your armor.")
        print_slow("You are surrounded by high tree's and thick bushes that flank ether side, blocking what you can see through the tree's, the forrest of HIGHRISE growls in the night.")
        print_slow(f"You follow a deralict road which leads towards nothing but darkness, gripping tight your {weapon}, ready for any surprise.")
        

        print_slow(f"\nA noise ahead, a distant roar, you ready your {weapon} as the sound of crashing feet grows closer, do you wish to investigate?(yes/no)")
        inspect_ahead = input()

        if inspect_ahead == "yes":
            captured = Captured("Captured")
            captured.print_captured()
        else:
            lost = Lost("Lost")
            lost.print_lost()
            

class Captured(Scene):
    def print_captured(self):
        print_slow(f"With one hand ready on your {weapon}, you move slowly towards the sound ahead, the thunderous clap hitting the ground getting louder!")
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
        if direction.lower() == self.directions[0]:
            print("skeleton fight")
        elif direction.lower() == self.directions[1]:
            print("skeleton fight")
        elif direction.lower() == self.directions[2]:
            print("trap")
        elif direction.lower() == self.directions[3]:
            print("back to road captured")
        else:
            print("Invalid input!")
            