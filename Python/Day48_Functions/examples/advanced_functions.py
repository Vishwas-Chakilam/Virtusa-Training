def summarize(*args, **kwargs):
    total = sum(args)
    print(f'Sum: {total}')
    for k, v in kwargs.items():
        print(f'{k}: {v}')

summarize(1, 2, 3, name="Alice", role="Admin")

square = lambda x: x ** 2
print(square(5))