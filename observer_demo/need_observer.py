class DivObserver(object):
    def __init__(self, value):
        self.value = value

    def update(self, val):
        print("{0} div {1} = {2}".format(
            val, self.value, val / self.value))


class ModObserver(object):
    def __init__(self, value):
        self.value = value

    def update(self, val):
        print("{0} mod {1} = {2}".format(
            val, self.value, val % self.value))


class Subject(object):
    def __init__(self):
        self.div_obj = DivObserver(4)
        self.mod_obj = ModObserver(3)
        self.value = None

    def set_value(self, value):
        self.value = value
        self.notify()

    def notify(self):
        self.div_obj.update(self.value)
        self.mod_obj.update(self.value)


if __name__ == '__main__':
    subj = Subject()
    subj.set_value(14)
