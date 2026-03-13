my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, val in my_dict.items():
    print(f'{key}={val}')

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print('Union:', set_a | set_b)
print('Intersection:', set_a & set_b)