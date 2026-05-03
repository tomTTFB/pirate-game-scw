from gameclasses import Character
from utils import clearScreen
from enemies import create_enemy
from battle import battle
import time
import pickle
import os
import random

try:
    os.mkdir("saves")
except:
    action = None

clearScreen()
action = input("Start new game (n) or load save (l)? ")

if action == "l":
    clearScreen()
    print("loading game from saves/save.pkl...")
    time.sleep(2)

    try:
        with open("saves/save.pkl", "rb") as file:
            player = pickle.load(file)
            clearScreen()
    except EOFError:
        print("The file is empty or corrupted.")
        exit

elif action == "n":
    clearScreen()
    print("Starting new game...")
    time.sleep(2)

    newGameCreationEnded = 0
    while newGameCreationEnded == 0:
        points = 30

        name = ""
        while len(name.strip()) <= 0:
            name = input("What is your ship's name? ").strip()
            if len(name) == 0:
                print("Ship name cannot be empty. Please try again.")

        try:
            attack = int(input(f"Enter your attack stat ({points} points remaining): "))

            if attack < 0:
                print("Attack stat cannot be negative.")
            elif attack > points:
                print(f"Error: You only have {points} points remaining.")
            else:
                points -= attack

        except ValueError:
            print("Invalid input. Please enter a whole number.")

        try:
            defense = int(input(f"Enter your defense stat ({points} points remaining): "))

            if defense < 0:
                print("Defense stat cannot be negative.")
            elif defense > points:
                print(f"Error: You only have {points} points remaining.")
            else:
                points -= defense

        except ValueError:
            print("Invalid input. Please enter a whole number.")

        try:
            speed = int(input(f"Enter your speed stat ({points} points remaining): "))

            if speed < 0:
                print("Speed stat cannot be negative.")
            elif speed > points:
                print(f"Error: You only have {points} points remaining.")
            else:
                points -= speed

        except ValueError:
            print("Invalid input. Please enter a whole number.")

        if attack <= 0:
            attack = 1
        if defense <= 0:
            defense = 1
        if speed <= 0:
            speed = 1

        if points > 0:
            action = input("You have points left over, restart? (y/N)")
            if action == "y" or "Y":
                clearScreen()
                continue
            elif action == "n" or "N":
                clearScreen()
            elif not action == "y" or "Y" or "n" or "N":
                clearScreen()

        print(f"Final Stats: {attack} ATK | {defense} DEF | {speed} speed")
        action = input("Continue? (y/N)")
        if action == "y" or "Y":
            player = Character(name, 50, 50, attack, defense, speed, "Ocean", 0, 0, 0, 0, 3, 0)
            with open("saves/save.pkl", "wb") as f:
                pickle.dump(player, f)
            newGameCreationEnded = 1
        elif action == "n" or "N":
            clearScreen()
        elif not action == "y" or "Y" or "n" or "N":
            clearScreen()

while player.current_location == "Ocean":
    itemsDone = 1
    clearScreen()
    print("\n")
    print(player)
    print(f"Ship's Inventory: Unstable Gunpower (+ATK): {player.ug} | Reinforced Planks (+DEF): {player.rp} | Rum (+SPD): {player.rum} | Ship Repair Kit (+HP): {player.srk} | Kraken Map: {player.krakenmap}")
    print(f"""\n
        1. Sail around
        2. Scavenge for items
        3. Use items
        4. Save Game
        5. Fight Kraken (End game) (requires Kraken Map)
        \n
        """)
    action = int(input("What will you do? "))

    if action == 1:
        clearScreen()
        print("You sail around and find...")
        time.sleep(2)

        encounterChance = random.randint(1,120)

        if encounterChance >= 1 and encounterChance <= 20:
            # Raft
            print("You found a Raft of pirates, they attack you...")
            time.sleep(2)
            enemy = create_enemy("Raft")
            battle(player, enemy)
            enemy = None
        if encounterChance >= 21 and encounterChance <= 40:
            # Little Boat
            print("You found a Little boat of pirates, they attack you...")
            time.sleep(2)
            enemy = create_enemy("Little Boat")
            battle(player, enemy)
            enemy = None
        if encounterChance >= 41 and encounterChance <= 70:
            encounterChancePirateShip = random.randint(1,80)
            if encounterChancePirateShip >= 1 and encounterChance <= 20:
                # Pirate Ship
                print("You found a pirate ship, they attack you...")
                time.sleep(2)
                enemy = create_enemy("Pirate Ship")
                battle(player, enemy)
                enemy = None
            elif encounterChancePirateShip >= 21 and encounterChance <= 40:
                # Pirate Ship
                print("You found a pirate ship, they appear to lots of cannons...")
                time.sleep(2)
                enemy = create_enemy("Pirate Ship (Well-Armed)")
                battle(player, enemy)
                enemy = None
            elif encounterChancePirateShip >= 41 and encounterChance <= 60:
                # Pirate Ship
                print("You found a pirate ship, their hull seems well armoured...")
                time.sleep(2)
                enemy = create_enemy("Pirate Ship (Fortified)")
                battle(player, enemy)
                enemy = None
            elif encounterChancePirateShip >= 61 and encounterChance <= 80:
                # Pirate Ship
                print("You found a pirate ship, they seem smaller and move quickly...")
                time.sleep(2)
                enemy = create_enemy("Pirate Ship (Nimble)")
                battle(player, enemy)
                enemy = None
        else:
            print("You found nothing...")
            time.sleep(2)

    if action == 2:
        clearScreen()
        print("Scavenger has been sent out to loot...")
        time.sleep(2)
        scavRandom = random.randint(1,10)
        if scavRandom == 1:
            scavRandomPrice = random.randint(3,6)
            action = input(f"Scavenger found Unstable Gunpowder for {scavRandomPrice} gold (buy/pass)?")
            if action == "buy":
                player.ug = player.ug + 1
                player.gold = player.gold - scavRandomPrice
                print(f"Bought Unstable Gunpowder for {scavRandomPrice} gold")
                time.sleep(2)
            if action == "pass":
                action = None
        if scavRandom == 2:
            scavRandomPrice = random.randint(4,5)
            action = input(f"Scavenger found Reinforced Planks for {scavRandomPrice} gold (buy/pass)?")
            if action == "buy":
                player.rp = player.rp + 1
                player.gold = player.gold - scavRandomPrice
                print(f"Bought Reinforced Planks for {scavRandomPrice} gold")
                time.sleep(2)
            if action == "pass":
                action = None
        if scavRandom == 3:
            scavRandomPrice = random.randint(2,5)
            action = input(f"Scavenger found Rum for {scavRandomPrice} gold (buy/pass)?")
            if action == "buy":
                player.rum = player.rum + 1
                player.gold = player.gold - scavRandomPrice
                print(f"Bought Rum for {scavRandomPrice} gold")
                time.sleep(2)
            if action == "pass":
                action = None
        if scavRandom >= 4 and scavRandom <= 7:
            scavRandomPrice = random.randint(3,6)
            action = input(f"Scavenger found Ship Repair Kit for {scavRandomPrice} gold (buy/pass)? ")
            if action == "buy":
                player.srk = player.srk + 1
                player.gold = player.gold - scavRandomPrice
                print(f"Bought Ship Repair Kit for {scavRandomPrice} gold")
                time.sleep(2)
            if action == "pass":
                action = None
        elif scavRandom >= 8 and scavRandom <= 10:
            print("Scavenger found nothing...")
            time.sleep(2)
            clearScreen()

    if action == 3:
        itemsDone = 0
        while itemsDone == 0:
            clearScreen()
            print("Use items:")
            print(f"""\n
            1. Unstable Gunpower (+ATK): {player.ug}
            2. Reinforced Planks (+DEF): {player.rp}
            3. Rum (+SPD): {player.rum}
            4. Ship Repair Kit (+HP): {player.srk}

            E. Exit
            \n
            """)
            action = input("What item will you use? ")

            
            if action == "1":
                player.attack = player.attack + 1
                player.ug = player.ug - 1
                print("Used 1 Unstable Gunpowder")
                time.sleep(1)
                clearScreen()
            if action == "2":
                player.defense = player.defense + 1
                player.rp = player.rp - 1
                print("Used 1 Reinforced Planks")
                time.sleep(1)
                clearScreen()
            if action == "3":
                player.speed = player.speed + 1
                player.rum = player.rum - 1
                print("Used 1 Rum")
                time.sleep(1)
                clearScreen()
            if action == "4":
                player.health = player.health + (random.randint(10,30))
                player.srk = player.srk - 1
                print("Used 1 Ship Repair Kit")
                time.sleep(1)
                clearScreen()
            if action == "E" or "e": 
                itemsDone = 1
            else:
                action = None
        
    if action == 4:
        clearScreen()
        print("Saving Game...")
        with open("saves/save.pkl", "wb") as f:
            pickle.dump(player, f)
        time.sleep(2)
        print("Game Saved")
    
    if action == 5:
        if player.krakenmap == 1:
            print(f"Are you sure you want to fight the kraken? Your save will be deleted if you win")
            action = input("Continue? (y/N)")
            if action == "y" or "Y":
                with open("saves/save.pkl", "wb") as f:
                    pickle.dump(player, f)
                print("You approach the kraken using the map... (saving game)")
                time.sleep(2)
                enemy = create_enemy("💀 The Kraken")
                battle(player, enemy)
                enemy = None
                time.sleep(4)
                clearScreen()
                print("YOU WIN!")
                if os.path.exists("saves/save.pkl"):
                    os.remove("saves/save.pkl")
                    print(f"saves/save.pkl deleted successfully.")
                else:
                        print("The file does not exist.")
                break
            elif action == "n" or "N":
                clearScreen()
            elif not action == "y" or "Y" or "n" or "N":
                clearScreen()
        else:
            print("You don't have the kraken map yet, fight some more enemies!")
            time.sleep(2)
            clearScreen()




    