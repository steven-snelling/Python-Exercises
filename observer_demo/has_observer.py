from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):  # an Observer
    def __init__(self, value):
        self.value = value
        self.subj = None
        self.state = None

    @abstractmethod
    def update(self):
        pass

    def set_subject(self, subj):
        self.subj = subj


class DivObserver(Observer):  # a ConcreteObserver
    def update(self):
        val = self.subj.get_state()
        self.state = val / self.value
        print("{0} div {1} = {2}".format(val, self.value, self.state))


class ModObserver(Observer):  # a ConcreteObserver
    def update(self):
        val = self.subj.get_state()
        self.state = val % self.value
        print("{0} mod {1} = {2}".format(val, self.value, self.state))


class AbstractSubject(metaclass=ABCMeta):  # a Subject
    def __init__(self):
        self.__observers = []

    def attach(self, obs):
        self.__observers.append(obs)

    def detach(self, obs):
        self.__observers.remove(obs)

    def notify(self):
        for obs in self.__observers:
            obs.update()


class Subject(AbstractSubject):  # a ConcreteSubject
    def __init__(self):
        AbstractSubject.__init__(self)
        self.__value = None

    def set_value(self, value):
        self.__value = value
        self.notify()

    def get_state(self):
        return self.__value


if __name__ == '__main__':
    subj = Subject()
    div_observer = DivObserver(4)
    div_observer.set_subject(subj)
    subj.attach(div_observer)

    mod_observer = ModObserver(3)
    mod_observer.set_subject(subj)
    subj.attach(mod_observer)

    subj.set_value(14)
