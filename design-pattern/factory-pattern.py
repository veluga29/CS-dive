from enum import Enum
import random


class CoffeeType(Enum):
    LATTE = "latte"
    ESPRESSO = "espresso"


class Latte:
    def __init__(self):
        self.name = "Latte"


class Espresso:
    def __init__(self):
        self.name = "Espresso"


class CoffeeFactory:
    @staticmethod
    def create_coffee(type):
        if type == CoffeeType.LATTE:
            return Latte()
        elif type == CoffeeType.ESPRESSO:
            return Espresso()
        else:
            raise Exception("Invalid Coffee Type")


coffee_type = random.choice(list(CoffeeType))
coffee = CoffeeFactory.create_coffee(coffee_type)
print(coffee.name)
