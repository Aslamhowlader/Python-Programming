class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Same sound")

    def info(self):
        print(f"I am {self.name}")


class Dog(Animal):
    def __init__(self, name, brand):
        super().__init__(name)  # fixed indentation
        self.brand = brand

    def speak(self):
        print(f"{self.name} says woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow")


# Creating objects
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

# Testing methods
dog.info()    # I am Buddy
dog.speak()   # Buddy says woof!
cat.info()    # I am Whiskers
cat.speak()   # Whiskers says Meow