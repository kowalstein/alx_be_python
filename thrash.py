class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return cls.add(a, -b)

animals = [Dog("Buddy"), Cat("Whiskers")]
sounds = [animal.speak() for animal in animals]
sum_result = Calculator.add(5, 3)
subtract_result = Calculator.subtract(10, 4)

print(sounds)
print(sum_result)
print(subtract_result)