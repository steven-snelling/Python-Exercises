from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    """
    Why cannot using extract method and pull up method to move the
    construction of ConcreteBuilderXXX to the Builder???????
    """

    # def __init__(self):
    #    self.__Room=[]

    @abstractmethod
    def build_wall(self):
        pass

    @abstractmethod
    def build_door(self):
        pass

    @abstractmethod
    def build_window(self):
        pass

    @abstractmethod
    def get_room(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.__Room = []

    def build_wall(self):
        self.__Room.append("Builder1 Build the wall. ")

    def build_door(self):
        self.__Room.append("Builder1 Build the door. ")

    def build_window(self):
        self.__Room.append("Builder1 Build the window. ")

    def get_room(self):
        return self.__Room


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.__Room = []

    def build_wall(self):
        self.__Room.append("Builder2 Build the wall. ")

    def build_door(self):
        self.__Room.append("Builder2 Build the door. ")

    def build_window(self):
        self.__Room.append("Builder2 Build the window. ")

    def get_room(self):
        return self.__Room


class Director(object):
    def __init__(self, builder):
        self.__build = builder

    def construct_order(self):
        self.__build.build_wall()
        self.__build.build_window()
        self.__build.build_door()


if __name__ == "__main__":
    builder1 = ConcreteBuilder1()
    director = Director(builder1)
    director.construct_order()
    print(builder1.get_room())

    builder2 = ConcreteBuilder2()
    director = Director(builder2)
    director.construct_order()
    print(builder2.get_room())
