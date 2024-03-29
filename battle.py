from monster import Monster_Easy, Monster_hard
from user import User
from game_functions.print_slow import print_slow
from random import randint
import time

"""u1 = User("Tom", "Sword")
m1 = Monster_Easy("Skelebob")
m2 = Monster_hard("Skelechamp")"""

#plays the battle
def battle(user, mons1=None, mons2=None):
    #battle status
    battle_on = True
    #initiative
    user.roll_initiative() #roll for initiative to decide turn order
    mons1.roll_initiative()
    #loop to run the battle 
    while battle_on:
        try:
            if user.health > 0 and ((mons1 and mons1.health > 0) or (mons2 and mons2.health > 0)):
                if user.initiative >= mons1.initiative: #checks who has the higher initiative roll
                    battle_menu(user, mons1, mons2)
                    enemies_turn(user, mons1, mons2)
                else:
                    enemies_turn(user, mons1, mons2)
                    battle_menu(user, mons1, mons2)
            else:
                battle_on = False
        except Exception as e:
            print(f"oops an error {e}")

#sets up battle menu and deals with user choices
def battle_menu(user, mons1, mons2):
    if mons1 and mons1.health > 0:
        print("\nEnemy:\t\t\tHealth:\n")
        print(f"{mons1.name}\t\t{mons1.health}\n")
    if mons2 and mons2.health > 0:
        print(f"{mons2.name}\t\t{mons2.health}\n")
    print("---------------------------\n")
    print(f"{user.name}\t\t\t{user.health}\n")
    print_slow(f"{user.name}:(A)to attack | (B)to block | (P)to use a potion | (I)Inventory")
    action_choice = input()
    if action_choice.lower() == "a":
        user_attack(user, mons1, mons2)
    elif action_choice.lower() == "b":
        user_block(user, mons1, mons2)
    elif action_choice.lower() == "p":
        user_use_potion(user)
    elif action_choice.lower() == "i":
        show_inventory(user)
        battle_menu(user, mons1, mons2)

#runs users attacks functions
def user_attack(user, mons1,mons2):
    dead = "" #variable of an empty string to use in place of mons name if mons is dead
    print_slow(f"Attack: {mons1.name if mons1 and mons1.health > 0 else dead} | {mons2.name if mons2 and mons2.health > 0 else dead}") #check is mons alive or dead, then display name or blank
    attack_choice = input()
    if attack_choice.lower() == mons1.name.lower():
        attack = user.attack() #returns damage 
        mons1.lose_health(attack) #takes returned damage and minus of mons health
        mons1.is_dead() #check if mons dead
    elif attack_choice.lower() == mons2.name.lower():
        attack = user.attack()
        mons2.lose_health(attack)
        mons2.is_dead()
    else:
        print("Invalid choice! Try again")

#if user wants to block, creates turn order for monster to attack, then runs the users block method
def user_block(user, mons1, mons2):
    print(f"You raise you {user.weapon} to defend.")
    choose_enemy = 0
    #check is enemies are alive first, then sets turn order based on whose alive
    if mons1.health <= 0: 
        choose_enemy = 2
    elif mons2.health <= 0:
        choose_enemy = 1
    else:
        choose_enemy = randint(1, 2) #sets random turn order if both enemies are alive
    if choose_enemy == 1:
        print(f"{mons1.name} Attacks!")
        user_damage = user.block() #returns damage if counter successful
        mons1.lose_health(user_damage)
        mons1.is_dead() #checks if enemy is dead 
    elif choose_enemy == 2:
        print(f"{mons2.name} Attacks!")
        user_damage = user.block() #returns damage if counter successful
        mons2.lose_health(user_damage)
        mons2.is_dead() #checks if enemy is dead
    else:
        print("Oops an error occurred")

#sends prompts to screen and calls the user use potion method  
def user_use_potion(user):
    used_potion = "You use a potion" if "potion" in user.inventory else ""
    do_not_need_potion = "You don't need that right now"
    print(used_potion if user.health < user.max_health else do_not_need_potion) #prints message bassed on if user needs a potion or not
    user.use_potion("potion")

def show_inventory(user):
    print(f"\n{user.inventory}")

def enemies_turn(user, mons1, mons2):
    if mons1.health > 0:
        damage = mons1.attack()
        user.lose_health(damage)
        user.is_dead()
    if mons2.health > 0:
        damage = mons2.attack()
        user.lose_health(damage)
        user.is_dead()
    
"""user = User("Tom", "Sword")
mons1 = Monster_Easy("Jim")
mons2 = Monster_Easy("Tim")
mons3 = Monster_Easy("Jim")
mons4 = Monster_Easy("Jim")

battle(user, mons1, mons2)"""