"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def super_asker(low, high, message):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """

    while True:
        try:
            number = int(input(message))
            if low <= number <= high:
                return number
            else:
                print(
                    "That's not a number within the specified range. Please try again."
                )
        except Exception:
            print("That's not a valid number. Please try again.")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the advancedguessing game!")
    print("Please type 2 numbers to start:")

    lowerBound = super_asker(-200000, 200000, "Enter a lower bound: ")
    upperBound = super_asker(
        lowerBound + 2, 200000, f"Enter a upper bound, {lowerBound + 2} or above: "
    )

    print(f"OK then, a number between {lowerBound} and {upperBound} ?")
    actualNumber = random.randint(lowerBound, upperBound)

    while True:
        guessedNumber = super_asker(lowerBound, upperBound, "Guess a number: ")
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
