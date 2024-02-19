#hangman game

import random

def hangman():
    word_list = ["python", "programming", "computer", "science"]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 10

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0 and "_" in word:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed {guess}.")
        else:
            guessed_letters.append(guess)

            if guess in word:
                print(f"Good job, {guess} is in the word!")
                word_so_far = ""
                for letter in word:
                    if letter in guessed_letters:
                        word_so_far += letter + " "
                    else:
                        word_so_far += "_ "
                print(word_so_far)
            else:
                print(f"Sorry, {guess} is not in the word.")
                attempts -= 1
                print(f"You have {attempts} attempts left.")

    if "_" not in word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over. The word was " + word)

hangman()