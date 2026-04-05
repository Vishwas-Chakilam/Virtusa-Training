class MathLib:
    pi = 3.1415

    @classmethod
    def change_pi(cls, val):
        cls.pi = val

    @staticmethod
    def add(a, b): # Doesn't require access to self or cls
        return a + b

print(MathLib.add(5, 4))
MathLib.change_pi(3.14)
print(MathLib.pi)