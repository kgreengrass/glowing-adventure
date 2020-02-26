# ##
# class Dog:
#     animal_kind = 'canine'  # assigned it a class variable, basically attributes
#
#     def bark(self):  # class method, some sort of a doing thing
#         print(self.animal_kind)
#         return "woof"  # this method is referring to the current class
#
# # print(Dog)
# # print(Dog.animal_kind)
# # print(Dog.bark(Dog))
#
# ##### instantiation
# fido = Dog()
# pido = Dog()
# print(type(fido))
# print(type(pido))
# print(fido.animal_kind)
#
# fido.animal_kind = "cat"  # we can change the attributes of one without affecting the others
# print(fido.animal_kind)
#
# Dog.animal_kind = "Parrot"  # alter all the entries for the whole class, other than those which has been already decided
# print(fido.animal_kind)
# print(pido.animal_kind)


# initialisation means we have to sepcify something about the item on creation

# class Rabbit:
#     animal_kind = 'Bunny'  # assigned it a class variable, basically attributes
#     def __init__(self, name, colour):  ## add the variables required here
#         self.name = name
#         self.colour = colour
#     def twitch(self):  # class method, some sort of a doing thing
#         print(self.animal_kind)
#         return "sniffsniff"  # this method is referring to the current class
#
# peter = Rabbit("Peter", "Brown")
#
# print(peter.colour)
# print(peter.name)

# class Elephant:
#     animal_kind = 'Proboscidea'
#     weight_class = 'Jumbo'
#
#     def __init__(self, name, age, gender, country):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.country = country
#
#     def trumpet(self):
#         print(self.animal_kind)
#         return('toot toot')
#
# nb = Elephant('Nuba', 27, 'F', 'Senegal')
# dv = Elephant('Dave', 50, 'M', 'Republic of Congo')
#
# print(dv.name)
# print(dv.trumpet())

## ABSTRACTION, INHERITANCE, ENCAPSULATION, POLYMORPHISM##
# 4 KEY PILLARS OF OBJECT ORIENTED PROGRAMMING


class Animal:
    def __init__(self):
        self.alive = "Yes I'm alive!"

    def breathe(self):
        print("I breathe!")

    def moves(self):
        print("I move!")
#
#
# class Reptile(Animal):
#     # def __init__(self):
#     #     super().__init__()
#
#     def cold(self):
#         print("I'm cold blooded!")
#
# jean = Animal()
# print(jean.alive)
#
# ali = Reptile()
