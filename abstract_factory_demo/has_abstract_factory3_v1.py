"""
REPLACE THIS LINE WITH YOUR NAME
"""

from abc import ABCMeta, abstractmethod


# There are two families of related products
# AbstractProductA
class XHTMLTag(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass


# ConcreteProductA1
class StartParaTag(XHTMLTag):
    def show(self):
        return "<p>"


# ConcreteProductA2
class EndParaTag(XHTMLTag):
    def show(self):
        return "</p>"


# AbstractProductB
class HTMLTag(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass


# ConcreteProductB1
class StartP(HTMLTag):
    def show(self):
        return "<P>"


# ConcreteProductB2
class End(HTMLTag):
    def show(self):
        return ""


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


class BaseAbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_start(self):
        pass

    @abstractmethod
    def make_end(self):
        pass


class XHTMLFactory(BaseAbstractFactory):
    def make_start(self):
        return StartParaTag()

    def make_end(self):
        return EndParaTag()


class HTMLFactory(BaseAbstractFactory):
    def make_start(self):
        return StartP()

    def make_end(self):
        return End()


def markup(factory, text):
    start_tag = factory.make_start()
    end_tag = factory.make_end()
    print(start_tag.show() + text + end_tag.show())


if __name__ == "__main__":
    print("***xhtml***")
    markup(XHTMLFactory(), "This is a test")
    markup(XHTMLFactory(), "This is a another test")
    print("***html***")
    markup(HTMLFactory(), "This is a test")
    markup(HTMLFactory(), "This is a another test")
