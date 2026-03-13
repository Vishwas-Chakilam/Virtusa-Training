# Generators remember state and yield elements lazily (saves memory)
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2