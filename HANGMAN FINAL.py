
import hangman_words
import random


class Hangman:
    word = random.choice(hangman_words.word_list)
    lives = 10
    guessed_letters = [ ]
    length = len(word)
    string = "_" * length
    amended_word = word

    def split(self):
        return [char for char in self]

    def looper(guess):
        while amended_word.count(guess) >= string.count(guess):
            index = word.index(guess)
            string[index] = guess
            amended_word = word.pop(index)

    word = split(word)
    amended_word = split(amended_word)
    string = split(string)
    print("Welcome to hang man! Your word is " + str(length) + " characters long")
    print(*word)
    print(*string)


    while "_" in string and lives != 0:
        guess = input("Please guess a letter..  ")
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:
            if guess not in guessed_letters:
                if guess in word:
                    print("Yay! You guessed right")
                    guessed_letters.append(guess)
                    while (amended_word.count(guess) ) > 0:
                            index = amended_word.index(guess)
                            string[index] = guess
                            amended_word[index] = "_"
                    else:
                        index = word.index(guess)
                        string[index] = guess
                        amended_word[index] = "_"
                    print(*string)
                    # print(*amended_word)
                else:
                    lives -= 1
                    print("No luck! You have " + str(lives) + " lives left!")
                    guessed_letters.append(guess)
                    print("So far you have tried " + str(guessed_letters))
            else:
                print("Looks like you've already tried that letter")
        else:
            print("Please enter one alphabetical character")
    else:
        if lives == 0:
            print("Oops! You're dead.")
            exit()
        else:
            print("Congratulations! You won")