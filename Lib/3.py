class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed_info(self):
        if not self.animals:
            return None

        most_expensive_animal = max(self.animals, key=lambda x: x.cost)
        breed = most_expensive_animal.breed
        movement = most_expensive_animal.move()

        print(f"The most expensive breed is: {breed}")
        print(f"Movement: {movement}")
        print(f"Cost: {most_expensive_animal.cost}$")


class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        return "Undefined method for movement"


class Fish(Animal):
    def __init__(self, breed, cost, water_type):
        super().__init__(breed, cost)
        self.water_type = water_type

    def move(self):
        return "Swimming"


class Bird(Animal):
    def __init__(self, breed, cost, wingspan):
        super().__init__(breed, cost)
        self.wingspan = wingspan

    def move(self):
        return "Flying"


# Пример использования
if __name__ == "__main__":
    zoo = ZooShop()

    fish1 = Fish("Goldfish", 15, "Freshwater")
    fish2 = Fish("Angelfish", 20, "Saltwater")
    bird1 = Bird("Parrot", 30, 40)
    bird2 = Bird("Eagle", 50, 80)

    zoo.add_animal(fish1)
    zoo.add_animal(fish2)
    zoo.add_animal(bird1)
    zoo.add_animal(bird2)

    zoo.get_most_expensive_breed_info()

    with open("zoo_info.txt", "w") as file:
        for animal in zoo.animals:
            file.write(f"{animal.breed}: {animal.cost}$\n")