import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, Guess is too low than my chosen number!')
        elif guess > random_number:
            print('Sorry, Guess is too high than my chosen number')

    print(f"YAY! Congrats. You have guessed the number {random_number} which is my chosen number!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), or too low(L), or correct (C)??: ").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f"YAY! The computer guessed your number, {guess}, correctly!")


# guess(int(input("Tell the number that you want to guess between 1 and ")))
# Guess the number that computer has guessed!

computer_guess(int(input("{COMPUTER}: Between what numbers do you want me to guess. Between 1 and ")))
# Guess a number and computer will guess it!