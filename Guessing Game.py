from random import randint
import sys

x = randint(1,100)
guess = []
tally = []

print("Welcome to the guessing game! \nGuess a number between 1 and 100.")
print(x)

while guess != x:
    guess = int(input("What number did I guess? \nYour answer: "))

    if guess not in range(1, 101):
        print("OUT OF BOUNDS. Try again.")
        continue

    tally.append(guess)

    if guess == x:
        print(f"Well done! You've guessed the correct number. \nYou've guessed the number in {len(tally)} attempts. \nThanks for playing!")
        break

    if len(tally) == 1:
        if abs(guess - x) <= 10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if abs(guess - x) < abs(tally[-2] - x):
            print("WARMER!")
        else:
            print("COLDER!")

sys.exit()
    