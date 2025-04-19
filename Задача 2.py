class Animal:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} покормлен(а)")

    def sound(self):
        pass


class Bird(Animal):
    def collect_eggs(self):
        print(f"У птицы {self.name} собраны яйца")


class Cow(Animal):
    def milk(self):
        print(f"Корову {self.name} подоили")

    def sound(self):
        print(f"{self.name} говорит: Мууу")


class Goat(Animal):
    def milk(self):
        print(f"Козу {self.name} подоили")

    def sound(self):
        print(f"{self.name} говорит: Меее")


class Sheep(Animal):
    def shear(self):
        print(f"Овцу {self.name} постригли")

    def sound(self):
        print(f"{self.name} говорит: Беее")


class Duck(Bird):
    def sound(self):
        print(f"{self.name} говорит: Кря-кря")


class Chicken(Bird):
    def sound(self):
        print(f"{self.name} говорит: Ко-ко-ко")


class Goose(Bird):
    def sound(self):
        print(f"{self.name} говорит: Га-га-га")

animals = [
    Goose("Серый"),
    Goose("Белый"),
    Cow("Манька"),
    Sheep("Барашек"),
    Sheep("Кудрявый"),
    Chicken("Ко-Ко"),
    Chicken("Кукареку"),
    Goat("Рога"),
    Goat("Копыта"),
    Duck("Кряква")
]

print("\n🐾 Работа на ферме:\n")
for animal in animals:
    animal.feed()
    animal.sound()

    if isinstance(animal, Bird):
        animal.collect_eggs()
    elif isinstance(animal, (Cow, Goat)):
        animal.milk()
    elif isinstance(animal, Sheep):
        animal.shear()

    print("-" * 30)