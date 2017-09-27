""" Example of AFTER applying Composite design pattern """

from abc import ABCMeta, abstractmethod


# abstract class as the interface between client and composite
class Component(metaclass=ABCMeta):
    def __init__(self, val):
        self.value = val

    def add(self, component):
        pass

    @abstractmethod
    def traverse(self):
        pass


class Primitive(Component):
    def __init__(self, val):
        Component.__init__(self, val)
        self.type = "LEAF"

    def traverse(self):
        # print("\t" + str(self.value) + "\t" + self.type)
        print('\t{}\t{}'.format(self.value, self.type))


class Composite(Component):
    def __init__(self, val):
        Component.__init__(self, val)
        self.children = []
        self.type = "INTERIOR"

    def add(self, component):
        self.children.append(component)

    def traverse(self):
        # print(str(self.value) + "\t" + self.type)
        print('{}\t{}'.format(self.value, self.type))
        for eachChild in self.children:
            eachChild.traverse()

if __name__ == '__main__':
    first = Composite(1)
    second = Composite(2)
    third = Composite(3)

    first.add(second)
    first.add(third)
    first.add(Primitive(4))
    second.add(Primitive(5))
    second.add(Primitive(6))
    third.add(Primitive(7))
    first.traverse()
