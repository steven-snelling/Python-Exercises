"""
Purpose.  Builder - NOT!
This monolithic design supports a single representation.
"""


class Array(object):
    def __init__(self):
        self.lst = []

    def add_front(self, ch):
        self.lst.insert(0, ch)

    def add_back(self, ch):
        self.lst.append(ch)

    def traverse(self):
        print("\n",)
        for item in self.lst:
            print(item, end=" ")


if __name__ == "__main__":
    input_data = ("fa", "bb", "fc", "bd", "fe", "bf", "fg", "bh")

    list = Array()

    for item in input_data:
        if item[0] == 'f':
            list.add_front(item[1])
        elif item[0] == 'b':
            list.add_back(item[1])
    list.traverse()

    """
    Expected output:
    g e c a b d f h
    """
