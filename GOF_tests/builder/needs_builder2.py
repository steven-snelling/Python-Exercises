"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Nissan hatchback option mentioned at the end
"""


# The whole product
class Car:
    """ The final product.
    A car is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """

    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheels(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
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

        
if __name__ == "__main__":
    """ expected output:
    Jeep
    body: SUV
    engine horsepower: 400
    tire size: 22'
    """
    print("Jeep")
    jeep = Car()

    jeep_body = Body()
    jeep_body.shape = "SUV"
    jeep.set_body(jeep_body)

    jeep_engine = Engine()
    jeep_engine.horsepower = 400
    jeep.set_engine(jeep_engine)
    
    for i in range(4):
        jeep_wheel = Wheel()
        jeep_wheel.size = 22
        jeep.attach_wheels(jeep_wheel)
        
    jeep.specification()

    """ additional functionality required is    
    Nissan
    body: hatchback
    engine horsepower: 85
    tire size: 16'
    """
