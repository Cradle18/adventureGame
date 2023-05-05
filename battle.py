from monster import Monster_Easy, Monster_hard
from user import User
from game_functions.print_slow import print_slow
from random import randint
import time

u1 = User("Tom", "Sword")
m1 = Monster_Easy("Skelebob")
m2 = Monster_hard("Skelechamp")

def battle(user, mons1=None, mons2=None):
    battle_on = True
    while battle_on:
        try:
            if user.health > 0 and ((mons1 and mons1.health > 0) or (mons2 and mons2.health > 0)):
                action_choice = battle_menu(user, mons1, mons2)
                if action_choice.lower() == "a":
                    user_attack(user, mons1, mons2)
                elif action_choice.lower() == "b":
                    user_block(user, mons1, mons2)
                elif action_choice.lower() == "p":
                    user_use_potion(user)
                else:
                    print("Error")
                damage  = mons1.attack()
                user.lose_health(damage)
                user.is_dead()
                damage2 = mons2.attack()
                user.lose_health(damage2)
                user.is_dead()
            else:
                battle_on = False
        except Exception as e:
            print(f"oops an error {e}")

def battle_menu(user, mons1, mons2):
    if mons1 and mons1.health > 0:
        print("\nEnemy:\t\t\tHealth:\n")
        print(f"{mons1.name}\t\t{mons1.health}\n")
    if mons2 and mons2.health > 0:
        print(f"{mons2.name}\t\t{mons2.health}\n")
    print("---------------------------\n")
    print(f"{user.name}\t\t\t{user.health}\n")
    print_slow(f"{user.name}:(A)to attack | (B)to block | (P)to use a potion")
    action_choice = input()
    return action_choice

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
    
def user_use_potion(user):
    used_potion = "You use a potion"
    do_not_need_potion = "You don't need that right now"
    print(used_potion if user.health < user.max_health else do_not_need_potion)
    user.use_potion("potion")

battle(u1,m1,m2)