# snowman.py

from game_logic import play_game

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing Snowman Meltdown! ☃️")
            break


if __name__ == "__main__":
    play_game()

