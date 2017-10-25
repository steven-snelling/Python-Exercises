from abc import ABCMeta, abstractmethod

# Class Adapter :: Using INHERITANCE

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


class FlyingCarAdapter(Car, Rocket):
    def get_wheels(self):
        self.get_blasters()

    def drive(self):
        self.fly()

    def apply_paint_job(self, colour):
        print("My rocket trails are now " + colour + "!")

    # Inheriting from it, can override behaviour easily.
    # def get_blasters(self):
    #     print("Attaching {} and {}.".format(*['blaster1', 'blaster2']))


# CLIENT
# Wants a flying car
# Only knows how to drive cars
def customer(car):
    car.get_wheels()
    car.drive()
    car.apply_paint_job("yellow")

if __name__ == '__main__':
    tractor = Tractor()
    customer(tractor)

    print()

    # Because we're defining the ADAPTER as a SubClass of the ADAPTEE,
    # we're committing to the single concrete ADAPTEE..
    # Can't reuse ADAPTER :(

    # rocket = FlyingCarAdapter()
    # customer(rocket)