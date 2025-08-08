import random

def play_game():
    # List of possible words
    word_list = ["python", "philip", "programming", "developer", "computer", "niron", "challenge", 
                 "yoobee", "education", "learning"]

    # START: Generate a random word
    word = random.choice(word_list)
    word_letters = list(word)

    # Generate as many blanks as letters in the word
    display = ["_"] * len(word)

    # Set the number of lives
    lives = 5

    print("Welcome to the Word Guessing Game!")
    print(" ".join(display))

    # Main game loop
    while True:
        guess = input("Guess a letter: ").lower()

        if guess in word_letters:
            # Replace the blanks with the letter
            for i in range(len(word_letters)):
                if word_letters[i] == guess:
                    display[i] = guess

            # Show current progress
            print(" ".join(display))

            # Check if all blanks are filled
            if "_" not in display:
                print("Congratulations! You guessed the word: ", word)
                break
        else:
            # Lose a life
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

            # Check if lives are finished
            if lives == 0:
                print(f"Game Over! The word was '{word}'")
                break

if __name__ == "__main__":
    play_game()