class Pet:
    def __init__(self, name , type , tricks, health, energy ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("woof")
        return self
    def print_stats(self):
        print(self.health.energy)
        return self

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet()
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

spike = Pet("Spike", "Poodle", "Fetch", 20, 25)
harry = Ninja("Harry", "Potter", "Chewies", "Kibbits", spike)


harry.walk()
harry.feed()
harry.bathe()