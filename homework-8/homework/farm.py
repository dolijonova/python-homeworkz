from datetime import datetime, time

class Animal:
    def __init__(self, name, species, eating_time):
        self.name = name
        self.species = species
        self.eating_time = eating_time

    def eat(self):
        print(f"{self.name} the {self.species} is eating at {self.eating_time}.")

    def __str__(self):
        return f"{self.name} the {self.species} (Eating Time: {self.eating_time})"


class Bird(Animal):
    def __init__(self, name, species, eating_time):
        super().__init__(name, species, eating_time)

    def fly(self):
        print(f"{self.name} the {self.species} is flying!")


class FourLeggedAnimal(Animal):
    def __init__(self, name, species, eating_time):
        super().__init__(name, species, eating_time)

    def run(self):
        print(f"{self.name} the {self.species} is running!")


class HomeAnimal(Animal):
    def __init__(self, name, species, eating_time):
        super().__init__(name, species, eating_time)

    def play(self):
        print(f"{self.name} the {self.species} is playing!")


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_animals(self):
        current_time = datetime.now().time()
        print(f"\nCurrent Time: {current_time}")
        for animal in self.animals:
            if animal.eating_time == current_time.strftime("%H:%M"):
                animal.eat()
            else:
                print(f"{animal.name} the {animal.species} is not eating now. Eating time is at {animal.eating_time}.")

    def display_animals(self):
        print("\nAnimals on the farm:")
        for animal in self.animals:
            print(animal)

if __name__ == "__main__":
    farm = Farm()
    hen = Bird("Henny", "Hen", "08:00")
    chicken = Bird("Chicky", "Chicken", "09:00")
    peacock = Bird("Peachy", "Peacock", "10:00")

    horse = FourLeggedAnimal("Horse", "Horse", "12:00")
    cow = FourLeggedAnimal("Moomu", "Cow", "14:00")
    sheep = FourLeggedAnimal("Sheepy", "Sheep", "16:00")

    dog = HomeAnimal("Buddy", "Dog", "18:00")
    cat = HomeAnimal("newcat", "Cat", "20:00")
    fish = HomeAnimal("Goldie", "Fish", "22:00")

    # Add animals to the farm
    farm.add_animal(hen)
    farm.add_animal(chicken)
    farm.add_animal(peacock)
    farm.add_animal(horse)
    farm.add_animal(cow)
    farm.add_animal(sheep)
    farm.add_animal(dog)
    farm.add_animal(cat)
    farm.add_animal(fish)

    # Display all animals
    farm.display_animals()

    # Simulate feeding animals
    farm.feed_animals()