target = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == target:
        print("You got it!")
        break
    else:
        print("Wrong, try again.")