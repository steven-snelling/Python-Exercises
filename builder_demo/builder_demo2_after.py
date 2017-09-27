"""
Purpose.  Builder
The monolithic design supports a single representation.
The Builder design allows a different representation
per Builder derived class,
and the common input and parsing have been defined in the Director class.
The Director constructs, the Builder returns the result.
"""

from abc import ABCMeta, abstractmethod


class Array(object):
    def __init__(self):
        self.lst = []

    def traverse(self):
        # print("\n",)
        print("\n")
        for item in self.lst:
            print(item, end=" ")


class Builder(metaclass=ABCMeta):
    def __init__(self):
        self.data = Array()

    def get_result(self):
        return self.data

    @abstractmethod
    def add_front(self, char):
        pass

    @abstractmethod
    def add_back(self, char):
        pass


class BuilderOne(Builder):
    def add_front(self, ch):
        self.data.lst.append(ch)

    def add_back(self, ch):
        self.data.lst.append(ch)


class BuilderTwo(Builder):
    def add_front(self, ch):
        self.data.lst.insert(0, ch)

    def add_back(self, ch):
        self.data.lst.append(ch)


class Director(object):
    def __init__(self, b):
        self.bldr = b

    def set_builder(self, b):
        self.bldr = b

    def construct(self, inputs):
        for item in inputs:
            if item[0] == 'f':
                self.bldr.add_front(item[1])
            elif item[0] == 'b':
                self.bldr.add_back(item[1])


if __name__ == "__main__":
    input_data = ("fa", "bb", "fc", "bd", "fe", "bf", "fg", "bh")

    one = BuilderOne()
    dir = Director(one)
    dir.construct(input_data)
    one.get_result().traverse()

    two = BuilderTwo()
    dir.set_builder(two)
    dir.construct(input_data)
    two.get_result().traverse()

    """
    expected output:
    a b c d e f g h
    g e c a b d f h
    """