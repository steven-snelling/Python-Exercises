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
XHTML = 1
HTML = 2


def markup(type, text):
    start_tag = end_tag = None
    if type == XHTML:
        start_tag = StartParaTag()
    elif type == HTML:
        start_tag = StartP()
    if type == XHTML:
        end_tag = EndParaTag()
    elif type == HTML:
        end_tag = End()
    print(start_tag.show() + text + end_tag.show())


if __name__ == "__main__":
    print("***xhtml***")
    markup(XHTML, "This is a test")
    markup(XHTML, "This is a another test")
    print("***html***")
    markup(HTML, "This is a test")
    markup(HTML, "This is a another test")
