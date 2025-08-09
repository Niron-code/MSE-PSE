import random

class WordGuessingGame:
    def __init__(self):
        """Initialize the game with default settings"""
        self.word_list = ["python", "philip", "programming", "developer", "computer", 
                         "niron", "challenge", "yoobee", "education", "learning"]
        self.lives = 5
        self.word = ""
        self.word_letters = []
        self.display = []
        self.guessed_letters = set()
        
    def select_random_word(self):
        """Randomly select a word from the word list"""
        self.word = random.choice(self.word_list)
        self.word_letters = list(self.word)
        self.display = ["_"] * len(self.word)
        self.guessed_letters = set()
        
    def display_status(self):
        """Display the current state of the word"""
        print(f"\nWord ({len(self.word)} letters): {' '.join(self.display)}")
        
    def check_guess(self, guess):
        """Check if the guessed letter is in the word"""
        if guess in self.word_letters:
            for i in range(len(self.word_letters)):
                if self.word_letters[i] == guess:
                    self.display[i] = guess
            return True
        return False
    
    def is_game_won(self):
        """Check if all letters have been guessed"""
        return "_" not in self.display
    
    def is_game_over(self):
        """Check if player has run out of lives"""
        return self.lives <= 0
        
    def play(self):
        """Main game loop"""
        self.select_random_word()
        print("\nWelcome to the Word Guessing Game!")
        print(f"Try to guess the word that has {len(self.word)} letters!")
        self.display_status()
        
        while True:
            guess = input("Guess a letter: ").lower()
            
            # Check if letter was already guessed
            if guess in self.guessed_letters:
                print(f"You already guessed the letter '{guess}'! Try another one.")
                continue
            
            # Add the letter to guessed letters
            self.guessed_letters.add(guess)
            
            if self.check_guess(guess):
                self.display_status()
                
                if self.is_game_won():
                    print(f"Congratulations! You guessed the word: {self.word}")
                    break
            else:
                self.lives -= 1
                print(f"Wrong guess! Lives left: {self.lives}")
                
                if self.is_game_over():
                    print(f"Game Over! The word was '{self.word}'")
                    break

if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()