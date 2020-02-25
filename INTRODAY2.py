# # list_numbers = [1, 2, 3, 4, 5, 6]
# # for x in list_numbers:  # for something in a given list, do whatever is after the colon
# #     print(x)
# list_num = [[1, 2, 3], [4, 5, 6]]
# # for x in list_num:  # for something in a given list, do whatever is after the colon
# #     print(x)
# #     for num in x:  # this indentation mean it is a nested loop
# #         print(num)  # given the label x to the two separate lists within the bigger list, now give the individual
# #         # objects in those lists, the label "num"
# for x in list_num:
#     print(x)
#     for num in x:
#         print(num + 3)  # can do something to the individual entries but not on the list as a whole
#
# dict_data = {
#     1: {"name": "Geoff", "money": 2500 },
#     2: {"name": "John", "money": 2090},
#     3: {"name": "Brandon", "money": 200}
# }
#
# for x in dict_data.values():  # add the .values to make it print the entries that are associated to the keys
#     print(x)
#     for e in x.values():
#         print(e)
#
# list_numbers = [1, 2, 3, 4, 5, 6]
#
# for num in list_numbers:
#     if num == 3:
#         print("I found a three!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too small!")
#
#
#
# min = input("Please choose a number to start from    ")   # making it check if the user input is actually integer
# if (min.isdigit()):
#     max = input("Please choose a number finish at    ")
#     if (max.isdigit()):
#         min = int(min)
#         max = int(max)
#         for x in range(min, max):
#             if x % 15 == 0:
#                 print("Fizzbuzz")
#             if x % 3 == 0:
#                 print("Fizz")
#             if x % 5 == 0:
#                 print("Buzz")
#             else:
#                 print(x)
#     else:
#         print("Please enter a numerical value")
# else:
#         print("Please enter a numerical value")

# min = input("Please choose a number to start from    ")  ########MIZA'S SOLUTION ################
# max = input("Please choose a number finish at    ")
# while min.isnumeric()==True and max.isnumeric()==True:
#     if min<max:
#         for x in range(int(min), int(max)):
#             if x % 3 == 0 and x % 5 == 0:
#                 print("fizzbuzz")
#             elif x % 3 == 0:
#                 print("fizz")
#             elif x % 5 == 0:
#                 print("buzz")
#             else:
#                 print(x)
#     break


# x = 1
# while x < 10:
#     print("It's working!")
#     x += 1

# x = 1
# while x < 10:
#     print(f"It's working! {x}")  # prints the value of x within the text
#     x += 1

# x = 1
# while x < 10:
#     print(f"It's working! {x}")  # prints the value of x within the text
#     x += 1
#     if x == 4:
#         break  # add a breaking point


###############  add error messages if the input are not satisfactory
x = input("Lower Bound?   ")
while x.isnumeric() == False:
    x = input("Please enter a numerical value for lower bound...  ")
y = input("Upper Bound?  ")
while y.isnumeric() == False:
    y = input("Please enter a numerical value for upper bound...  ")
x = int(x)
y = int(y)
while y <= x:
    y = input("Please enter a value greater than the lower bound...  ")
    y = int(y)
while (y-x) >200:
    y = input("Please enter a number that is within a range of 200 of lower bound...")
    while y.isnumeric() == False:
        y = input("Please enter a numerical value for upper bound...  ")
    y = int(y)
for d in range(x, y):
    if d % 15 == 0:
        print("Fizzbuzz")
    if d % 3 == 0:
        print("Fizz")
    if d % 5 == 0:
        print("Buzz")
    else:
        print(d)
