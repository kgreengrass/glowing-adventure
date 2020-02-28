
import hangman_words
import random

class hangman:

    word = random.choice(hangman_words.word_list)
    lives = 10
    guessed_letters = [ ]
    length = len(word)
    string = "_" * length

    def split(word):
        return [char for char in word]

    def splitter(string):
        return [char for char in string]

    print("The word is " + str(length) + " characters long")
    print(*string)
    string = splitter(string)
    print(word)
    amended_word = word

    if "_" in string:

        while lives != 0:
            guess = input( "Please guess a letter...  ")
            guess = guess.upper()
            if guess.isalpha():
                if guess not in guessed_letters:
                    if str(guess) in word:
                        print("Yes, you guessed right ")
                        amended_word = splitee(amended_word)
                        index = word.index(guess)
                        string[index] = guess
                        print(*string)
                        guessed_letters.append(guess)

                    else:
                        lives -= 1
                        print("Uh-oh, no luck! You now have " + str(lives) + " lives left!")
                        print(*string)
                        guessed_letters.append(guess)
                        print("So far you have tried " + str(guessed_letters))
                elif guess in guessed_letters:
                    print("Looks like you've already tried that letter")
            else:
                print("Please enter an alphabetical character")
        else:
            print("Oh No! You're out of lives!")
    else:
        print("Well done! You won")

 # a = [1,2,3,4,5,1,2,3,4,5,1]        #Replacing every 1 with 10
 # for i in xrange(len(a)):
 #   if a[i] == 1:
 #     a[i] = 10
 # print a