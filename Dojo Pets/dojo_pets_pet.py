from dojo_pets_ninja import Ninja

class Pet:
    def __init__(self, name, type, tricks):
        self.energy = 50
        self.health = 100
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = "grunts"

    def sleep(self):
        print(f"{self.name} goes night night")
        self.energy += 25
        print(f"{self.name}'s energy = {self.energy}")

    def eat(self):
        print(f"{self.name} chows down")
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy = {self.energy} and health = {self.health}")

    def play(self):
        print(f"{self.name} plays")
        self.health += 5
        print(f"{self.name}'s health = {self.health}")

    def noise(self):
        print(f"{self.name} {self.sound}")

class Cat(Pet):
    def __init__(self, name, tricks, color):
        super().__init__(name, "cat", tricks)
        self.color = color
    
    def sleep(self):
        print(f"{self.name} goes night night")
        self.energy += 25
        print(f"{self.name}'s energy = {self.energy}")

    def eat(self):
        print(f"{self.name} chows down")
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy = {self.energy} and health = {self.health}")

    def play(self):
        print(f"{self.name} plays")
        self.health += 5
        print(f"{self.name}'s health = {self.health}")

    def noise(self):
        print(f"{self.name} {self.sound}")


nardy = Pet("Nardy", "Dog", ["back-flip", "high-five", "speak"])
bert = Ninja("Big-Boy", "Bert", nardy, "kibbles", "PupChow")
print(bert.pet.name)
bert.feed().walk().bathe()

pickles = Cat("Pickles", ["batt-ball", "chase laser"], "blue")
samantha = Ninja("Samantha", "Jones", pickles, "nibbles", "tuna")

print(samantha.pet.name, samantha.pet.type, samantha.pet.tricks)

