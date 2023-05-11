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
        part1 = Part1("Part1")
        part1.print_part1()
        
        

class Part1(Scene):
    def print_part1(self):
        print_slow("The moon is bright and full above, the path before you lit, only by the moons reflection off your armor.")
        print_slow("You are surrounded by high tree's and thick bushes that flank ether side, blocking what you can see through the tree's, the forrest of HIGHRISE growls in the night.")
        print_slow(f"You follow a deralict road which leads towards nothing but darkness, gripping tight your {new_user.weapon}, ready for any surprise.")
        

        print_slow(f"\nA noise ahead, a distant roar, you ready your {new_user.weapon} as the sound of crashing feet grows closer, do you wish to investigate?(yes/no)")
        inspect_ahead = input()

        #if statement to check what the user decides to do, then prints the next scene.
        if inspect_ahead == "yes":
            print_slow(f"With one hand ready on your {new_user.weapon}, you move slowly towards the sound ahead, the thunderous clap hitting the ground getting louder!")
            print("\n'ROAR!'")
            time.sleep(1)
            print("\n'CRASH!'")
            time.sleep(1)
            print_slow("\nNow all you see is black! As you crash into a tree with a 'CRACK!'.")
            print_slow("You lay slumbed, back against a broken a tree, a large shadow approaches over you and slings your lifeless body over it's shoulder and walks off back from where it came.")
            time.sleep(1)
            captured = Captured("Captured")
            captured.print_captured()
        else:
            lost = Lost("Lost")
            lost.print_lost()
            

class Captured(Scene):
    def print_captured(self):
        new_user.lose_health(25)
        print_slow("You awake feeling groggy, a sharp pain banging through your head, your whole body aches.")
        print_slow("While slowly sitting up, you look around and bars of metal suround you, a chain wrapped around one of your legs.")
        print_slow("Conclusion, you are locked in a cage. You sigh and begin to look around for any way out.")
        print_slow("You notice a lock ahead and wonder if you can pick it! Do you wish to attempt your escape? (yes/no)")
        escape_answer = input()
        if escape_answer.lower() == "yes":
            self.__puzzle_1(new_user)
        else:
            print_slow("You decide to roll over and acept your fate, after sometime you notice the smell of burning.")
            print_slow("Suddenly the cage door crashes open and a ogre grabs you by the arm pulling you out of the cage.")
            print_slow("He pulls with such a force but not enough to pull the chain out of the floor with you, you cry out in pain, as your leg tears away from your body and is left behind with the chain.")
            print_slow("You scream out in agony as the orge take you towards the fire, atop sits a cauldron, you realise your mistake.\n")
            new_user.lose_health(50)
            new_user.is_dead()
            
    
    def __puzzle_1(self, user):
        print_slow("You scramble your way over to lock and begin to look it over for any clues on how to unlock it")
        print_slow("You notice strange markings on the side and a roller of numbers along the bottom.")
        print_slow("\nSide: II IV V VII | Roller: |1|2|3|4|\n")
        guesses = 3
        while guesses > 0:
            user_answer = input("Whats your guess?: ")
            if user_answer == "2457":
                break
            else:
                guesses -= 1
            if guesses == 0:
                print_slow("A strange buzzing sound comes from inside the lock!")
                time.sleep(0.5)
                print("\nBANG!\n")
                user.lose_health(50)
                user.is_dead()
                
        
class Lost(Scene):
    def __init__(self, name):
        super().__init__(name)

    def print_lost(self):
        print_slow("You see a gap in the bush to your left and dive through it, landing safely with a role and take cover behind a tree.")
        print_slow("You peer round and look back to the road, the ground shakes, as thunderous footsteeps from the path, pass you by.")
        print_slow("You sigh with relief, knowing that the danger has moved on, as the sound of footsteep disappear of into the distance.")
        print_slow("You turn around and realise that now all you can see is black, no light it peering through tree's, which direction do you wish to take?")
        print("(Left, Right, Forward, Backwards)")
        direction = input()
        if direction.lower() == self.directions[0] or direction.lower() == self.directions[1]:
            self.__skeleton_fight_1(new_user)
        elif direction.lower() == self.directions[2]:
            self.__trap()  
        elif direction.lower() == self.directions[3]:
            print_slow("You head back to where you think you came from and push you way through the branches of the bush.")
            print_slow("You made it! The path is ahead of you again.")
            print_slow("You begin to step forward, when a shadow looms over you.\n")
            new_user.lose_health(25)
            captured = Captured("Captured")   
            captured.print_captured()
            
        else:
            print("Invalid input!")

    def __skeleton_fight_1(self, user):
            print_slow("\nYou turn your head left and then right, you think you can see light, you turn and begin to walk forward.")
            print_slow("After what seems like hours, a little moonlight begins to peer through the tree's ahead and you pick up the pace hoping to reach the path again.")
            print_slow("A rustle from the bush ahead startles you, as two skeletons charge at you with there swords raised\n")
            mons1 = Monster_Easy("Skulldugery")
            mons2 = Monster_Easy("Skelebob")
            battle(user, mons1, mons2)
            print_slow("\nSuccess! You have vanquished your foes, you take a moment to catch your breath and continue to walk ahead to rejoin the path.")
            print_slow("You push through a small gap in the bushes, crawling on your hands and knees, you have made it! Time to pick up where you left off.")
            print_slow("You continue to follow the path, walking at a faster pace than before, after a few minutes you begin to smell something.")
            print_slow("You can smell the burning of flesh and you realise that you are walking right towards it!")
            
    
    def __trap(self):
        print_slow("You begin to walk straight ahead, deeper into the darkness.")
        print_slow("The sounds in the forrest around you begin to disapear and a errie silence falls over you.")
        print_slow("Even the ground beneath you has softened, creating no sounds when you feet touch the ground. The darkness begins to feel like it's tighting around you!")
        print_slow("A sudden CREAK! alerts you, as you feel the ground beneath your feet disapear and the feeling of falling hits.")

        captured = Captured("Captured")   
        captured.print_captured()