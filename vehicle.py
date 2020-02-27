class Vehicle:

    def __init__(self, max_speed, model, speed=0):
        self.__max_speed = max_speed
        self.__model = model
        self._speed = speed
        self._backwards = 0

    def accelerate(self, amount):
        if self._backwards == 0:
            if self._speed + amount < self.__max_speed:
                self._speed += amount
                print("Woah, you sped up to " + str(self._speed) + " mph")
            else:
                self._speed = self.__max_speed
                print("Calm down there, don't get carried away! Your speed is capped at  " + str(self._speed) + " mph")
        if self._backwards != 0:
            print("You can't start going forward again! You need to stop first, your speed remains at " + str(self._backwards) + "mph")


    def brake(self, amount):
        if self._speed > 0 and self._backwards == 0:
            if (self._speed - amount) > 0:
                self._speed -= amount
                print("Woah, you slowed down to " + str(self._speed) + " mph")
            elif (self._speed - amount) < 0:
                self._speed = 0
                print("Oh boy, you've stopped! Your speed is " + str(self._speed) + " mph")
        elif self._backwards > 0 and self._speed == 0:
            if self._backwards - amount > 0:
                self._backwards -= amount
                print("Woah, you slowed down to " + str(self._backwards) + " mph")
            if (self._backwards - amount) < 0:
                self._backwards = 0
                print("Oh boy, you've stopped! Your speed is " + str(self._backwards) + " mph")
        elif self._speed == 0 and self._backwards == 0:
            print("You were already stopped! But you keep that foot on the brake just in case.")

    def current_speed(self):
        if self._speed > 0:
            print("Your current speed is " + str(self._speed) + " mph")
        elif self._backwards > 0:
            print("Your current speed is " + str(self._backwards) + " mph")
        elif self._speed == 0 and self._backwards == 0:
            print("Looks like you are stationary!")


    def reverse_accelerate(self, amount):
        if self._speed == 0:
            if self._backwards + amount < self.__max_speed:
                self._backwards += amount
                print("Woohoo! We are reversing at " + str(self._backwards) + " mph")
            else:
                self._backwards = self.__max_speed
                print("Calm down there, don't get carried away! Your speed is capped at " + str(self._backwards) + " mph")
        if self._speed != 0:
            print("You can't start reversing! You carry on at "+ str(self._speed) + " mph")

class Car(Vehicle):
    vehicle_type = "car"

    def __init__(self, max_speed, brand, model, speed=0):
        self.__max_speed = max_speed
        self.__brand = brand
        self.__model = model
        self._speed = speed
        self._backwards = 0

class Lorry(Vehicle):
    vehicle_type = "Lorry"

    def __init__(self, max_speed, brand, model, speed=0):
        self.__max_speed = max_speed
        self.__brand = brand
        self.__model = model
        self._speed = speed
        self._backwards = 0


    def horn(self):
        print("HONK HONNNKKKKK")

class Train(Vehicle):
    def __init__(self, max_speed, model, capacity, speed=0):
        self.__max_speed = max_speed
        self.__model = model
        self.capacity = capacity
        self._speed = speed
        self._backwards = 0

    def horn(self):
        print("choo choooooooo")

class Plane(Vehicle):
    def __init__(self, max_speed, model, height = 0,  speed=0):
        self.__max_speed = max_speed
        self.__model = model
        self._speed = speed
        self._altitude = height
        self._backwards = 0

    def lift(self, amount):
        self._altitude += amount
        print("Woah, you're at  " + str(self._altitude) + " thousand feet")

    def drop(self, amount):
        if self._altitude - amount > 0:
            self._altitude -= amount
            print("Woah, you're at  " + str(self._altitude) + " thousand feet")
        elif self._altitude - amount < 0:
            self._altitude = 0
            print("Welcome back to earth")




aero = Plane(500, "boeing", 0, 0)

aero.lift(20)
aero.drop(30)
