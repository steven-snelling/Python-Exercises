"""
REPLACE THIS LINE WITH YOUR NAME
"""

from abc import ABCMeta, abstractmethod


# There are two families of related products
# AbstractProductA
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def cook(self):
        pass


# ConcreteProductA1
class HawaiianPizza(Pizza):
    def cook(self):
        print("HawaiianPizza - ham & pineapple")


# ConcreteProductA2
class CheesePizza(Pizza):
    def cook(self):
        print("DeluxPizza - Cheddar & Mozzarella")


# AbstractProductB
class Chinese(metaclass=ABCMeta):
    @abstractmethod
    def cook(self):
        pass


# ConcreteProductB1
class Dumplings(Chinese):
    def cook(self):
        print("Dumplings - ham & pineapple")


# ConcreteProductB2
class MoonCake(Chinese):
    def cook(self):
        print("MoonCake - sesame seeds, ground lotus seeds and duck eggs")


"""
The CLIENT code below currently has to make too many decisions
and know all about the food choices

Change things by applying the ABSTRACT FACTORY pattern
so the client only has to decide the type of feast
and does not need to know the details of feast preparation.

To make things simpler can you please ..
get rid of the constants (too much to remember)
get rid of the case statements (too difficult to maintain)

"""
CHINESE = 1
PIZZA = 2


def feast(type):
    print("Main")
    main = None
    desert = None
    if type == PIZZA:
        main = CheesePizza()
    elif type == CHINESE:
        main = Dumplings()
    main.cook()
    print("Desert")
    if type == PIZZA:
        desert = HawaiianPizza()
    elif type == CHINESE:
        desert = MoonCake()
    desert.cook()


if __name__ == "__main__":
    print("***A Chinese feast***")
    feast(CHINESE)
    print("***A Pizza feast***")
    feast(PIZZA)
