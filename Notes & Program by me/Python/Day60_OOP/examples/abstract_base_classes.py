from abc import ABC, abstractmethod

# Abstract base class
class BaseAnimal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(BaseAnimal):
    def make_sound(self):
        return "Bark!"

# a = BaseAnimal() # Raises TypeError
d = Dog()
print(d.make_sound())