from monster import Monster_Easy, Monster_hard
from user import User
from game_functions.print_slow import print_slow

u1 = User("Tom", "Sword")
m1 = Monster_Easy("Skelebob")
m2 = Monster_hard("Skelechamp")

def battle(user, mons1=None, mons2=None):
    battle_on = True
    while battle_on:
        try:
            if user.health > 0 and ((mons1 and mons1.health > 0) or (mons2 and mons2.health > 0)):
                if mons1 and mons1.health > 0:
                    print(f"{mons1.name}\t\t{mons1.health}")
                if mons2 and mons2.health > 0:
                    print(f"{mons2.name}\t\t{mons2.health}")
                print(f"{user.name}\t\t{user.health}")
                print_slow(f"{user.name}:(A)to attack | (B)to block | (P)to use a potion")
                action_choice = input()
                if action_choice.lower() == "a":
                    print_slow(f"Attack: {mons1.name if mons1 and mons1.health > 0 else None} | {mons2.name if mons2 and mons2.health > 0 else None}")
                    attack_choice = input()
                    if attack_choice.lower() == mons1.name.lower():
                        attack = user.attack()
                        mons1.lose_health(attack)
                        if mons1.health <= 0:
                            mons1.death()
                    elif attack_choice.lower() == mons2.name.lower():
                        attack = user.attack()
                        mons2.lose_health(attack)
                        print(mons2.health)
                        if mons2.health <= 0:
                            mons2.death()
                    else:
                        print("Invalid choice! Try again")
                elif action_choice.lower() == "b":
                    pass
                else:
                    pass
            else:
                battle_on = False
        except Exception as e:
            print(f"oops an error {e}")


battle(u1,m1,m2)