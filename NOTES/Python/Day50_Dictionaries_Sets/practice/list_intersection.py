list1 = ["apple", "banana", "cherry", "date"]
list2 = ["cherry", "date", "fig"]

# Convert to sets and intersect
common = list(set(list1) & set(list2))
print("Common elements:", common)