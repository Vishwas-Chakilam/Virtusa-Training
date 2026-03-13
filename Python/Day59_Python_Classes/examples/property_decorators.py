class Temperature:
    def __init__(self, c):
        self._celsius = c

    @property # Getter
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32

    @fahrenheit.setter # Setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) / 1.8

t = Temperature(0)
print("Temp in F:", t.fahrenheit)
t.fahrenheit = 212
print("Temp in C:", t._celsius)