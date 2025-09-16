# game_logic.py

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "="*30)
    print(f"❄️ Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(STAGES[mistakes])
    print("Word: ", end="")
    print(" ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print("="*30 + "\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 You saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("💧 The snowman melted! The word was:", secret_word)