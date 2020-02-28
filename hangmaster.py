
import hangman_words
import random


class Hangman:
    word = random.choice(hangman_words.word_list)
    lives = 10
    guessed_letters = [ ]
    length = len(word)
    string = "_" * length

    def split(self):
        return [char for char in self]

    word = split(word)
    amended_word = word
    amended_word = split(amended_word)
    string = split(string)
    print("Welcome to hang man! Your word is " + str(length) + " characters long")
    print(*word)
    print(*string)
    amended_word = word

    if "_" in string:
        while lives != 0:
            guess = input("Please guess a letter..  ")
            guess = guess.upper()
            if guess.isalpha():
                if guess not in guessed_letters:
                    if guess in word:
                        print("Yay! You guessed right")
                        while amended_word.count(guess) >= string.count(guess):
                            index = word.index(guess)
                            string[index] = guess
                            amended_word = word.pop(index)
                        print(*string)
                    else:
                        lives -= 1
                        print("No luck! You have " + str(lives) + " lives left!")
                        guessed_letters.append(guess)
                        print("So far you have tried " + str(*guessed_letters))
                else:
                    print("Looks like you've already tried that letter")
            else:
                print("Please enter an alphabetical character")
        else:
            print("Oops! Looks like you're dead!")


    else:
        print("Congratulations! You've won!!!")



