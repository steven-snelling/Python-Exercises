"""
observer after by Steven Snelling
"""

from abc import ABCMeta, abstractmethod


# abstract Observer class
class Observer(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.new_release_name = ""
        self.store = None

    def set_store(self, store):
        self.store = store

    @abstractmethod
    def update(self):
        pass


# concreate observer
class Customer(Observer):
    def update(self):
        new_release = self.store.get_new_release()
        self.new_release_name = new_release


# abstract subject
class Store(metaclass=ABCMeta):
    def __init__(self):
        self.customers = []

    def attach(self, observ):
        self.customers.append(observ)

    def detach(self, observ):
        self.customers.remove(observ)

    def notify(self):
        for obs in self.customers:
            obs.update()


# concrete Subject class
class VideoStore(Store):
    def __init__(self):
        super().__init__()
        self.new_release_name = ""

    def set_new_release(self, new_release):
        self.new_release_name = new_release

    def get_new_release(self):
        return self.new_release_name


def main():
    # Test
    # create a subject instance object.
    video_store = VideoStore()
    # tight coupling of a few Observers to the Subject! - resolved
    customer1 = Customer("Mike")
    customer1.set_store(video_store)

    customer2 = Customer("Mehdi")
    customer2.set_store(video_store)

    customer3 = Customer("Trevor")
    customer3.set_store(video_store)

    customer4 = Customer("Malcolm")
    customer4.set_store(video_store)

    customer5 = Customer("Luofeng")
    customer5.set_store(video_store)

    video_store.attach(customer1)
    video_store.attach(customer2)
    video_store.attach(customer3)
    video_store.attach(customer4)
    video_store.attach(customer5)

    # do something customers/Observers need to know about
    video_store.set_new_release("Scary Movie 44")
    video_store.notify()

    # do the customers know?

    for customer in video_store.customers:
        print(customer.name + ": The new release is " + customer.new_release_name)

    video_store.set_new_release("Avengers 6")
    video_store.notify()

    for customer in video_store.customers:
        print(customer.name + ": The new release is " + customer.new_release_name)


if __name__ == '__main__':
    main()
