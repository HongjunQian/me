# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """

    # while True:
    #     try:
    #         number = int(input("Enter a number between {} and {}: ".format(low, high)))
    #         if low < number < high:
    #             return number
    #         else:
    #             print(
    #                 "That's not a number within the specified range. Please try again."
    #             )
    #     except Exception:
    #         print("That's not a valid number. Please try again.")

    tries = 0

    while low <= high:
        guess = (low + high) // 2
        tries = tries + 1

        if guess == actual_number:
            return {"guess": guess, "tries": tries}
        elif guess < actual_number:
            print(f"Guess: {guess} (Too small)")
            low = guess + 1
        else:
            print(f"Guess: {guess} (Too big)")
            high = guess - 1

    # Write your code in here


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
