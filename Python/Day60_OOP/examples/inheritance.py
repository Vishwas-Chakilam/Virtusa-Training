class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Noise"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    # Overriding method
    def speak(self):
        return "Meow!"

c = Cat("Whiskers", "Black")
print(f"{c.name} ({c.color}) says {c.speak()}")