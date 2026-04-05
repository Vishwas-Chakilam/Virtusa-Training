try:
    num = int(input("Enter number: "))
    res = 100 / num
except ValueError:
    print("Must be an integer!")
except ZeroDivisionError:
    print("Cannot divide by 0!")
else:
    print(f"All good, result is {res}")
finally:
    print("Block finished.")