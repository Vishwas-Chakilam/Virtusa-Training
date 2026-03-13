my_tuple = (10, 20, 30, 40)
a, b, *rest = my_tuple
print("First:", a)   # 10
print("Second:", b)  # 20
print("Rest:", rest) # [30, 40]