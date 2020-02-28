
import hangman_words
import random

class hangman:
    word = random.choice(hangman_words.word_list)
    lives = 10
    guessed_letters = (" ")
    length = len(word)
    string = "_" * length

    def split(word):
        return [char for char in word]

    def splitter(string):
        return [char for char in string]

    print("The word is " + str(length) + " characters long")
    print(string)
    string = splitter(string)

    while lives != 0:
        print(word)
        guess = input( "Please guess a letter...  ")
        if guess.isalpha() and guess not in guessed_letters:
            if str(guess) in word:
                print("Yes, you guessed right ")
                index = word.index(guess)
                string[index] = guess
                print(string)



 # a = [1,2,3,4,5,1,2,3,4,5,1]        #Replacing every 1 with 10
 # for i in xrange(len(a)):
 #   if a[i] == 1:
 #     a[i] = 10
 # print a