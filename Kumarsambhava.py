"""
कुमारसंभव (KUMARA-SAMBHAVA):- The Birth of War God

Realms/Factions

1) Kshatriyas (kshuh-tree-yuh): Highly intelligent but cynical species from deccan plains. Capable of greatness!
                                Can forge great weapons and tools, and use opponent's weakness to their advantage.

2) Parvateshwaras (Perva-tehsh-wara): The mountain people, brave warriors from the himalayan mountain ranges: the land of mist and snow.
                      Parvateshwaras are known to be the only species capable of taming dragons!
                      As per old vedic myth, they are dragonborn.

3) Rakshasas(Rakh-sha-sa): The forest dwelling, extremely powerful, a-sura(devil) worshipping species. Counter-force to Kshatriyas
                    and Parvateshwaras

"""
import random as random
import math as math
import copy as copy
from urllib.request import urlopen
from PIL import Image

# Loading Image for final final outcome
img = Image.open(urlopen('https://i.imgur.com/hL8QuOw.jpg'))

# Global Variables
FACTIONS = ['Kshatriyas', 'Parvateshwaras']
KASHATRIYAS = {'Hero': {'Strength': 5, 'Health': 15, 'Intellect': 7},'Foot Soldier': {'Strength': 2, 'Health': 10, 'Intellect': 2}, 'Foot Soldier 2': {'Strength': 2, 'Health': 10, 'Intellect': 2}}
PARVATESHWARAS = {'Hero': {'Strength': 7, 'Health': 15, 'Intellect': 5},'Archer': {'Strength': 3, 'Health': 10, 'Intellect': 1},'Archer 2': {'Strength': 3, 'Health': 10, 'Intellect': 1}}
WOLF = {'Alpha': {'Strength': 3, 'Health': 15 }, 'Omega':{'Strength': 2, 'Health': 10},  'Omega 2':{'Strength': 2, 'Health': 10}}
GRIFFIN = {'Griffin': {'Strength': 6, 'Health':35 }}
DRAGON = {'Dragon': {'Strength': 7, 'Health': 45}}
GIANT = {'Giant': {'Strength': 7, 'Health': 45}}
RAKSHASA = {'Narakasura': {'Strength': 8,'Health': 60}}
FOOD = 25
STATES = ["healthy", "slightly wounded", "getting weaker", "near defeat" ]
MERCY = 0
GAME_STATUS = True

def main():

    # If status turns false game is over, the function should end
    intro_text()
    faction_choice = int(check_input(input("Enter value: "),'faction'))
    choice = FACTIONS[faction_choice]
    q1_list = quest_1(choice)
    team = q1_list[0]
    food = q1_list[1]
    status = q1_list[2]
    if status == False:
        return
    optional_quest = get_opt_quest()
    q2_list = quest_2(choice,optional_quest,team,food)
    team = q2_list[0]
    food = q2_list[1]
    mercy = q2_list[2]
    status = q2_list[3]
    if status == False:
        return
    q3_list = quest_3(choice,team,mercy,food)
    team = q3_list[0]
    food = q3_list[1]
    mercy = q3_list[2]
    status = q3_list[3]
    dragon_status = q3_list[4]
    if status == False:
        return
    status = quest_4(choice,team,mercy,food,dragon_status)
    if status == False:
        return
    outro_text()

def intro_text():

    print("")
    print("\033[1mWelcome to कुमारसंभव(KUMARA-SAMBHAVA): The Birth of War God." + " A text based Action RPG game set in Treta Yuga: The Age of Triad. \033[0m")
    print("")
    print("")
    print("The Kshatriyas and Parvateshwaras are at a war with Rakshasas. After a bitter defeat at the hands of Rakshasas.")
    print("Both Kshatriyas and Parvateshwaras have lost their stronghold in central and western region and are forced to retreat their forces.")
    print("Kshatriyas and Parvateshwaras have decided to take the fight to Asarta-van: The decayed forest. Home of Rakshasas!")
    print("")
    print("Rules:")
    print("1) This is a turn based game, you go first.")
    print("2) You may either attack, defend or may restore health in a turn.")
    print("3) If the hero dies, it's Game Over!!")
    print("4) The opponent can only attack, being a wild creature. Also due to limitations of noob programmer, living in his mother's basement.")
    print("5) Intelligence determines how well you can attack or defend against an opponent.")
    print("")
    print("Note: Please expand your terminal/console to full-screen for a better experience!")
    print("")
    print("Choose your faction:")
    print("0) Kshatriyas(Kshuh-tree-yuh): Highly intelligent but cynical species from deccan plains. Human beings are considered to be descendants of Kashatriyas.")
    print("1) Parvateshwaras(Perva-tehsh-wara): Brave warriors from the himalayan mountain ranges: As per old vedic myth, they are dragonborn.\n")

def quest_1(x):

    print("")
    if x == FACTIONS[0]:
        org_team = KASHATRIYAS
    else:
        org_team = PARVATESHWARAS
    team_list = list(org_team.keys())

    # Quest Intro Text
    print("Your Team is "+ x + ".")
    print("You have a Hero in your team with starting Strength: "+ str(org_team['Hero']['Strength']) + ", Heath:" , org_team['Hero']['Health'], "and Intellect:" , org_team['Hero']['Intellect'])
    print("Along with your Hero, you have 2 " + team_list[1] + "s." + " With Strength: " + str(org_team[team_list[1]]['Strength']) +", Health: " + str(org_team[team_list[1]]['Health']) + " and Intellect: " + str(org_team[team_list[1]]['Intellect']) + " each.")
    print("")
    print("Your team has been camping for the night in Arakoo valley. Low on food supplies, your " + team_list[1] + " goes looking for some berries and wild animals to hunt.")
    print("It's been a while since the " + team_list[1] + " left. You and the other " + team_list[1] + " decide to go and check.")
    print("In the distance you hear a wolf howling. You trace footsteps of your missing " + team_list[1] + ".")
    print("You find that he is surrounded by a pack of ravenous wolves and is wounded..\n")

    # Calculated values needed for progression, deep copy prevents alteration to original file
    team = copy.deepcopy(org_team)
    wolf = WOLF
    org_wolf = copy.deepcopy(wolf)

    max_thealth_q1 = 0
    for key in org_team:
        max_thealth_q1 += org_team[key]['Health']

    max_opp_health = 0
    for key in org_wolf:
        max_opp_health += org_wolf[key]['Health']

    # Since team mate got wounded
    team[team_list[2]]['Health'] -= 2

    # Updated team health
    team_health = team[team_list[0]]['Health'] + team[team_list[1]]['Health'] + team[team_list[2]]['Health']
    pack_health = org_wolf['Alpha']['Health'] + org_wolf['Omega']['Health'] + org_wolf['Omega 2']['Health']
    wolf_state = STATES[0]
    food = FOOD
    defence_state = False

    print("Your hero is at " + str(team['Hero']['Health']) + " health. The " + team_list[1] + "s" + " are at " + str(
        team[team_list[1]]['Health']) + " and " + str(team[team_list[2]]['Health']) + " respectively.")
    print("Current food supplies are at " + str(food))
    print("While the pack of wolves appears to be " + wolf_state + ".\n")

    # Both teams need to be alive for game to continue
    while team_health > 0 and pack_health > 0:
        print("You 0) Attack 1) Defend 2) Restore Health")
        choice = check_input(input("Enter number: "), 'combat')
        # Combat is designed to hit last player in team first. i.e. foot soldier 2 or archer 2
        # No of health points to be restored cannot be more than food supplies or more than amount of hit taken from max health
        if choice == 2 and team_health < max_thealth_q1 and food >= 1:
            difference = max_thealth_q1 - team_health
            print("Teams health is low by " + str(difference) + ". Your food supplies are at " + str(food))
            food_choice = check_input(input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            while food_choice > food or food_choice > difference or food_choice <= 0:
                print("Invalid input! Your food supplies are at " + str(food) + ".")
                print("You can only restore your health by " + str(difference) + ".")
                food_choice = check_input(input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            output = health_choice(team, food_choice, food, team_health, org_team)
            food = output[0]
            team_health = output[1]
            print("Food resources at: " + str(food))
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Team health is at " + str(team_health))
        elif choice == 2 and team_health == max_thealth_q1 or food == 0:
            while choice == 2:
                print("Team already at full health or No food left. Choose again!")
                choice = check_input(input("Enter number: "), 'combat')
        if choice == 1:
            print("You raise your shield and brace for next attack!")
            defence_state = True
        if choice == 0:
            team_attack = attack(team)
            pack_health = health_status(team_attack,pack_health,wolf)
            print_status(pack_health,max_opp_health,update_opp(wolf))
        opponent_attack = attack_opp(defence_state,team,wolf)
        # Prevent printing of 0 attack in case opponent died by last hit from team
        if pack_health > 0:
            print("")
            print("The Alpha leading the charge leaps at your team..")
            print("Hits you with a "+ str(opponent_attack) + " point attack!")
        team_health = health_status(opponent_attack,team_health,team)
        update_team(team)
        # Changing to default state in case user uses defence in their turn
        defence_state = False
        print("")
        # Max health can change as team members can die in combat, total possible max health would reduce after that
        max_thealth_q1 = 0
        for key in team:
            max_thealth_q1 += org_team[key]['Health']
        if team_health > 0:
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Your food supplies are at " + str(food))
    if team_health == 0:
        print("GAME OVER!! Start again")
        game_status = False
    if pack_health == 0:
        print("")
        print("You've managed to take down the Pack of Wolves!")
        print("You salvage raw meat and few items, your food supplies are up by 20!")
        print("The hero has gained experience points, intelligence is up by 1 point!")
        print("The pack of wolf was also guarding a cursed oil, you apply it to your blade, damage is up by 1!")
        team['Hero']['Intellect'] += 1
        team['Hero']['Strength'] += 1
        food += 20
        game_status = True
    return [team,food, game_status]

def quest_2(team_choice,choice,team,food):

    if team_choice == FACTIONS[0]:
        org_team = KASHATRIYAS
    else:
        org_team = PARVATESHWARAS

    #Getting necessary variables
    org_griffin = GRIFFIN
    griffin = copy.deepcopy(org_griffin)

    #Necessary Calculations
    max_thealth_q2 = 0
    for key in team:
        max_thealth_q2 += org_team[key]['Health']
    max_opp_health = org_griffin['Griffin']['Health']

    team_health = 0
    for key in team:
        team_health += team[key]['Health']
    griffin_health = griffin['Griffin']['Health']
    food = food
    defence_state = False
    # In case player chooses to help
    if choice == 0:
        mercy = MERCY
        mercy += 1
        print("")
        print("Your team reaches the village, the hero speaks to the farmers and gets to know more about the Griffin.")
        print("The frequency of its raids, time of attack and it's favourite animal to hunt..")
        print("Based on the given info, your team plans to lure the Griffin in an open field with a bait.")
        print("They tie a sheep to a pole and wait for the Griffin to attack at dusk!")
        print("")
        print("Hero is woken up by a loud screech..Up in the sky griffin is circling over the sheep!")
        print("The team readies itself, shoots some arrow at the Griffin, try to get its attention.")
        print("Griffin now swoops down, swiftly approaching your team.. ")
        print("")
        for key in team:
            print("Your " + key + " is at health: " + str(team[key]['Health']))
        print("Your food supplies are at " + str(food))
        while team_health > 0 and griffin_health > 0:
            print("You 0) Attack 1) Defend 2) Restore Health")
            choice = check_input(input("Enter number: "), 'combat')
            if choice == 2 and team_health < max_thealth_q2 and food >= 1:
                difference = max_thealth_q2 - team_health
                print("Teams health is low by " + str(difference) + ". Your food supplies are at " + str(food))
                food_choice = check_input(input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
                while food_choice > food or food_choice > difference or food_choice <= 0:
                    print("Invalid input! Your food supplies are at " + str(food) + ".")
                    print("You can only restore your health by " + str(difference) + ".")
                    food_choice = check_input(input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "),'food_choice')
                output = health_choice(team, food_choice, food, team_health, org_team)
                food = output[0]
                team_health = output[1]
                print("Food resources at: " + str(food))
                for key in team:
                    print("Your " + key + " is at health: " + str(team[key]['Health']))
                print("Team health is at " + str(team_health))
            elif choice == 2 and team_health == max_thealth_q2 or food == 0:
                while choice == 2:
                    print("Team already at full health or No food left. Choose again!")
                    choice = check_input(input("Enter number: "), 'combat')
            if choice == 1:
                print("You raise your shields and brace for next attack!")
                defence_state = True
            if choice == 0:
                team_attack = attack(team)
                griffin_health = health_status(team_attack, griffin_health, griffin)
                print_status_opp('Griffin',griffin_health, max_opp_health, update_opp(griffin))
            opponent_attack = attack_opp(defence_state, team, griffin)
            if griffin_health > 0:
                print("")
                print("The Griffin flies down, stretches its claws and attacks..")
                print("Hits you with a " + str(opponent_attack) + " point attack!")
            team_health = health_status(opponent_attack, team_health, team)
            update_team(team)
            defence_state = False
            print("")
            max_thealth_q2 = 0
            for key in team:
                max_thealth_q2 += org_team[key]['Health']
            if team_health > 0:
                for key in team:
                    print("Your " + key + " is at health: " + str(team[key]['Health']))
                print("Your food supplies are at " + str(food))
        if team_health == 0:
            print("GAME OVER!! Start again")
            game_status = False
        if griffin_health == 0:
            print("")
            print("Down with the swing of the blade!! The Griffin is dead...")
            print("The hero has gained experience points, intelligence is up by 1 point!")
            print("You forge a knife from Griffin claws and bones, damage is up by 1!")
            print("You take raw meat of Griffin, food supplies up by 20!")
            print("")
            team['Hero']['Intellect'] += 1
            team['Hero']['Strength'] += 1
            food += 20
            print("Villagers thank you for your bravery and are indebted to you and your clan!")
            print("As a token of gratitude, the villagers offer your their last supply of food")
            print("")
            print("Take food worth 30 points!?")
            print("0) NO! You never did it for money/food. A village of 20 people needs food more than you do!")
            print("1) YES! You might need later while facing other uncertainties!")
            take_food = check_input(input("Enter number: "), 'quest')
            if take_food == 1:
                food += 30
            else:
                mercy += 1
                print("")
                print("The villagers are humbled by your act! Seeing your altruism, the village sage approaches you...")
                print("He warns you about an impending danger.. you'll come across a giant creature before you reach Asarta-van")
                print("The creature possesses massive source of knowledge..He advises you not to kill the creature!")
            game_status = True
        return [team, food,mercy,game_status]

    #Without help, we'd return all variables as is
    elif choice == 1:
        return [team,food,0,True]

def quest_3(team_choice,team,mercy,food):

    mercy = mercy
    if team_choice == FACTIONS[0]:
        org_team = KASHATRIYAS
        org_opponent = DRAGON
    else:
        org_team = PARVATESHWARAS
        org_opponent = GIANT

    #Getting necessary variables

    opponent = copy.deepcopy(org_opponent)

    #Necessary Calculations
    max_thealth_q3 = 0
    for key in team:
        max_thealth_q3 += org_team[key]['Health']
    for key in org_opponent:
        max_opp_health = org_opponent[key]['Health']

    team_health = 0
    for key in team:
        team_health += team[key]['Health']
    for key in opponent:
        opponent_health = opponent[key]['Health']

    food = food
    defence_state = False
    opp_name = list(opponent.keys())[0]
    print("")
    print("Your team is entering the forest..")
    print("As you find your way across the decayed forest you come across a huge cave at the base of a mountain.")
    print("You hear an ominous voice coming from the inside. A " + opp_name + " emerges from the cave.")
    print("'You cannot go beyond this point!' exclaimed the " + opp_name + ". He has been enslaved to Rakshasas for past 900 years.")
    print("Without fighting the " + opp_name + " you cannot proceed into the forest!")
    print("The final challenge before facing off with the head of Rakshasa clan!")
    print("")
    for key in team:
        print("Your " + key + " is at health: " + str(team[key]['Health']))
    print("Your food supplies are at " + str(food))

    # To introduce last choice in the quest, we work with last 25% of opponent health
    while team_health > 0 and opponent_health > 0.25 * max_opp_health:
        print("You 0) Attack 1) Defend 2) Restore Health")
        choice = check_input(input("Enter number: "), 'combat')
        if choice == 2 and team_health < max_thealth_q3 and food >= 1:
            difference = max_thealth_q3 - team_health
            print("Teams health is low by " + str(difference) + ". Your food supplies are at " + str(food))
            food_choice = check_input(
                input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            while food_choice > food or food_choice > difference or food_choice <= 0:
                print("Invalid input! Your food supplies are at " + str(food) + ".")
                print("You can only restore your health by " + str(difference) + ".")
                food_choice = check_input(
                    input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            output = health_choice(team, food_choice, food, team_health, org_team)
            food = output[0]
            team_health = output[1]
            print("Food resources at: " + str(food))
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Team health is at " + str(team_health))
        elif choice == 2 and team_health == max_thealth_q3 or food == 0:
            while choice == 2:
                print("Team already at full health or No food left. Choose again!")
                choice = check_input(input("Enter number: "), 'combat')
        if choice == 1:
            print("You raise your shields and brace for next attack!")
            defence_state = True
        if choice == 0:
            team_attack = attack(team)
            opponent_health = health_status(team_attack, opponent_health, opponent)
            print_status_opp(opp_name,opponent_health, max_opp_health, update_opp(opponent))
        print("")
        if opponent_health > 0.25 * max_opp_health and opp_name == 'Dragon':
            # Prevents attack after opponent's health has reduced to given level
            opponent_attack = attack_opp(defence_state, team, opponent)
            print("The Dragon swoops down, breathing fire and melting everything in it's path.. ")
            print("Hits you with a " + str(opponent_attack) + " point attack!")
            team_health = health_status(opponent_attack, team_health, team)
            update_team(team)
        elif opponent_health > 0.25 * max_opp_health and opp_name == 'Giant':
            # Prevents attack after opponent's health has reduced to given level
            opponent_attack = attack_opp(defence_state, team, opponent)
            print("The Giant swings it's blade, and throws a boulder at you..")
            print("Hits you with a " + str(opponent_attack) + " point attack!")
            team_health = health_status(opponent_attack, team_health, team)
            update_team(team)
        defence_state = False
        print("")
        max_thealth_q3 = 0
        for key in team:
            max_thealth_q3 += org_team[key]['Health']
        if team_health > 0:
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Your food supplies are at " + str(food))
    if team_health == 0:
        print("GAME OVER!! Start again")
        game_status = False
        dragon_status = False
    else:
        print("")
        print("The " + opp_name + " falls on the ground..gasping for breath is near death..")
        print(opp_name + " has just been a pawn to the Rakshasas and has been enslaved to them!")
        print(opp_name + " was tricked by conniving members of Rakshasas clan. Forced to serve them..Pleads for mercy.")
        print("0) You give the creature another chance to start over and show mercy!")
        print("1) You kill it!! Their kind can't be trusted")
        q3_choice = check_input(input("Enter number: "), 'quest')
        if q3_choice == 0 and opp_name == 'Dragon':
            print("")
            print("The dragon surprised by kindness from your kind.. Tells that your clan and Parvateshwaras have spent decades mistrusting each other..")
            print("But are not so different after all.. eons ago a group of brave warriors went on a mission to slay the Golden Dragon for the bounty on it's head.")
            print("Only one person survived and returned without the dragon's head! The person came to be the founder of the clan you now know as Parvateshwaras: The dragonborns!")
            print("Dragon slits your wrists with his claws and falls on the ground..dead!")
            print("An aura with reddish hue surrounds the dragon and the hero. Lifting them off the ground.")
            print("The dragon vanishes and the hero falls on the ground..")
            print("The dragon has now given you all it's power! You are now a DRAGONBORN!!!")
            print("Intelligence maxed to 10! Damage maxed out at 10!")
            print("You've acquired dragon breath capability")
            print("Food supplies up by 30.")
            mercy += 1
            team['Hero']['Strength'] = 10
            team['Hero']['Intellect'] = 10
            food += 30
            game_status = True
            dragon_status = True
        elif q3_choice == 0 and opp_name == 'Giant':
            print("")
            print("The Giant is barely able to stand. Thanks you for your kindness..")
            print("Being a Parvateshwara he didn't expect any kindness from you. When his own clan people ostracized him.")
            print("He talks about being a part of Kshatriya clan eons back but was rejected as they became cynical and apprehensive about people different from them.")
            print("Giant has survived for ages and possesses immense knowledge about Kshatriyas.")
            print("He offers you a Potion..vanishes into thin air..")
            print("")
            print("The potion gives you all knowledge Kshatriyas possess. You learn what is is to be a Kshatriya.")
            print("Intelligence maxed to 10! Damage maxed out at 10!")
            print("Food supplies up by 30.")
            mercy += 1
            team['Hero']['Strength'] = 10
            team['Hero']['Intellect'] = 10
            food += 30
            game_status = True
            dragon_status = True
        elif q3_choice == 1:
            print("You showed no mercy to the creature, he lies dead on the ground!")
            print("You gained experience points! Intelligence up by 1!")
            print("Gained extra damage point. Damage up by 1")
            print("Food supplies up by 30.")
            team['Hero']['Strength'] += 1
            team['Hero']['Intellect'] += 1
            food += 30
            game_status = True
            dragon_status = False
    return [team, food,mercy,game_status,dragon_status]

def quest_4(team_choice,team,mercy,food,dragon_status):
    if team_choice == FACTIONS[0]:
        org_team = KASHATRIYAS
    else:
        org_team = PARVATESHWARAS

    #Getting necessary variables
    mercy = mercy
    org_opponent = RAKSHASA
    opponent = copy.deepcopy(org_opponent)
    dragon = dragon_status
    if team_choice == 'Parvateshwaras':
        dragon = True

    #Necessary Calculations
    max_thealth_q4 = 0
    for key in team:
        max_thealth_q4 += org_team[key]['Health']
    for key in org_opponent:
        max_opp_health = org_opponent[key]['Health']

    team_health = 0
    for key in team:
        team_health += team[key]['Health']
    for key in opponent:
        opponent_health = opponent[key]['Health']

    food = food
    defence_state = False
    print("")
    print("After defeating all the foes on your way, you finally reach Asarta-van")
    print("The clan head of Rakshasas, Narakasura has been waiting for the final showdown!")
    print("The demon emerges from ground. Wielding an enormous sword, engulfed in flames!")
    print("You wield your weapon and charge towards the creature..")
    print("Narakasura shoots multiple arrows at you. You deflect them away at breakneck speed.")
    for key in team:
        print("Your " + key + " is at health: " + str(team[key]['Health']))
    print("Your food supplies are at " + str(food))
    while team_health > 0 and opponent_health > 0:
        print("You 0) Attack 1) Defend 2) Restore Health")
        choice = check_input(input("Enter number: "), 'combat')
        if choice == 2 and team_health < max_thealth_q4 and food >= 1:
            difference = max_thealth_q4 - team_health
            print("Teams health is low by " + str(difference) + ". Your food supplies are at " + str(food))
            food_choice = check_input(
                input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            while food_choice > food or food_choice > difference or food_choice <= 0:
                print("Invalid input! Your food supplies are at " + str(food) + ".")
                print("You can only restore your health by " + str(difference) + ".")
                food_choice = check_input(
                    input("How much food do you wish to use? 1 Food = 1 Health point.\nEnter number: "), 'food_choice')
            output = health_choice(team, food_choice, food, team_health, org_team)
            food = output[0]
            team_health = output[1]
            print("Food resources at: " + str(food))
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Team health is at " + str(team_health))
        elif choice == 2 and team_health == max_thealth_q4 or food == 0:
            while choice == 2:
                print("Team already at full health or No food left. Choose again!")
                choice = check_input(input("Enter number: "), 'combat')
        if choice == 1:
            print("You raise your shields and brace for next attack!")
            defence_state = True
        if choice == 0:
            team_attack = attack(team)
            if team_attack >= 8 and dragon == True:
                print("---------------------------------------------------------------")
                print(r"""\
                                    ==(W{==========-      /===-                        
                                              ||  (.--.)         /===-_---~~~~~~~~~------____  
                                              | \_,|**|,__      |===-~___                _,-' `
                                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~      
                             ______-==|        /`\_. .__/\ \    | |  \\           _-~`         
                       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'             
                    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               
                  .'        /       |   \\      /~\___/~~\/  /' /        \   /'                
                 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  
                /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                                  \_|      /        _) | ;  ),   __--~~                        
                                    '~~--_/      _-~/- |/ \   '-~ \                            
                                   {\__--_/}    / \\_>-|)<__\      \                           
                                   /'   (_/  _-~  | |__>--<__|      |                          
                                  |   _/) )-~     | |__>--<__|      |                          
                                  / /~ ,_/       / /__>---<__/      |                          
                                 o-o _//        /-~_>---<__-~      /                           
                                 (^(~          /~_>---<__-      _-~                            
                                ,/|           /__>--<__/     _-~                               
                             ,//('(          |__>--<__|     /                  .----_          
                            ( ( '))          |__>--<__|    |                 /' _---_~\        
                         `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
                        ,/,'//( (             \__>--<__\    \            /'  //        ||      
                      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
                    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
                  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
                   ;'( ')/ ,)(                              ~~~~~~~~~~                         
                  ' ') '( (/                                                                   
                    '   '  `
                                    !!! D R A G O N   B R E A T H !!!!
                """)
                print("")
                print("You wound Narakasura fatally, hit him with your Dragon-Breath!")
                team_attack = math.floor(team_attack * 1.5)
                print("A " + str(team_attack) + " point attack!!")
                print("---------------------------------------------------------------")
            opponent_health = health_status(team_attack, opponent_health, opponent)
            print_status_opp('Narakasura', opponent_health, max_opp_health, update_opp(opponent))
        opponent_attack = attack_opp(defence_state, team, opponent)
        if opponent_health > 0:
            print("")
            print("Narakasura swings his mighty sword and attacks..")
            print("Hits you with a " + str(opponent_attack) + " point attack!")
        team_health = health_status(opponent_attack, team_health, team)
        update_team(team)
        defence_state = False
        print("")
        max_thealth_q4 = 0
        for key in team:
            max_thealth_q4 += org_team[key]['Health']
        if team_health > 0:
            for key in team:
                print("Your " + key + " is at health: " + str(team[key]['Health']))
            print("Your food supplies are at " + str(food))
    if team_health == 0:
        print("GAME OVER!! Start again")
        game_status = False
        return game_status
    else:
        print("")
        print("CONGRATULATIONS! You've WON!!")
        print("The mighty Narakasura is down!! You've defeated the Rakshasa clan's head.")
        print("Bringing an end to the war, restoring balance to the world again..")
        if mercy == 0:
            print("")
            print("Even though you've won, tensions still grow with the rival clans!")
            print("Villages and other parts of the empire have lost everything in your greed for power!")
            print("You cannot be a War God without showing any mercy!")
        elif mercy == 1:
            print("")
            print("You have been kind to others who are different from you!")
            print("Even though you've shown mercy but have been egocentric!")
            print("You cannot be a War God without being altruistic!")
        else:
            print("")
            print("You've been kind to others different from you!")
            print("Shown mercy on more than one occasion! Being altruistic has earned you the trust of other clans and people in your empire!")
            print("You are a true WAR-GOD!!!")
            img.show()
        game_status = True
        return game_status

def print_status(thealth,max_opp_health,status):
    # Keeps the health classified
    if status != True:
        if thealth >= (max_opp_health * .75):
            print("The Wolve(s) is/are wounded by your attack, overall still appear " + STATES[0])
        elif thealth >= (max_opp_health * .5):
            print("The Wolve(s) is/are wounded by your attack, now appear " + STATES[1])
        elif thealth >= (max_opp_health * .25):
            print("The Wolve(s) is/are wounded by your attack, now appear to be " + STATES[2])
        else:
            print("The Wolve(s) is/are wounded by your attack, now " + STATES[3])

def print_status_opp(name,thealth,max_opp_health,status):
    if status != True:
        if thealth >= (max_opp_health * .75):
            print("The " + name + " is wounded by your attack, still appears " + STATES[0])
        elif thealth >= (max_opp_health * .5):
            print("The " + name + " is wounded by your attack, now appears " + STATES[1])
        elif thealth >= (max_opp_health * .25):
            print("The " + name + " is wounded, now appears to be " + STATES[2])
        else:
            print("The " + name + " is wounded, now " + STATES[3])

def get_opt_quest():
    print("")
    print("After fighting off the Wolves, your team goes back to their base to rest and recuperate.")
    print("Next morning, they march towards the forest. A villager stops their way!")
    print("He speaks about how their village is constantly raided by a giant Griffin.")
    print("The villagers are already struggling to put food on plate, the griffin situation has made it difficult to save their cattle and flocks!")
    print("Due to the ongoing war villagers are short on soldiers and are desperately looking for any brave warrior who can help them!!")
    print("")
    print("Do you wish to help them?")
    print("0) Yes! 1) No! You have other matters to attend.")
    choice = check_input(input("Enter number: "), 'quest')
    return  choice

def update_team(team):
    # copy is crucial to prevent key change error, as dictionary might change in loop
    for key in team.copy():
        if team[key]['Health'] == 0:
            print("The attack has fatally wounded your " + key + "!" )
            print("You've lost your " + key)
            del team[key]

def attack_opp(state,team,opp):
    opponent_attack = 0
    # Intellect helps reduce the attack, higher intelligence of hero lower the attack
    if state == True:
        if random.random() <= (team['Hero']['Intellect']) / 10:
            opponent_attack = random.randint(0,1)
        else:
            for key in opp:
                opponent_attack += random.randint(1, math.floor(opp[key]['Strength']/ 2))
        return opponent_attack
    # No defence state, Attack can range from 1 to max strength
    else:
        for key in opp:
            opponent_attack += random.randint(1, opp[key]['Strength'])
        return opponent_attack

def update_opp(opp):
    for key in opp.copy():
        if opp[key]['Health'] == 0:
            print("FATALITY!! Your attack has SLAAAAINN!! the " + key + "!" )
            del opp[key]
            return True

def health_status(attack,thealth,opp):
    if attack >= thealth:
        thealth = 0
        for key in opp:
            opp[key]['Health'] = 0
    else:
        # Reverse is crucial to let the attack begin from last key
        reverse_list = list(opp.keys())
        reverse_list.reverse()
        thealth -= attack
        for key in reverse_list:
            value = min(opp[key]['Health'],attack)
            opp[key]['Health'] -= value
            attack -= value
    return thealth

def attack(team):
    team_attack = 0
    for key in team:
        # Intelligence increases chances of a severe attack
        if random.random() <= (team[key]['Intellect'])/10:
            team_attack += random.randint(math.floor((team[key]['Strength'])/2), team[key]['Strength'])
        else:
            team_attack += random.randint(1, team[key]['Strength'])
    return team_attack

def health_choice(team,food_c,food,team_health,org_team):
    for key in team:
        if team[key]['Health'] < org_team[key]['Health']:
            food -= food_c
            team[key]['Health'] += food_c
            team_health += food_c
            break
    return [food,team_health]

def outro_text():
    print("")
    print("---------------------------------------------------------------------------------------------------")
    print("The game has been a very basic attempt to test different concepts of programming!")
    print("Hope you've had fun as I've had while writing this..")
    print("Game offers you 3 different outcomes based the choices you've made. Try and get them all?")

# Crucial function ensuring all values input by user are legitimate
def check_input(value,key):
    while True:
        try:
            value = int(value)
            input_options = {'faction': [0, 1], 'combat': [0, 1, 2], 'food_choice': list(range(0, 100)), 'quest': [0,1]}
            while int(value) not in input_options[key]:
                print("Invalid Input! Enter the number indicated next to option\n")
                value = input("Enter number: ")
            break
        except ValueError:
            print("Please input integer only...")
            value = input("Enter number: ")
    return int(value)


if __name__ == '__main__':
    main()