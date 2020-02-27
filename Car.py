class Car:
    vehicle_type = "car"

    def __init__(self, max_speed, brand, model, speed=0):
        self.__max_speed = max_speed
        self.__brand = brand
        self.__model = model
        self._speed = speed
        self.__backwards = 0

    def accelerate(self, amount):
        if self.__backwards == 0:
            if self._speed + amount < self.__max_speed:
                self._speed += amount
                print("Woah, you sped up to " + str(self._speed) + " mph")
            else:
                self._speed = self.__max_speed
                print("Calm down there, don't get carried away! Your speed is capped at  " + str(self._speed) + " mph")
        if self.__backwards != 0:
            print("You can't start going forward again! You need to stop first, your speed remains at " + str(self.__backwards) + "mph")


    def brake(self, amount):
        if self._speed > 0 and self.__backwards == 0:
            if (self._speed - amount) > 0:
                self._speed -= amount
                print("Woah, you slowed down to " + str(self._speed) + " mph")
            elif (self._speed - amount) < 0:
                self._speed = 0
                print("Oh boy, you've stopped! Your speed is " + str(self._speed) + " mph")
        elif self.__backwards > 0 and self._speed == 0:
            if self.__backwards - amount > 0:
                self.__backwards -= amount
                print("Woah, you slowed down to " + str(self.__backwards) + " mph")
            if (self.__backwards - amount) < 0:
                self.__backwards = 0
                print("Oh boy, you've stopped! Your speed is " + str(self.__backwards) + " mph")
        elif self._speed == 0 and self.__backwards == 0:
            print("You were already stopped! But you keep that foot on the brake just in case.")

    def current_speed(self):
        if self._speed > 0:
            print("Your current speed is " + str(self._speed) + " mph")
        if self.__backwards > 0:
            print("Your current speed is " + str(self.__backwards) + " mph")
        if self._speed == 0 and self.__backwards == 0:
            print("Looks like you are stationary!")


    def reverse_accelerate(self, amount):
        if self._speed == 0:
            if self.__backwards + amount < self.__max_speed:
                self.__backwards += amount
                print("Woohoo! We are reversing at " + str(self.__backwards) + " mph")
            else:
                self.__backwards = self.__max_speed
                print("Calm down there, don't get carried away! Your speed is capped at " + str(self.__backwards) + " mph")
        if self._speed != 0:
            print("You can't start reversing! You carry on at "+ str(self._speed) + " mph")


car1 = Car(97, 'BMW', 'S-Series')
car1.current_speed()
car1.accelerate(70)
car1.brake(20)
car1.brake(60)
car1.accelerate(50)
car1.brake(46)
