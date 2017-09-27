""" Example of BEFORE applying composite pattern """


class Primitive(object):
    def __init__(self, val):
        self.value = val
        self.type = "LEAF"

    def report_type(self):
        return self.type

    def print_val(self):
        # result = str(self.value) + "\t" + self.type
        # print('\t' + result)
        print('\t{}\t{}'.format(self.value, self.type))


class Composite(object):
    def __init__(self, val):
        self.value = val
        self.type = "INTERIOR"
        self.children = []

    def report_type(self):
        return self.type

    def add(self, composite):
        self.children.append(composite)

    def traverse(self):
        # print(str(self.value) + "\t" + self.type)
        print('{}\t{}'.format(self.value, self.type))
        for eachChild in self.children:
            if eachChild.report_type() == "LEAF":
                eachChild.print_val()
            elif eachChild.report_type() == "INTERIOR":
                eachChild.traverse()

if __name__ == '__main__':
    first = Composite(1)
    second = Composite(2)
    third = Composite(3)

    first.add(second)
    first.add(third)
    first.add(Primitive(4))
    second.add(Primitive(5))
    second.add(Primitive(6))
    third.add(Primitive(7))
    first.traverse()
