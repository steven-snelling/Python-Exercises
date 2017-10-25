"""
Steven Snelling
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


class Restaurant(metaclass=ABCMeta):
    @abstractmethod
    def make_main(self):
        pass

    @abstractmethod
    def make_desert(self):
        pass


class PizzaRestaurant(Restaurant):
    def make_main(self):
        return CheesePizza.cook(self)

    def make_desert(self):
        return HawaiianPizza.cook(self)


class ChineseRestaurant(Restaurant):
   def make_main(self):
       return Dumplings.cook(self)

   def make_desert(self):
        return MoonCake.cook(self)


def feast(factory):
    main = None
    desert = None

    print("Main")
    factory.make_main()

    print("Desert")
    factory.make_desert()


if __name__ == "__main__":
    print("***A Chinese feast***")
    feast(ChineseRestaurant())
    print("***A Pizza feast***")
    feast(PizzaRestaurant())
