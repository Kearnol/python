from random import randint

class Char:
    roster = {}
    class_types = ["Ranger", "Fighter", "Mage", "Rogue"]

    def __init__(self, name, char_class, main_att, sec_att, heal):
        self.name = name
        self.char_class = char_class
        self.main_att = main_att
        self.sec_att = sec_att
        self.heal = heal
        self.health = 100
        self.max_health = 100
        self.att_mod = randint(0,4)
        self.heal_mod = randint(0,4)
        self.block_mod = randint(0,4)
        Char.roster[name]= self

    def attack_action(self, foe):
        print(f"[[_ATTACK_]]\n...{self.name} attacks with {self.main_att}")
        roll = Char.d20_roll()
        mod_roll = roll + self.att_mod
        print(f"...{self.name} rolls an attack of {roll} + an attack modifier of {self.att_mod} = {mod_roll}")
        future_health = foe.health - mod_roll
        if roll == 20: 
            print("...!! Critical Shot!! + 10 damage")
            foe.health -=10
        if future_health > 0:
            foe.health -= mod_roll
            print(f"... the {self.main_att} lands and {foe.name} takes {mod_roll} points of damage.")
            print(f"{foe.name} | Health: {foe.health}\n")
        else:
            print(f"...{self.name}'s {self.main_att} strikes a CATASTROPHIC blow to {foe.name} causing {mod_roll} points of damange and bringing {foe.name} to their knees.\n Things do not look good for {foe.name}")
            foe.health = 0
            print(f"{foe.name} | Health: {foe.health}")
            print(f"\n---\n{foe.name} has been downed\n \nCan they survive?")           
            return True
# --- Second Attack Logic ---
        if roll <= 8 and future_health > 0:
            print("But wait!!")
            sec_roll = Char.d6_roll()
            sec_mod_roll = sec_roll + self.att_mod
            future_health = foe.health - sec_mod_roll
            if future_health > 0:
                foe.health -= sec_mod_roll
                print(f"...{self.name} moves quickly and attacks again. This time using their {self.sec_att}")
                print(f"... {self.name}'s {self.sec_att} is well placed and stikes {foe.name} causing {sec_mod_roll} points of damage.[Damage roll: {sec_roll} + Att Mod: {self.att_mod}]")
                print(f"\n{foe.name} | Health: {foe.health}")
            else:
                print(f"...{self.sec_att} strikes a CATASTROPHIC blow to {foe.name} causing {sec_mod_roll} points of damange and bringing {foe.name} to their knees.\n Things do not look good for {foe.name}")
                foe.health = 0
                print(f"\n{foe.name} Health: {foe.health}\n")
                return False
        else:
            sec_mod_roll = 0
# __ BLOCK LOGIC___
        response = input(f"...{foe.name} has the chance to block. To block, a d20 will roll. \n If the roll is 1 - 10, the block fails and 10 extra damange is taken. \n If the roll is 10 - 20, the block succeeds and the damage taken from {self.name} is reduced by 75%.\n---\nType 'Y' to attempt block \nType 'N' to end turn. \n  -->  ")
        if response == "Y" or response == "y":
            new_roll = Char.d20_roll()
            new_mod_roll = new_roll + foe.block_mod
            print(f"\n[[__BLOCK ATTEMPT__]]\n...{foe.name}'s block roll is {new_roll} + a block modifier of {foe.block_mod} = {new_mod_roll}")
            if new_mod_roll > 10:
                print(f"...{foe.name}'s block roll succeeds! {foe.name} effectively blocks {self.name}'s {self.main_att} and gains back {(sec_mod_roll + mod_roll)*.75} points of health.")
                foe.health += ((sec_mod_roll + mod_roll)*.75)
                print(f"{foe.name} | Health: {foe.health}")
                print("\n<< Okay, end of turn >>")
                return False
            else:
                future_health = foe.health - 10
                if future_health > 0:
                    foe.health -= 10
                    print(f"...{foe.name} whiff's the block, exposing them even more to {self.name}'s {self.main_att}. {foe.name} takes an extra 10 points of damage.\n")
                    print(f"{foe.name} | Health: {foe.health}")
                    return False
                else:
                    foe.health = 0
                    print(f"...{foe.name} fails to block {self.name}'s {self.sec_att} resulting in a CATASTROPHIC blow to {foe.name} and brining them to their knees.\n Things do not look good for {foe.name}")
                    print(f"{foe.name} | Health: {foe.health}")
                    return True
        else:
            print("\n<< Okay, end of turn >>")
            return False

    def heal_action(self):
        roll = Char.d8_roll()*2
        heal_mod_roll = roll + self.heal_mod
        print(f"\n...the heal roll was {roll} + a heal modifier of {self.heal_mod} = {heal_mod_roll}")
        future_health = self.health + heal_mod_roll
        if future_health < self.max_health:
            self.health += heal_mod_roll
            print(f"...{self.name} {self.heal}, restoring {roll} points of health")
            print(f"{self.name} | Health: {self.health}\n")
            return False
        else:
            self.health = self.max_health
            print(f"...{self.name} is at max health!")
            print(f"...{self.name} | Health: {self.health}\n")
            return False


    @classmethod
    def random_class(cls):
        random = randint(1,4)
        class_select = cls.class_types[random]
        return class_select

    @staticmethod
    def d20_roll():
        main_roll = randint(1, 20)
        return main_roll

    def d6_roll():
        sec_roll = randint(1,6)
        return sec_roll

    def d8_roll():
        d8roll = randint(1,8)
        return d8roll

class Ranger(Char):
    def __init__(self, name, char_class, main_att, sec_att, heal):
        super().__init__(name, char_class, main_att, sec_att, heal)
        self.health = 105
        self.max_health = 105
        self.att_mod = 3
        self.block_mod = 2
        self.heal_mod = 2
        Char.roster[name]= self

class Fighter(Char):
    def __init__(self, name, char_class, main_att, sec_att, heal):
        super().__init__(name, char_class, main_att, sec_att, heal)
        self.health = 115
        self.max_health = 115
        self.att_mod = 3
        self.block_mod = 3
        Char.roster[name]= self

class Mage(Char):
    def __init__(self, name, char_class, main_att, sec_att, heal):
        super().__init__(name, char_class, main_att, sec_att, heal)
        self.health = 100
        self.max_health = 100
        self.att_mod = 5
        self.heal_mod = 5
        Char.roster[name]= self

class Rouge(Char):
    def __init__(self, name, char_class, main_att, sec_att, heal):
        super().__init__(name, char_class, main_att, sec_att, heal)
        self.health = 100
        self.max_helth = 100
        self.att_mod = 3
        self.block_mod = 5
        Char.roster[name]= self
    