import random


def guess_the_number():
    target_number = random.randint(1, 10)
    user_guess = int(input("Guess the number between 1 and 10: "))

    if user_guess == target_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {target_number}.")


guess_the_number()
