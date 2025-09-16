# Snowman Meltdown Game - Starter
import random

# Snowman ASCII Art stages
STAGES = [
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    """,
    """
     ___  
    /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    # For now, just one guess to test display
    guess = input("Guess a letter: ").lower()
    guessed_letters.add(guess)
    mistakes += 1  # Simulate a wrong guess for testing

    display_game_state(mistakes, secret_word, guessed_letters)



if __name__ == "__main__":
    play_game()