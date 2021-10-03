from character_class import Char, Ranger, Fighter, Mage, Rouge
from random import randint

# ------ GAME RUN FUNCTIONS ---------

def define_char_class():
        random = randint(0,3)
        char_class_select = Char.class_types[random]
        return char_class_select

def create_character():
        print("\n--- \nLet's start with a name. Enter your character's name. \nAnything goes, but remember, this is how you'll be referred to throughout this game.\n")

        name = input("What will be your name? --> ")

        def main_att_choice_type():
            main_att = input("Retype your attack: -->  ")
            print(f"Here's how that looks: \n \"{name}'s {main_att.upper()} strikes a devistating blow\" \n")
            main_att_choice = input("Happy with that? Type Y to continue or N to retype your primary attack. -->  ")
            if main_att_choice == "Y" or main_att_choice == "y" or main_att_choice == "yes":
                print(f"\n --- \n Wonderful, we have that stored. {name}'s primary attack is {main_att.upper()} \nNow, let's move on to the secondary attack...")
                return main_att
            else: 
                main_att_choice_type()

        def sec_att_choice_type():
            sec_att = input("Retype your attack: -->  ")
            print(f"Here's how that looks: \n \"{name}'s {sec_att.upper()} strikes a devistating blow\" \n")
            sec_att_choice = input("Happy with that? Type Y to continue or N to retype your primary attack. -->  ")
            if sec_att_choice == "Y" or sec_att_choice == "y" or sec_att_choice == "yes":
                return sec_att
            else: 
                sec_att_choice_type()

        def heal_choice_type():
            heal = input("Retype your attack: -->  ")
            print(f"Here's how that looks: \n \"{name} {heal.upper()} restoring health. \n")
            heal_choice = input("Happy with that? Type Y to continue or N to retype your primary attack. -->  ")
            if heal_choice == "Y" or heal_choice == "y" or heal_choice == "yes":
                return heal
            else: 
                heal_choice_type()

        print(f"\n--- \nAhh, yes, hello {name.upper()}. Welcome!\n \nNext let's pick your character class. \nThere are four character classes: Fighter, Rogue, Mage, & Ranger. \nYou can you pick any of these classes, or you can input \"RANDOM\" and a random class will be assigned to you.")

        char_class = input(f"\n\nWhat class will {name.upper()} be? -->")
        if char_class == "Mage" or char_class == "Ranger" or char_class == "Fighter" or char_class == "Rogue" or char_class == "mage" or char_class == "ranger" or char_class == "fighter" or char_class == "rogue":
            pass
        else: 
            char_class = "Random"
        print(f"Input = {char_class}")

        if char_class == "RANDOM" or char_class == "random" or char_class == "Random":
            char_class = define_char_class()
            print("\n---\nRandomizing your class...")
            print(f"\n...Okay, great. {name} will be a {char_class.upper()}.\n---")
        else:    
            print(f"\n--- \nOkay, great. {name} will be a {char_class.upper()}.")

        print(f"\nNow {name}, as a {char_class.upper()} you have a primary and secondary attack which you get to describe.\n \nLet's start with your primary attack. \nPlease describe the action of your primary attack. \nExamples in1clude \"fireball spell\", \"axe swing\", \"blazing hot arrow shot\", or \"dagger backstab\".")

        main_att = input("\n--- \nNow go ahead, what will your attack be? -->  ")

        print(f"\nHere's how that looks: \n  \"{name}'s {main_att.upper()} strikes a devistating blow\" \n")

        main_att_choice = input("Happy with that? Type Y to continue or N to retype your primary attack. -->  ")

        if main_att_choice == "N" or main_att_choice == "n" or main_att_choice == "no":
            main_att = main_att_choice_type()
        else:
            print(f"\n--- \nWonderful, we have that stored. {name}'s primary attack is {main_att.upper()}\nNow, let's move on to the secondary attack...")

        print(f"Your secondary attack is a quick-attack that is used if you roll a low result on your primary attack. It's something quick like \"shield slam\", \"kick\", \"staff-jab\", or \"trip\".")

        sec_att = input("\n---\nGo ahead, describe your secondary attack. -->  ")

        print(f"\nHere's how that looks: \n  \"{name}'s {sec_att.upper()} strikes a devistating blow\" \n")

        sec_att_choice = input("Happy with that? Type Y to continue or N to retype your primary attack. -->  ")

        if sec_att_choice == "N" or sec_att_choice == "n" or sec_att_choice == "no":
            sec_att = sec_att_choice_type()
        else:
            print(f"\n--- \nOkay, Nice! {name}'s secondary attack is {sec_att}")

        print(f"\n --- \nOne last thing, {name}! In this game, you can heal yourself. Describe what your heal action will look like. Example: \"drinks health potion\"")

        heal = input("Input your heal action -->  ")

        print(f"\n --- \nHere's how that looks: \n  \"{name} {heal.upper()}, restoring health. \n")

        heal_choice = input("Happy with that? Type Y to continue or N to retype your heal action. -->  ")

        if heal_choice == "N" or heal_choice == "n" or heal_choice == "no":
            heal = heal_choice_type()
        else:
            print(f"\n--- \nCopy that. {name}'s heal effect = {heal.upper()} \nThat should be it. Let's review your character...\n")

        def build_character(character, charClass):
            if charClass == "Rogue" or charClass == "rogue":
                return Rouge(character, char_class, main_att, sec_att, heal)
            elif charClass == "Mage" or charClass == "mage":
                return Mage(character, char_class, main_att, sec_att, heal)
            elif charClass == "Ranger" or charClass == "ranger":
                return Ranger(character, char_class, main_att, sec_att, heal)
            elif charClass == "Fighter"or charClass == "fighter":
                return Fighter(character, char_class, main_att, sec_att, heal)
                    
        return build_character(name, char_class)   

def create_another_character_func():
    create_another_character = input("\n--- \nCreate another character? Y for yes, N for no. -->  ")

    if create_another_character == "Y" or create_another_character == "y" or create_another_character == "yes":
        create_character()
        return True
    else:
        return False
# ^ Unused at the moment.

def print_char_data():
    print(f"-- PLAYERS --\n")
    for j in Char.roster:
        print(f"NAME: {Char.roster[j].name} \nCLASS: {Char.roster[j].char_class}\nMAIN ATT: {Char.roster[j].main_att} \nSEC ATT: {Char.roster[j].sec_att}\nHEAL ACT: {Char.roster[j].heal} \nHEALTH: {Char.roster[j].health} \nATT MOD: {Char.roster[j].att_mod} \nHEAL MOD: {Char.roster[j].heal_mod}\nBLOCK MOD: {Char.roster[j].block_mod}\n--------\n")

    print("<< Character build success! >>\n")
    return

# ----- QUICK PLAY -----
# For Quick Play, Characters Can be quickly created here. Requires commenting out the creat_character functions in the "--GAME ON--" below, and uncommenting the quck_character_builds functions

# def quick_character1():
    player1 = Char("Bash", "Fighter", "bat swing", "head butt", "drinks a potion")
    print(player1.name, player1.char_class, player1.main_att, player1.sec_att, player1.heal)
    return player1

# def quick_character2():
    player2 = Char("Bob", "Roque", "axe throw", "shield slam", "drinks blood")
    print(player2.name, player2.char_class, player2.main_att, player2.sec_att, player2.heal)
    return player2

# --------END QUICK PLAY FUNCTIONS------ 

## ------- PLAYER TURN FUNCTIONS -------
def check_health(current, other):
    if current.health == 0:
        print(f"{current.name} bleeds out on the floor and doesn't make it.")
        input("Dead. Do you understand? DEAD!! - type Y to accept defeat.")
        return True
    elif other.health == 0:
        print(f"{other.name} is downed.\n Will they make it?")
        input(f"No -they're dead... Dead! Do you understand? DEAD!!! \n[[{other.name}]] type Y to accept defeat. -->  ")
        return True
    else:
        return False

def take_action(current, other):
    action = input("\nWill you ATTACK 'A' or Heal 'H'? -->  ")
    if action == "A" or action == "a":
        foe = input(f"\n[[{current.name}]], who will you attack? {current.name} or {other.name} -->  ")  
        if foe == current.name:
            print(f"---\n...{current.name} looks at {current.name}. 'You're Mine!, wait... what? ahhh!")
            print(f"{current.name} causes 20 points of damange to themselves. Whatever they did just looks bad.")
            current.health -= 20
            if current.health <= 0:
                current.health = 0
                print(f"{current.name} | HEALTH: {current.health}\n")
                return True
            else: 
                print(f"{current.name} | HEALTH: {current.health}\n")
                return False
        elif foe == other.name:
            print(f"---\n...{current.name} looks at {other.name} and says, 'You're Mine!'")
            death = current.attack_action(other)
        else:
            print("...Input error. You heal.")
            death = current.heal_action()
    elif action =="H" or action =="h":
        death = current.heal_action()
    else:
        print("Error / End Turn")   
    if death == True:
        return True
    if death == False:
        return False

def player_turn(current, other):
    death = check_health(current, other)
    if death == False:
        print(f"\n[[_NEW TURN_]]\nOkay {current.name} you're up.")
        print(f"-------------------\n<<Hero Status:>> \n   {current.name} | Health: {current.health} \n   {other.name} | Health: {other.health}\n-------------------")
        death_result = take_action(current, other)
        if death_result == True:
            return True
        else:
            return False
    else:
        return True

# --- GAME ON ---- 
def game_on():  

    #  -- QUICK PLAY -- uncomment to creat characters quickly
    # player1 = quick_character1()
    # player2 = quick_character2()
    # -- -- -- -- -- -- --

    print(f"\nWelcome to Hack-A-Thong's RPG Experience\n")
    print("__¶_____________________________________________¶\n__¶¶___________________________________________¶\n__¶¶¶¶________________________________________¶¶¶\n__¶¶_¶¶_____________________________________¶¶_¶¶\n__¶¶__¶¶___________________________________¶¶__¶¶\n__¶¶_¶_¶¶_________________________________¶¶_¶_¶¶\n__¶¶__¶__¶_______________________________¶¶_¶__¶¶\n__¶¶___¶__¶¶____________________________¶__¶___¶¶\n___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶\n____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶\n_____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶\n______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶\n_______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶\n________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶\n_________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶\n__________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶\n___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶\n_____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶\n______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶\n________________¶¶¶___¶¶__¶¶¶___¶¶¶¶\n__________________¶¶¶___¶¶_¶¶__¶¶¶\n____________________¶¶¶__¶¶_¶¶¶¶\n____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶\n_________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶\n________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶\n________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶\n_____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶\n___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶\n__________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶\n_________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶\n_______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶\n______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶\n_¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶\n¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶\n¶¶_____¶¶¶¶______________________________¶¶_____¶¶\n_¶¶¶____¶¶_______________________________¶____¶¶¶\n__¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶\n____¶¶¶¶¶_________________________________¶¶¶\n")


    print(f"First, let's start by creating a character...")

    # -- FULL CHARACTER BUILD -- uncomment player(x) = create_character functions below
    player1 = create_character()
    print_char_data()
    print("Alright, now let's move to building player 2.")

    player2 = create_character()
    print_char_data()
    print("It's time to fight!!\n")

    death = False
    while death == False:
        death1 = player_turn(player1, player2)
        # print("death1= " + str(death1))
        death2 = player_turn(player2, player1)
        # print("death2= " + str(death2))
        if death1 == True or death2 == True:
            death = True

    print("\nA player has died!\n<------ GAME ------->\n<------ OVER ------->")
    return False

play_game = True
while play_game == True:
    play_game = game_on()



