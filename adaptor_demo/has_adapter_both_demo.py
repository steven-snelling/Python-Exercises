class Target(object):
    def request(self):
        return "Called Target Request()"


class Adaptee(object):
    def specific_request(self):
        return "Called SpecificRequest()"


class ClassAdapter(Target, Adaptee):
    def request(self):
        return self.specific_request()


class ObjectAdapter(Target):
    def __init__(self):
        self.__adaptee = Adaptee()

    def request(self):
        return self.__adaptee.specific_request()


if __name__ == '__main__':
    classAdapter = ClassAdapter()
    print(classAdapter.request())

    objectAdapter = ObjectAdapter()
    print(objectAdapter.request())
