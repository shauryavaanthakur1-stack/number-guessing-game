"""
Number Guessing Game
A mini project using Python: loops, conditions, functions,
random module and exception handling.
"""

import random

MIN_NUM = 1
MAX_NUM = 100
MAX_ATTEMPTS = 7


def get_guess():
    """Take a valid integer guess from the user (handles invalid input)."""
    while True:
        try:
            guess = int(input("Aapka guess: "))
            if guess < MIN_NUM or guess > MAX_NUM:
                print(f"Please {MIN_NUM} se {MAX_NUM} ke beech ka number daalo.")
                continue
            return guess
        except ValueError:
            print("Invalid input! Sirf number daalo.")


def play_game():
    """Play one round of the game. Returns True if the player won."""
    secret = random.randint(MIN_NUM, MAX_NUM)
    attempts = 0

    print(f"\nMaine {MIN_NUM} se {MAX_NUM} ke beech ek number socha hai.")
    print(f"Aapke paas {MAX_ATTEMPTS} attempts hain. Guess karo!\n")

    while attempts < MAX_ATTEMPTS:
        guess = get_guess()
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        if guess > secret:
            print(f"Too high! Chhota number try karo. (Attempts left: {remaining})")
        elif guess < secret:
            print(f"Too low! Bada number try karo. (Attempts left: {remaining})")
        else:
            print(f"Correct! Aapne {attempts} attempts mein guess kar liya.")
            return True

    print(f"Game over! Sahi number {secret} tha.")
    return False


def main():
    print("=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)

    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_game():
            wins += 1

        again = input("\nDobara khelna hai? (yes/no): ").strip().lower()
        if again != "yes":
            break

    print(f"\nTotal rounds: {rounds} | Jeete: {wins} | Haare: {rounds - wins}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
