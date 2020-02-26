# list_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
# list_2 = ["D", "G"]
# list_3 =  ["B", "C", "M", "P"]
# list_4 =  ["F", "H", "V", "W", "Y"]
# list_5 =  ["K"]
# list_8 = ["J", "X"]
# list_10 = ["Q", "Z"]
# word = input("Please write a word....   ")
# while word.isalpha() == False:
#     word = input("Please only include alphabetical characters...  ")
# word = word.upper()
# score = 0
# score = int(score)
# for x in word:
#     if x in list_1:
#         score += 1
#     if x in list_2:
#         score += 2
#     if x in list_3:
#         score += 3
#     if x in list_4:
#         score += 4
#     if x in list_5:
#         score += 5
#     if x in list_8:
#         score += 8
#     if x in list_10:
#         score += 10
# print(score)

##########FUNCTIONS###############
## dont repeat yourself
# def useless_print():  # dont have to pout anything in the brackets, arguments go in here
#     print("something was printed")
# # AVOID USING PRINT IN YOUR FUNCTIONS
# useless_print()  # calling the function

# def useless_addition(integer1, integer2):
#     return integer1 + integer2
#
#
# print(useless_addition(1, 3))

# ## specifying defaults
# def useless_addition(integer1=1, integer2=2):
#     return integer1 + integer2
#
# print(useless_addition())
# print(useless_addition(1, 8))

# def multi(*multiargs):
#     for args in multiargs:
#         print(args)    # specify that we want multiple arguments
#
# multi("hello", 8, 64265)  # specify the arguments

# def multi(*multiargs):
#     print(type(multiargs))  #  asks what type of things the multiargs is
#     for args in multiargs:
#         print(args)    # specify that we want multiple arguments
#
# multi("hello", 8, 64265)  # specify the arguments

## good practices for functions, function names are clear and obvious
## use underscores instead of spaces or varying cases
## comments are important, because it will make it easier for other people to interpret

#############make fizzbuzz into a function

# def fizzbuzz(x=1, y=1):
#     x = input("Lower Bound?   ")
#     while x.isnumeric() == False:
#         x = input("Please enter a numerical value for lower bound...  ")
#     y = input("Upper Bound?  ")
#     while y.isnumeric() == False:
#         y = input("Please enter a numerical value for upper bound...  ")
#     x = int(x)
#     y = int(y)
#     while y <= x:
#         y = input("Please enter a value greater than the lower bound...  ")
#         y = int(y)
#     while (y - x) > 200:
#         y = input("Please enter a number that is within a range of 200 of lower bound...")
#         while y.isnumeric() == False:
#             y = input("Please enter a numerical value for upper bound...  ")
#         y = int(y)
#     for d in range(x, y):
#         if d % 15 == 0:
#             print("Fizzbuzz")
#         if d % 3 == 0:
#             print("Fizz")
#         if d % 5 == 0:
#             print("Buzz")
#         else:
#             print(d)
#     return d
# print(fizzbuzz())

# def scrabble_calc(word="a"):
#     list_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
#     list_2 = ["D", "G"]
#     list_3 = ["B", "C", "M", "P"]
#     list_4 = ["F", "H", "V", "W", "Y"]
#     list_5 = ["K"]
#     list_8 = ["J", "X"]
#     list_10 = ["Q", "Z"]
#     word = input("Please write a word....   ")
#     while word.isalpha() == False:
#         word = input("Please only include alphabetical characters...  ")
#     word = word.upper()
#     score = 0
#     score = int(score)
#     for x in word:
#         if x in list_1:
#             score += 1
#         if x in list_2:
#             score += 2
#         if x in list_3:
#             score += 3
#         if x in list_4:
#             score += 4
#         if x in list_5:
#             score += 5
#         if x in list_8:
#             score += 8
#         if x in list_10:
#             score += 10
#     return(score)
#
# print(scrabble_calc( ))

# def fizzbuzz(x, y):  # without user input
#     x = int(x)
#     y = int(y)
#     for d in range(x, y):
#         if d % 15 == 0:
#             print("Fizzbuzz")
#         elif d % 3 == 0:
#             print("Fizz")
#         elif d % 5 == 0:
#             print("Buzz")
#         else:
#             print(d)
# fizzbuzz(1, 20)

