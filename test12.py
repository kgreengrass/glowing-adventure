
import hangman_words
import random
class  hangman:
    word = "ANTIBACTERIAL"
    lives = 10
    length = len(word)
    string = "_" * length


    def split(word):
        return [char for char in word]
    def splitter(string):
        return [char for char in string]

    def splitee(amended_word):
        return [char for char in amended_word]

    print("The word is " + str(length) + " characters long")
    print(*string)
    string = splitter(string)
    print(word)
    while lives != 0:
        guess = input( "Please guess a letter...  ")
        guess = guess.upper()

        if str(guess) in word:

            print("Yes, you guessed right ")
            amended_word = word
            amended_word = splitee(amended_word)

            while (amended_word.count(guess) + 1) >= string.count(guess):
                index = word.index(guess)
                string[index] = guess
                word = split(word)
                amended_word = word.pop(index)
            print(*string)
            print(*amended_word)
            print(''.join(word))


        else:
            print("null")