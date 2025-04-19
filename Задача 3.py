class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

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
    Goose("Серый", 5),
    Goose("Белый", 6),
    Cow("Манька", 350),
    Sheep("Барашек", 80),
    Sheep("Кудрявый", 78),
    Chicken("Ко-Ко", 2),
    Chicken("Кукареку", 2),
    Goat("Рога", 70),
    Goat("Копыта", 68),
    Duck("Кряква", 3)
]

total_weight = 0
heaviest_animal = None

for animal in animals:
    total_weight += animal.weight

    if heaviest_animal is None or animal.weight > heaviest_animal.weight:
        heaviest_animal = animal

print(f"\n📦 Общий вес всех животных: {total_weight} кг")
print(f"🏋️ Самое тяжёлое животное: {heaviest_animal.name} ({heaviest_animal.weight} кг)")