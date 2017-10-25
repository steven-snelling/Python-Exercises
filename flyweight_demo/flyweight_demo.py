from abc import ABCMeta, abstractmethod


class FlyweightFactory(object):
    def __init__(self):
        self.__flyweight_pool = {}

    def get_flyweight(self, key):
        if key not in self.__flyweight_pool:
            print("Flyweight " + key + " has been created!")
            self.__flyweight_pool[key] = eval(key + "()")
        else:
            print("Flyweight " + key + " exists!")
        return self.__flyweight_pool[key]


class Flyweight(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def operation(self, extrinsic_state):
        print(self._name + " appears at " + extrinsic_state)


class ConcreteFlyweight1(Flyweight):
    def __init__(self):
        super().__init__("Flyweight 1")
        # self._name = "Flyweight 1"

    def operation(self, extrinsic_state):
        super().operation(extrinsic_state)


class ConcreteFlyweight2(Flyweight):
    def __init__(self):
        # self._name = "Flyweight 2"
        super().__init__("Flyweight 2")

    def operation(self, extrinsic_state):
        super().operation(extrinsic_state)


if __name__ == '__main__':
    f = FlyweightFactory()
    cf = f.get_flyweight("ConcreteFlyweight1")
    cf.operation("(1, 2)")

    cf = f.get_flyweight("ConcreteFlyweight1")
    cf.operation("(1, 3)")

    cf = f.get_flyweight("ConcreteFlyweight2")
    cf.operation("(2, 3)")
