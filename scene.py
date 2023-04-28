import time

def print_slow(text, input_mode=False):
    if input_mode:
        return input(text)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)
    print()
    return None

class Scene:
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
        print_slow("The moon is bright and full above, the path before you lit, only by the moons reflection off your armour.")
        print_slow(f"You follow a deralict road which leads towards nothing but darkness, gripping tight your {weapon}, ready for any surprise.")
        print_slow("You are surrounded by high tree's and thick bushes at your side, the forrest of HIGHRISE growls in the night.")

        print_slow(f"\nA noise ahead, a screech and a scratch, you ready your {weapon}, do you wish to investigate?(yes/no)")
        inspect_ahead = input()

        if inspect_ahead.lower == "yes":
            pass
        else:
            pass