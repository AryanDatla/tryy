# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:42:41 2024

@author: ARYAN DATLA
"""

# -*- coding: utf-8 -*-

import random

EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 5
HARD_ATTEMPTS = 3

def generate_random_number():
    return random.randint(1, 100)

def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_guess(number, guess):
    if guess < number:
        print("Too low! Try a higher number.")
        return False
    elif guess > number:
        print("Too high! Try a lower number.")
        return False
    print("Congratulations! You guessed the correct number.")
    return True

def play_game(difficulty):
    number = generate_random_number()
    attempts = {
        "easy": EASY_ATTEMPTS,
        "medium": MEDIUM_ATTEMPTS,
        "hard": HARD_ATTEMPTS
    }[difficulty]
    for i in range(attempts):
        guess = get_user_input("Enter your guess: ")
        if check_guess(number, guess):
            print(f"You guessed the correct number in {i + 1} attempts.")
            break
        print(f"You have {attempts - i - 1} attempts left.")
    else:
        print(f"Sorry, you didn't guess the correct number. The correct number was {number}.")

def main():
    print("--------Welcome to the number guessing game--------")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Please select the difficulty level:\n"
                         "1. Easy (10 chances)\n"
                         "2. Medium (5 chances)\n"
                         "3. Hard (3 chances)\n"
                         "Enter your choice: ").lower()
    if difficulty in ["easy", "medium", "hard"]:
        play_game(difficulty)
    else:
        print("Wrong input. Please try again.")

if __name__ == "__main__":
    main()