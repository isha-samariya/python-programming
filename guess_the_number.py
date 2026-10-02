import random

print("HEY\nWelcome to the number guessing game\nYou have 5 chances to guess the number(1 to 100)")

n = random.randint(1,100)
attempts = 0

while attempts < 4:
    num = int(input("Enter your guess: "))

    if num > 100 or num < 1:
        print("Please enter a number between 1 to 100")
        continue

    attempts = attempts + 1

    if num == n:
        print("🎉 Correct! You guessed the number!")
        break
    elif num > n:
        print("Too High")
    else:
        print("Too Low")

if num != n:
    while True:
        num1 = int(input("Enter your guess: "))

        if num1 > 100 or num1 < 1:
            print("Please enter a number between 1 to 100")
            continue

        attempts = attempts + 1
        break

    if num1 == n:
        print("🎉 Correct! You guessed the number!")
    else:
        print("The number was",n)
        print("BETTER LUCK NEXT TIME")