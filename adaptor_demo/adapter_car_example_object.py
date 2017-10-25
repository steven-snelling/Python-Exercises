from abc import ABCMeta, abstractmethod

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


# class SpaceShuttle(Rocket):
#
#     def get_blasters(self):
#         print("Attached to main rocket.")
#
#     def fly(self):
#         print("Falling gracefully into the ocean!")


# ADAPTER
class FlyingCarAdapter(Car):
    def __init__(self, rocket):
        self.rocket = rocket

    def get_wheels(self):
        self.rocket.get_blasters()

    def drive(self):
        self.rocket.fly()

    # Access to API, can't alter behaviour, only add to it.
    def apply_paint_job(self, colour):
        print("My rocket trails are now " + colour + "!")


# CLIENT
# Wants a flying car
# Only knows how to drive cars
def customer(car):
    car.get_wheels()
    car.drive()
    car.apply_paint_job("teal")

if __name__ == '__main__':
    tractor = Tractor()
    customer(tractor)

    print()

    # rocket = Rocket()
    # flying_car = FlyingCarAdapter(rocket)
    # customer(flying_car)

    print()

    # Through DEPENDENCY INJECTION we can reuse the ADAPTER polymorphically.
    # Anything of type 'Rocket'
    # OR Anything that implements an interface 'Rocket'

    # shuttle = SpaceShuttle()
    # floating_car = FlyingCarAdapter(shuttle)
    # customer(floating_car)
