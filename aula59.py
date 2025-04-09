import enum

def eat(fruit):
    print(f'Eating {fruit}')

# Creating the Enum for fruits
class Fruits(enum.Enum):
    APPLE = enum.auto()
    BANANA = enum.auto()
    ORANGE = enum.auto()
    GRAPE = enum.auto()

# Displaying information about the fruits
print(Fruits(1), Fruits['APPLE'], Fruits.APPLE)
print(Fruits(1).name, Fruits.APPLE.value)

# Function that accepts an object of type Fruits
def eat(fruit: Fruits):
    if not isinstance(fruit, Fruits):
        raise ValueError('Fruit not found')

    print(f'Eating {fruit.name} ({fruit.value})')

# Using the fruits
eat(Fruits.APPLE)
eat(Fruits.BANANA)
eat(Fruits.ORANGE)
eat(Fruits.GRAPE)
