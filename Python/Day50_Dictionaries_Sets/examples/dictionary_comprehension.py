keys = ['a', 'b', 'c']
values = [1, 2, 3]
# Using zip() to iterate them together
dict_comp = {k: v for k, v in zip(keys, values)}
print(dict_comp)