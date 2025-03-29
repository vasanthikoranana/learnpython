import random
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == num:
    print("You guessed it right!")
else:
    print("Wrong! The number was", num)
