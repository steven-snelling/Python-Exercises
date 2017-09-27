from abc import ABCMeta, abstractmethod

__author__ = 'xul'


class Component(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def add(self, component):
        pass

    @abstractmethod
    def traverse(self, level=0):
        pass


class File(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self.type = "File"

    def traverse(self, level=0):
        # print("\t"*level + self.name + "\t" + self.type)
        print('{}{}\t{}'.format('\t' * level, self.name, self.type))


class Folder(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self.children = []
        self.type = "Folder"

    def add(self, component):
        self.children.append(component)

    def traverse(self, level=0):
        # print("\t"*level + self.name + "\t" + self.type)
        print('{}{}\t{}'.format("\t" * level, self.name, self.type))
        for child in self.children:
            child.traverse(level + 1)


if __name__ == '__main__':
    fileSystem = Folder("Pools")
    next = Folder("FC")
    fileSystem.add(next)

    current = next
    next = Folder("School of Computing")
    current.add(next)

    current = next
    next = Folder("BICT")
    current.add(next)

    current = next
    next = Folder("PR301")
    current.add(next)
    next = File("TheSecretMessage.txt")
    current.add(next)

    fileSystem.traverse()
