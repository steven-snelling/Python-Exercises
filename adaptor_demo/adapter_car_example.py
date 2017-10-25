from abc import ABCMeta, abstractmethod

# Tasks:
# Class Adapter :: Using INHERITANCE
# Object Adapter :: Using COMPOSITION


# TARGET INTERFACE
class Car(metaclass=ABCMeta):
    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def apply_paint_job(self, colour):
        pass


class Tractor(Car):
    def get_wheels(self):
        print("Wheels are attached.")

    def drive(self):
        print("Driving!")

    def apply_paint_job(self, colour):
        print("I am now " + colour + "!")


# ADAPTEE
class Rocket(object):
    def get_blasters(self):
        print("All fueled up.")

    def fly(self):
        print("Flying!")


# CLIENT
# Wants a flying car
# Only knows how to drive cars
def customer(car):
    car.get_wheels()
    car.drive()
    car.apply_paint_job("blue")

if __name__ == '__main__':
    tractor = Tractor()
    customer(tractor)

    print()

    # rocket = Rocket()
    # customer(rocket)
