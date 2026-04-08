class Engine:
    def start_engine(self): print("Engine started")

class Wheels:
    def spin(self): print("Wheels spinning")

# Inherits from both Engine and Wheels
class Car(Engine, Wheels):
    pass

c = Car()
c.start_engine()
c.spin()