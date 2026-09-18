import random

guess_number = random.randint(1, 100)

user_guess = 0  

while user_guess != guess_number:
    user_guess = int(input("Guess the number: "))

    if user_guess > guess_number:
        print("Lower")
    elif user_guess < guess_number:
        print("Higher")
    else:
        print("Correct guess!")
