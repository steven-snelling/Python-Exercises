from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        count = 0
        for observer in self.observers:
            observer.update()
            count += 1
        print(str(count) + " observers notified")


class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.subject_state = ""

    def get_state(self):
        return self.subject_state

    def set_state(self, new_state):
        self.subject_state = new_state
        print("\nConcreteSubject has CHANGED")
        self.notify_observers()


class Observer(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.subject = None

    @abstractmethod
    def update(self):
        pass

    def set_subject(self, new_subject):
        self.subject = new_subject


class ConcreteObserver(Observer):
    def __init__(self, name):
        Observer.__init__(self, name)
        self.observer_state = ""

    def update(self):
        self.observer_state = self.subject.get_state()
        print(self.name + " updated to " + self.observer_state)


if __name__ == '__main__':
    # test
    # create a subject and some observers, and set their relationships
    cs = ConcreteSubject()
    for i in range(1, 11):
        o = ConcreteObserver("observer " + str(i))
        cs.attach(o)
        # o.subject = cs
        o.set_subject(cs)

    # change the state of the subject, observers will be notified
    for i in range(1, 4):
        cs.set_state("subject state " + str(i))

    print("**********end observer test************")
