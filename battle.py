from gameclasses import Character
from enemies import create_enemy
from utils import clearScreen
import random
import time

def calc_damage(attacker, enemy):
    multiplier = random.uniform(0.75, 1.25)
    damage = attacker.attack - (enemy.defense / 2) * multiplier
    damage = max(0, damage)
    return int(round(damage))

def battle(player, enemy):
    activebattle = 1
    exposedMessage = 0
    while activebattle == 1:

        clearScreen()
        print("\n")
        print(player)
        print("\n")
        if enemy.health <= (enemy.max_hp * 0.2):
            print(enemy)
        else:
            enemy.enemystats()
        print("\n")
        action = input("Attack (a) or use items (i)? ")
        
        if action == "a":
            if player.speed > enemy.speed:
                clearScreen()
                time.sleep(0.5)
                print("You outsped the enemy ship!")
                print("\n")
                damage = calc_damage(player, enemy)
                enemy.take_damage(damage)
                print(f"{enemy.name} lost {damage} health!")
                time.sleep(1)
                damage = calc_damage(enemy, player)
                player.take_damage(damage)
                print(f"you lost {damage} health!")
                input("Press ENTER to continue...")

            if enemy.speed > player.speed:
                clearScreen()
                time.sleep(0.5)
                print("The Enemy Ship outsped you!")
                print("\n")
                damage = calc_damage(enemy, player)
                player.take_damage(damage)
                print(f"you lost {damage} health!")
                time.sleep(1)
                damage = calc_damage(player, enemy)
                enemy.take_damage(damage)
                print(f"{enemy.name} lost {damage} health!")
                input("Press ENTER to continue...")

            if player.speed == enemy.speed:
                speedtest = random.randint(0,1)
                if speedtest == 0:
                    clearScreen()
                    time.sleep(0.5)
                    print(f"You both moved at the same time, but {enemy.name} shot first!")
                    print("\n")
                    damage = calc_damage(enemy, player)
                    player.take_damage(damage)
                    print(f"you lost {damage} health!")
                    time.sleep(1)
                    damage = calc_damage(player, enemy)
                    enemy.take_damage(damage)
                    print(f"{enemy.name} lost {damage} health!")
                    input("Press ENTER to continue...")
                elif speedtest == 1:
                    clearScreen()
                    time.sleep(0.5)
                    print(f"You both moved at the same time, but you shot first!")
                    print("\n")
                    damage = calc_damage(player, enemy)
                    player.take_damage(damage)
                    print(f"you lost {damage} health!")
                    time.sleep(1)
                    damage = calc_damage(enemy, player)
                    enemy.take_damage(damage)
                    print(f"{enemy.name} lost {damage} health!")
                    input("Press ENTER to continue...")

        if enemy.health <= (enemy.max_hp * 0.2) and exposedMessage != 1:
            exposedMessage = 1
            print(f"{enemy.name} had their stats exposed!")
            time.sleep(2)

        if player.health <= 0:
            clearScreen()
            print("You Died, Returning to main menu")
            time.sleep(4)
            activebattle = 0
            clearScreen()
            return()
        elif enemy.health <= 0:
            clearScreen()
            earnedgold = enemy.gold * random.uniform(0.5,1)
            earnedgold = int(round(damage))
            print(f"You defeated {enemy.name} and stole {earnedgold} gold!")

            levelupChance = random.randint(5,11)

            if levelupChance >= 5 and levelupChance <= 7:
                attackGained = random.randint(2,6)
                player.attack = player.attack + attackGained
                print(f"You gained +{attackGained} attack from the battle")
                time.sleep(3)
            if levelupChance >= 8 and levelupChance <= 9:
                defenseGained = random.randint(1,3)
                player.defense = player.defensek + defenseGained
                print(f"You gained +{defenseGained} defense from the battle")
                time.sleep(3)
            if levelupChance >= 10 and levelupChance <= 11:
                speedGained = random.randint(2,4)
                player.speed = player.speed + speedGained
                print(f"You gained +{speedGained} attack from the battle")
                time.sleep(3)
            
            if player.krakenmap == 0:
                krakenMapChance = random.randint(1,50)
                if krakenMapChance == 50:
                    player.krakenmap = 1

            activebattle = 0
            return()