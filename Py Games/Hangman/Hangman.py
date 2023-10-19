import random
from words_list import word_list
from Logo import hang_logo, hangman_drawings

# Display the Hangman game logo and select a random word from the word list
print(hang_logo)
random_word = random.choice(word_list)

# Initialize a list to represent the word to be guessed
word_filled = [" _ " for _ in range(len(random_word))]

# Display the initial hidden word
for d in word_filled:
    print(d, end='')
print()

# Initialize game variables
lose_counter = 0  # Counter for incorrect guesses
win_counter = 0   # Counter for correct guesses
life = 6         # Number of lives

# Main game loop
while True:
    final_word = "".join(word_filled)

    # Check if the player has guessed the entire word
    if random_word == final_word:
        print('you win')
        break

    # Get a letter guess from the player
    guess = input("Guess a letter: ").lower()

    # Check for valid input (single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the guess is in the random word
    if guess in random_word:
        print(f"Lives: {life}")

        # Check if the letter has already been guessed
        if guess in word_filled:
            print(f"You already guessed {guess}. Try another letter.")
            print(hangman_drawings[lose_counter])
            continue

        # Update the word with correct guesses
        for i in range(len(random_word)):
            if random_word[i] == guess:
                word_filled[i] = random_word[i]
                win_counter += 1

        # Display the current state of the word and hangman drawing
        for j in word_filled:
            print(j, end='')
        print()
        print(hangman_drawings[lose_counter])

        # Check if the player has guessed the entire word
        if random_word == final_word:
            print('You win!')
            break
    else:
        # Check if the letter has already been guessed
        if guess in word_filled:
            print(f"You already guessed {guess}. Try another letter.")
            print(hangman_drawings[lose_counter])
            continue

        # Update the number of lives and display the hangman drawing
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # Increment the incorrect guess counter
        lose_counter += 1
        print(f"Lives: {life}")
        for j in word_filled:
            print(j, end='')
        print()
        print(hangman_drawings[lose_counter])

        # Check if the player has lost the game
        if lose_counter == 6:
            print(f"You lost. The word was {random_word}")
            break
