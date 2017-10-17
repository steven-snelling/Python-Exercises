from abc import ABCMeta, abstractmethod


class VisualComponent(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self):
        pass


class TextView(VisualComponent):
    def __init__(self, text):
        super().__init__()
        self._text = text

    def draw(self):
        print("Drawing a TextView... ", self._text)

    def resize(self):
        print("Resizing a text view")


class Decorator(VisualComponent, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, visual_component):
        super().__init__()
        self._component = visual_component

    @abstractmethod
    def draw(self):
        self._component.draw()

    @abstractmethod
    def resize(self):
        self._component.resize()


class BorderDecorator(Decorator):
    def __init__(self, visual_component, border_width):
        super().__init__(visual_component)
        # self._component = visual_component
        self._width = border_width

    def draw(self):
        Decorator.draw(self)
        self.draw_border()

    def resize(self):
        Decorator.resize(self)
        print("Resizing a border")

    def draw_border(self):
        print("Drawing a border of width %s " % self._width)


class Window(object):
    def __init__(self):
        self._component = None

    def set_contents(self, visual_component):
        print("Set Window contents")
        self._component = visual_component

    def draw(self):
        self._component.draw()

    def resize(self):
        self._component.resize()


if __name__ == "__main__":
    window = Window()
    textView = TextView("Hello, I'm a TextView")
    borderDecorator = BorderDecorator(textView, 1)
    window.set_contents(borderDecorator)
    window.draw()
    window.resize()
