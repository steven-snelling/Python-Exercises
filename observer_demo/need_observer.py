from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value
        self.subject = None

    @abstractmethod
    def update(self, val):
        pass

    def set_subject(self, subject):
        self.subject = subject


class DivObserver(Observer):

    def update(self, val):
        print("{0} div {1} = {2}".format(
            val, self.value, val / self.value))


class ModObserver(Observer):

    def update(self, val):
        print("{0} mod {1} = {2}".format(
            val, self.value, val % self.value))


class AbstractSubject(metaclass=ABCMeta):

    def __init__(self):
        self.__observers = []

    def attach(self, obs):
        self.__observers.append(obs)

    def detach(self, obs):
        self.__observers.remove(obs)

    def notify(self):
        for o in self.__observers:
            o.update()




class Subject(AbstractSubject):
    def __init__(self):
        self.div_obj = DivObserver(4)
        self.mod_obj = ModObserver(3)
        self.value = None

    def set_value(self, value):
        self.value = value
        self.notify()




if __name__ == '__main__':
    subj = Subject()
    subj.set_value(14)
