import random
from guess_art import logo

the_number = random.randrange(1, 100)
difficulty = 0
print(logo)

choose = input("Choose a difficulty. Type 'easy' or 'hard' :")
if choose == 'easy':
    difficulty = 10
else:
    difficulty = 5
while True:
    guess = int(input("Make a guess: "))
    if guess < the_number:
        print("Too low.")
        difficulty -= 1
        if difficulty == 0:
            print("you've run out of guesses, you lose")
            break
        print("Guess again.")
        print(f"you have {difficulty}  attempts remaining  to guess the number.")

    if guess > the_number:
        print("too high.")
        difficulty -= 1
        if difficulty == 0:
            print("you've run out of guesses, you lose")
            break
        print("Guess again.")
        print(f"you have {difficulty}  attempts remaining  to guess the number.")

    elif guess == the_number:
        print(f"You got it! The answer was {the_number}")