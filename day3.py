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

## specifying defaults
def useless_addition(integer1=1, integer2=2):
    return integer1 + integer2

print(useless_addition())
print(useless_addition(1, 8))
