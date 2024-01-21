import random

try:
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


    guess(int(input("Tell the number that you want to guess between 1 and ")))

except:
    print("INVALID INPUT!")
    print("Now plz restart the Game. This is your Punishment!")
    print("<BY GAME OWNER> Hahahahaahahahahahahahahahah!")

