print("For loop over range:")
for i in range(1, 6):
    print(i)

print("For loop skipping odds:")
for i in range(1, 6):
    if i % 2 != 0:
        continue
    print(i)