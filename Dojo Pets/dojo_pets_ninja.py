class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} on a walk")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} feeds {self.pet.name}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} gives {self.pet.name} a bath")
        self.pet.noise()
        return self
