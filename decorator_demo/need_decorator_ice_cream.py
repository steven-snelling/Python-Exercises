# ----------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
# reference:   http://javapapers.com/design-patterns/decorator-pattern/
# Created:
# Copyright:
# Licence:     <your licence>
# ----------------------------------------------------------------------------
# !/usr/bin/env python


from abc import ABCMeta, abstractmethod


class IceCream(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    @staticmethod
    def make_ice_cream():
        pass


class SimpleIceCream(IceCream):
    @staticmethod
    def make_ice_cream():
        return "Base IceCream"


class Decorator(IceCream, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, ice_cream):
        super().__init__()
        self._component = ice_cream

    @abstractmethod
    def make_ice_cream(self):
        self._component.make_ice_cream()





class NuttyIceCream(SimpleIceCream):
    @staticmethod
    def make_nutty_ice_cream():
        return SimpleIceCream.make_ice_cream() + " + crunchy nuts"


class HoneyIceCream(SimpleIceCream):
    @staticmethod
    def make_honey_ice_cream():
        return SimpleIceCream.make_ice_cream() + " + sweet honey"


class NuttyHoneyIceCream(SimpleIceCream):
    @staticmethod
    def make_nutty_honey_ice_cream():
        return SimpleIceCream.make_ice_cream() + \
            " + sweet honey" + \
            " + crunchy nuts"

if __name__ == '__main__':
    simple_ice_cream = SimpleIceCream()
    print(simple_ice_cream.make_ice_cream())

    nutty_ice_cream = NuttyIceCream()
    print(nutty_ice_cream.make_nutty_ice_cream())

    honey_ice_cream = HoneyIceCream()
    print(honey_ice_cream.make_honey_ice_cream())

    nutty_honey_ice_cream = NuttyHoneyIceCream()
    print(nutty_honey_ice_cream.make_nutty_honey_ice_cream())
