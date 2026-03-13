def my_decorator(func):
    def wrapper():
        print("Something before function.")
        func()
        print("Something after function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()