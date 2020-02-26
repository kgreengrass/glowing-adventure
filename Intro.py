# comments are written like this
print('hello world!')
msg = "Hello World, This is testing"  # str
# name = "Kate"
print(msg)
a = 1
b = 2  # int
c = 3.5  # float

# print is a method, a method usually does something to a variable

type(msg)  # lets us find out the type of our objects
print(type(msg))  # have to ask it to tell us the value
print(type(c))
print(type(b))

# name = input('What is your name?  ')
# print(msg + ' ' + name + '!')
# age = input('How old are you?  ')
# age = int(age)
# grg = 'I see that you are '
# dob = input('What is your date of birth?  ')
# snacc = input('What is your favourite snack?  ')
# g1 = ' and that your date of birth is '
# g2 = ' is my favourite too!'
# print(grg + str(age) + g1 + str(dob) + '. ' + snacc + g2) this is called 'casting'

e = complex(2, 4)
print(e)

# how to add an int and a float  click control and forward slash to hash everything
# f= b + c
# print(f)
# print(type(f))
# g= e + b
# print(g)
#
# print(b/a)
# print(type(b/a))
#
# print(c*c)
# print(type(c*c))
#
# names = "King's Way"  # can use the other type of quotes to include them in the text
# print(names)
# # or we can also use
# single = 'King\'s Way'
# print(single)

# hi="Hello World!"  # specify numbers which will be the indexes of the characters you want
# print(hi[1])
# print(hi[1:])
# print(hi[:5])
# print(hi[6:12])
# print(hi[::-1])
# print(hi[::-4])
# print(hi[::2])  # skip characters e.g gives 0,2,4,...th characters
#
# msgg = ('      Hello World!              ')
# msgg=msgg.strip()  # removes leading and trailing spaces  ..important to reassign it
# print(msgg)
# print(len(msgg))  # length of the string

#
# print(msg.lower())
# print(msg.upper())
# print(msg.capitalize())
# print(msg.count('o')) #number of times a string appears
# print(msg.replace('o','e'))

# d = True
# f = False
# print(d == f)
# print(d != f)
# print(d >= True)
# print(f <= False)
# print(d > f)
# print(d < f)

# print(msg.isalpha())  # detects if there are only alphabetical character
# print(msg.islower()) # checks if a string is lower case
# print(msg.endswith('e'))
# print(msg.startswith('H'))
#

x = 0
y = 10
z = -1
d = None

print(bool(x))  # is a nothing, therefore it is false
print(bool(y))  # is true
print(bool(d))

# LISTS AND TUPLES #
# LISTS HAVE SQUARE BRACKETS AND TUPLES HAVE ROUND BRACKETS#
# tuples cannot be altered
#
# shopping_list=["nutella", "oranges", "tofu", "bourbons", 47, "One", "6"]  # lists can contain any data type
# print(shopping_list)  # whole list
# print(shopping_list[0])  # certain item in the list
# print(type(shopping_list))
# shopping_list.append("carrots")  # add something new
# print(shopping_list)
# shopping_list[1] = "clementines"  # amend an item
# print(shopping_list)
#
# print(len(shopping_list))  # five items in the list
#
# shopping_list.remove('bourbons')  # removes a specific item based on the entry
# print(shopping_list)
# shopping_list.pop(2)  # removes an item based on its index, if you put no number it takes the last entry
# print(shopping_list)
#
# essentials=("milk", "biscuits", "tea")  # cannot change the entries
# print(essentials)
# print(essentials.count("milk"))


# DICTIONARIES # very important !!! use key value pairs
# student_1 = {
#     "name": "Kate",
#     "stream": "Data",
#     "number": 3,
#     "snacks": ["biscuits", "nutella"],  # a list within the the dictionary
#     "other_dict": {
#         "other_key": "value",
#         "here": "other"
#     }
# }
# print(student_1)
# print(student_1["stream"])
# print(student_1["snacks"][1])
# print(student_1["other_dict"]["other_key"])  # use dictionary spec within dictionary
#
#
# student_1["name"] = "Bob"  # change a value
# print(student_1)
# student_1["snacks"].remove("nutella")  # remove an entry
# print(student_1)
#
# print(student_1.values())  # gives you a list of the 'values' part of the pairs

# name, course, dates (start,end ), trainers, topics(sql, python, nosql, big data),

# student = {
#     "Name": {
#         "Title": "Miss",
#         "First_Name": "Kate",
#         "Last_Name": "Greengrass"
#     },
#     "Course": "Data",
#     "Course Dates": {
#         "Start Date": "03-FEB-2020",
#         "End Date": "09-APR-2020"
#     },
#     "Trainers": ["Paula", "David"],
#     "Topics": { "SQL": {
#     "Week": 2,
#     "Content": ["Queries", "Functions"]
#                       },
#     "Python":{
#     "Week": 4,
#     "Content": "Coding"
#             },
#     "NoSQL": {
#         "Week": 6,
#         "Content": "blahblah"
#               }
# }
# }
# print(student)
# print(student["Topics"]["SQL"]["Content"][1])
#

######## SETS AND FROZEN SETS ############
# are unordered and unindexed
animals = {"giraffe", "dog", "guinea pig", "elephant", "tortoise"}
print(animals)  # random order

animals.add("lion")
print(animals)
animals.add("goat")
print(animals)
animals.discard("lion")
print(animals)
#
# # a frozen set you cannot change
# animals2 = frozenset(["giraffe", "dog", "guinea pig", "elephant", "tortoise"])
# print(animals2)  # not randomised, like a list within a tuple
#
# ###############CONTROL FLOW###########
#
# age = input("What is your age?   ")
# if int(age) >= 25:
#     print("You are over the age limit")
# if int(age) < 18:
#     print("You are under the age limit")
# else:
#     print("Click here to buy")

# TASK: provide user input of age
##############HOMEWORK
print("Hi there movie goer, the movies available today fit into the following categories: U, PG, 12A, 15 and 18")
rating = input("Which would you like to hear about?  ")
if rating == "18":
    print("Only people aged 18 and over can watch these movies, you may be asked to provide ID")
elif rating == "15":
    print("These movies are suitable for viewers age 15 and over")
elif rating == "12":
    print("These films are watchable by viewers over the age of 12, any viewers below this age must have a parent present")
elif rating == "PG":
    print("These films may not be appropriate for very small children, parental guidance is advised")
elif rating == "U":
    print("These films are suitable for everyone, have fun!")
else:
    print("Sorry, we didn't recognise your input, please try again.")





