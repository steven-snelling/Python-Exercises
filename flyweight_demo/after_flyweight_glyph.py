# -----------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      xul
#
# Created:     12:15 PM 29/05/15
# Copyright:   (c) xul 12:15 PM 29/05/15
# Licence:     <your licence>
# -----------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Context(object):
    def __init__(self, position, style_info=set()):
        self.index = position
        self.style_info = style_info

    def __add__(self, other):
        return Context(self.index,
                       self.style_info | other.style_info)


class GlyphFlyweight(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, context):
        pass


class CharacterFlyweight(GlyphFlyweight):
    def __init__(self, char):
        self.__char_code = char

    def draw(self, context):
        return 'Char {} {} at Position {:2d} with Style {}'. \
            format(self.__char_code, self,
                   context.index, sorted(context.style_info))


class Row(GlyphFlyweight):
    def __init__(self, context=None):
        self.__children = {}
        self.__context = context

    def add_child(self, child, context):
        self.__children[context.index] = [child, context]

    def draw(self, context):
        self.__context = context
        apparent = ''
        for position in sorted(self.__children.keys()):
            if self.__context is not None:
                apparent += self.__children[position][0].draw(
                    self.__children[position][1] + self.__context) + "\n"
        return apparent


class FlyweightFactory(object):
    def __init__(self):
        self.__characters = {}

    def create_character(self, char):
        if char not in self.__characters:
            self.__characters[char] = CharacterFlyweight(char)
        return self.__characters[char]

    @staticmethod
    def create_row(context=None):
        return Row(context)

if __name__ == '__main__':
    def get_random_style():
        from random import random
        from math import floor
        final_style = set()
        styles = ["Times", "Underline", "Green", "Italic", "Bold"]
        for _ in range(len(styles)):
            final_style |= {styles[floor(random() * len(styles))]}
        return final_style

    f = FlyweightFactory()
    row = f.create_row()

    text = "Flyweight is a pattern"
    for index in range(len(text)):
        row.add_child(f.create_character(text[index]),
                      Context(index, get_random_style()))

    print(row.draw(Context(0, {"12"})))
