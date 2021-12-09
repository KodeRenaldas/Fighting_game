import random

class player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        #generate random num for base, light, heavy attack (currently disabled)
        self.normal_attack = 10 #random.randint(10,40)
        self.normal_attack_max = 40
        self.light_attack =  20 #random.randint(20,30)
        self.light_attack_max = 30
        self.heavy_attack = 10 #random.randint(10,100)
        self.heavy_attack_max = 100
        self.pots = 3
        self.wins = 0
playerIG = player("player")
class monster:
    def __init__(self, monstername):
        self.name = monstername
        self.maxhealth = random.randint(10,100)
        self.health = self.maxhealth
        #generate random number for normal attack, might add random chance for heavy or light attack
        self.normal_attack = 10 #random.randint(10,30)
        self.normal_attack_max = 30
monsterIG = monster("monster")
#randomevent class / random chances for something to happen
class randevent:
    def __init__(self,randomevent):
        self.chance_for_potion = 1
        self.chance_for_potion_max = 100
randeventvar = randevent("randevent")
#declaring your current stats, and asks if you are ready or not to fight, else exit()
def start1():
    print (f"Name: {playerIG.name}")
    print (f"Potions: {playerIG.pots}")
    print (f"Health: {playerIG.health}")
    print ("Are you ready to fight?")
    print ("1 for yes, 2 for no")
    option = input(":")
    if option == "1":
        fight()
    else:
        exit()
#declares the fight, difference in stats
def fight():
    print(f"{playerIG.name} vs {monsterIG.name}")
    print (f"{playerIG.name}'s {playerIG.health} {playerIG.maxhealth}  {monsterIG.name}'s {monsterIG.health} {monsterIG.maxhealth}")
    attack()
#declares the attack sequence
def attack():
    print (f"1 for normal attack, 2 for light attack, 3 for heavy attack, 4 to drink a potion")
    #declaring how much damage each attack does
    playeratk_normal = random.randint(playerIG.normal_attack, playerIG.normal_attack_max)
    playeratk_light = random.randint(playerIG.light_attack, playerIG.light_attack_max)
    playeratk_heavy = random.randint(playerIG.heavy_attack, playerIG.heavy_attack_max)
    monsteratk_normal = random.randint(monsterIG.normal_attack, monsterIG.normal_attack_max)
    option = input(" ")
    if option == "1":
    #normal attack
        monsterIG.health -= playeratk_normal 
        print (f"you deal {playeratk_normal} damage")
    elif option == "2":
    #light attack
        monsterIG.health -= playeratk_light
        print (f"you deal {playeratk_light} damage")
    elif option == "3":
    #heavy attack
        monsterIG.health -= playeratk_heavy
        print (f"you deal {playeratk_heavy} damage")
    elif option == "4":
    #drink potion
        drinkpot()
    if monsterIG.health <= 0:
        victory()
    #not using if for this(NEEDS WORKS, where to place best?)
    playerIG.health -= monsteratk_normal
    if playerIG.health <= 0:
        defeat()
    else:
        fight()


def drinkpot():
    if playerIG.pots == 0:
        print ("No more potions left")
    else:
        playerIG.health += 50
        playerIG.pots -= 1
        if playerIG.health >= playerIG.maxhealth:
            playerIG.health = playerIG.maxhealth
        print (f"You drink a potion, you have {playerIG.pots} left")
        fight()
#declaring victory
def victory():
    monsterIG.health = monsterIG.maxhealth
    playerIG.wins += 1
    drop_chance_pot = random.randint(randeventvar.chance_for_potion, randeventvar.chance_for_potion_max)
    if drop_chance_pot <= 50:
        playerIG.pots += 1
        print (f"The monster you slain, dropped a health potion, you have {playerIG.pots} left")
    print (f"You defeated {monsterIG.name}")
    print(f"Debug for potion drop {drop_chance_pot}")
    #print (f"You defeated {playerIG.wins} in total")
#when you die
def defeat():
    print("You have died")
    exit()
start1()