"""
By: Steven Snelling
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Nissan hatchback option mentioned at the end
"""
from abc import ABCMeta, abstractmethod


class AbstractCar(metaclass=ABCMeta):
    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def attach_wheels(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass


class Jeep(AbstractCar):
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self):
        body = Body()
        body.shape = "SUV"
        self.__body = body

    def attach_wheels(self):
        for i in range(4):
            wheel = Wheel()
            wheel.size = 22
            self.__wheels.append(wheel)

    def set_engine(self):
        engine = Engine()
        engine.horsepower = 400
        self.__engine = engine

    def specification(self):
        print("body: {}".format(self.__body.shape))
        print("engine horsepower: {}".format(self.__engine.horsepower))
        print("tire size: {}\'".format(self.__wheels[0].size))


class Nissan(AbstractCar):
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self):
        body = Body()
        body.shape = "hatchback"
        self.__body = body

    def attach_wheels(self):
        for i in range(4):
            wheel = Wheel()
            wheel.size = 16
            self.__wheels.append(wheel)

    def set_engine(self):
        engine = Engine()
        engine.horsepower = 85
        self.__engine = engine

    def specification(self):
        print("body: {}".format(self.__body.shape))
        print("engine horsepower: {}".format(self.__engine.horsepower))
        print("tire size: {}\'".format(self.__wheels[0].size))


# Car parts
class Wheel:
    def __init__(self):
        self.__size = None

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


class Engine:
    def __init__(self):
        self.__horsepower = None

    @property
    def horsepower(self):
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, horsepower):
        self.__horsepower = horsepower


class Body:
    def __init__(self):
        self.__shape = None

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        self.__shape = shape


class CarMaker(object):
    def __init__(self, model):
        self.model = model

    def make_car(self):
        self.model.attach_wheels()
        self.model.set_body()
        self.model.set_engine()


if __name__ == "__main__":

    print("---Jeep---")
    jeep = Jeep()
    CarMaker(jeep).make_car()
    jeep.specification()

    print("---Nissan---")
    nissan = Nissan()
    CarMaker(nissan).make_car()
    nissan.specification()


    """ expected output:
    Jeep
    body: SUV
    engine horsepower: 400
    tire size: 22'
    """

    """ additional functionality required is    
    Nissan
    body: hatchback
    engine horsepower: 85
    tire size: 16'
    """
