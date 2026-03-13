nums = [1, 2, 3, 4, 5]
# Using map with lambda to square numbers
squares = list(map(lambda x: x**2, nums))
print(*squares)

# Using filter to keep odds
odds = list(filter(lambda x: x%2 != 0, nums))
print(*odds)