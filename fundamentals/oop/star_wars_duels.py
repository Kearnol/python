from random import randint

class Trooper: # capatalize the first letter
    game_name = "Star Wars Dojo Duel"
    everyone = []
    def __init__(self,name,attack): # this is the "initialize" constructor function 
        self.name = name
        self.weapon = "Blaster"
        self.attack = attack
        self.health = 100
        Trooper.everyone.append(self)

    def fight(self, foe):
        rand_attack = randint(0, self.attack)
        foe.health -= rand_attack
        if foe.health > 0:
            print(f"{self.name} damages {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} remaining health = {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")
        return self

    def heal(self, heal=0):
        rand_health = randint(1,10)
        self.health += heal
        self.health += rand_health
        future_health = self.health + rand_health + heal
        if Trooper.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} heals for {rand_health} | current health: {self.health}")
            return self
        else: 
            self.health = 100
            print(f"{self.name} is at max health. {self.name}'s health is {self.health}." )
        return self
    
    @classmethod
    def all_fighters(cls):
        print("Fighters:")
        for fighter in cls.everyone:
            print(f" Fighter: {fighter.name} | Weapon: {fighter.weapon} | Health: {fighter.health}")

    @staticmethod
    def can_heal(future_health):
        if future_health > 100:
            return False
        else:
            return True

class Jedi(Trooper): # class inheritance 
    def __init__(self, name, attack):
        super().__init__(name, attack) # inteherits the attribute values of Parent Class of Trooper
        self.trooper = Trooper("Finn", 25) # class association 
        self.weapon = "Light Saber" #overrides the parent class
        self.force_push_attack = 50
        self.health = 200
        # polymorphism = when a child class overrides attributes of a parent class, such as weapon & health
        def __repr__(self):
            return str(f"This is the Jedi Class: {self.Name} | {self.Attack} | {self.weapon}")

    def __repr__(self) -> str:
        return f"This is {self.name} a JEDI with {self.health} health and using a {self.weapon} as their weapon."


    def force_push(self, foe):
        foe.health -= self.force_push_attack
        if foe.health > 0:
            print(f"{self.name} damages {foe.name} with a Force Push by {self.force_push_attack}")
            print(f"{foe.name} remaining health = {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with Force Push using their {self.weapon}")
        return self
    
    def heal(self, heal=0):
        rand_health = randint(1,10)
        self.health += heal
        self.health += rand_health
        future_health = self.health + rand_health + heal
        if Jedi.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} heals for {rand_health} | current health: {self.health}")
            return self
        else: 
            self.health = 200
            print(f"{self.name} is at max health. {self.name}'s health is {self.health}." )
        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 200:
            return False
        else:
            return True

class Sith(Jedi):
    def __init__(self, name, attack, color): #(me testing) – you can add additional perameters that are not handled by the super().funciton
        super().__init__(name, attack)
        self.color = color # (me testing) – and you can define attributes with those additional parameters. 
        self.force_lightening_attack = 75

    def force_lightening(self, foe):
        foe.health -= self.force_lightening_attack
        if foe.health > 0:
            print(f"{self.name} damages {foe.name} with Force Lightening by {self.force_lightening_attack}")
            print(f"{foe.name} remaining health = {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with Force Lightening using their {self.weapon}")
        return self



print(f"Welcome to {Trooper.game_name}")

vader = Sith("Darth Vader", 75, "red")
# print(vader.name, vader.color, vader.health, vader.attack, vader.weapon)
obi = Jedi("Obi Wan", 75)
rex = Trooper("Rex",50)
cody = Trooper("Cody",12)
Trooper.all_fighters()   
print(f"<< {rex.name} vs {vader.name} vs {obi.name} vs {cody.name} >>")
print(obi) #this is possible as a result of __repr__() function under the JEDI Class 
print("<< Let's Begin >>")
vader.force_lightening(obi).fight(rex).fight(cody).force_push(obi) #chaining  - requires that the class methods used here return "self"
obi.force_push(rex)
rex.fight(obi)
rex.fight(obi)
obi.heal(75)
print("<<A short skuffle insues>>")
rex.fight(cody)
rex.fight(cody)
rex.fight(cody)
cody.fight(rex)
cody.fight(rex)
cody.heal(30)

# print("Status:")
# print(f"{rex.name}: Attack – {rex.attack} | Health – {rex.health}")
# print(f"{cody.name}: Attack - {cody.attack} | Health – {cody.health}")


# this is the long form 👇

# rex = {
#     "name": "Rex",
#     "attack": 15,
#     "weapon": "Blaster",
#     "health": 100
# }

# cody = {
#     "name": "Cody",
#     "attack": 15,
#     "weapon": "Blaster",
#     "health": 100
# }

# print(rex["name"])
# print(rex["attack"])
# print(rex["weapon"])
# print(rex["health"])
# print(cody["name"])
# print(cody["attack"])
# print(cody["weapon"])
# print(cody["health"])

