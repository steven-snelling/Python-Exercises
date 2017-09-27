from abc import ABCMeta, abstractmethod

"""
Steven Snelling

TASK:   (1) redesign this system so it uses the BUILDER GOF pattern
        (2) add the additional option mentioned at the end
"""

# now obsolete
class HTMLDoc(object):
    def __init__(self):
        self.tokens = []

    def parse(self, text, type):
        """
        This design is inflexible.
        The case statement in this method
        will forever have to be edited and extended
        """
        if type == 'HEAD':
            self.tokens.append("<H1>" + text + "</H1>")
        elif type == 'FONT':
            self.tokens.append("<FONT>" + text + "</FONT>")
        elif type == 'PARA':
            self.tokens.append("<P>" + text + "</P>")


class AbstractBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.tokens = []

    @abstractmethod
    def add_font(self, text):
        pass

    @abstractmethod
    def add_head(self, text):
        pass

    @abstractmethod
    def add_para(self, text):
        pass


class HTMLBuilder(AbstractBuilder):
    def add_font(self, text):
        self.tokens.append("<FONT>" + text + "</FONT>")

    def add_head(self, text):
        self.tokens.append("<H1>" + text + "</H1>")

    def add_para(self, text):
        self.tokens.append("<P>" + text + "</P>")

    def get_result(self):
        return self.tokens


class JSONBuilder(AbstractBuilder):
    def add_font(self, text):
        self.tokens.append('"FONT"="' + text + '"')

    def add_head(self, text):
        self.tokens.append('"H1"="' + text + '"')

    def add_para(self, text):
        self.tokens.append('"P"="' + text + '"')

    def get_result(self):
        return self.tokens


class Writer(object):
    def __init__(self, builder):
        self.builder = builder

    def write(self):
        self.builder.add_font("timesRoman")
        self.builder.add_head("Once upon a time...")
        self.builder.add_para("There was a student doing a programming test")
        self.builder.add_para("It was hard")

if __name__ == "__main__":
    builder1 = HTMLBuilder()
    director = Writer(builder1)
    director.write()
    print(builder1.get_result())

    builder2 = JSONBuilder()
    director = Writer(builder2)
    director.write()
    print(builder2.get_result())



    # doc = HTMLDoc()
    # doc.parse("timesRoman", "FONT")
    # doc.parse("Once upon a time...", "HEAD")
    # doc.parse("There was a student doing a programming test.", "PARA")
    # doc.parse("It was hard", "PARA")
    # print(doc.tokens)
    # ['<FONT>timesRoman</FONT>', '<H1>Once upon a time...</H1>', '<P>There was a student doing a programming test.</P>', '<P>It was hard</P>']

    """
    additional functionality required is
    same input but JSON format output
    ['"FONT"="timesRoman"', '"H1"="Once upon a time"', '"P"="There was a student doing a programming test.", '"P"="It was hard"']
    """
