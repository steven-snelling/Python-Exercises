"""
Purpose.  Abstract Factory design pattern lab.
 
Problem.
case statements are spread throughout the code to accommodate 3 different
porting targets. This makes maintenance difficult, and porting to a 4th
platform onerous.

Assignment.
 1. Create an abstract base class Factory.
 2. In this base Factory class define member functions createSocket(),
    createPipe(), and createThread(). All are 'pass' abstract functions.
 3. Subclass UnixFactory, VmsFactory, and NtFactory off of Factory.
 4. Refactor the "create" functions to be member functions of one of
    the Factory derived classes.
 5. Declare a factory pointer local to "__main__"
 6. Use a single if case statement in "__main__" to instantiate the desired
    Factory derived class.
 7. Do not optimize-out the doOneLaneIPC(), doTwoLaneIPC(), and
    doParallelProcessing() free functions.
 8. Pass the Factory pointer to each of these free functions so that they
    can create sockets, pipes, and threads without regard to race, creed,
    or platform.
 9. Extra credit: implement the Factory class as a Singleton.
"""

from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_socket(self):
        pass

    @abstractmethod
    def create_pipe(self):
        pass

    @abstractmethod
    def create_thread(self):
        pass


class UnixFactory(Factory):
    def create_socket(self):
        print("UnixFactory: create_socket:")

    def create_pipe(self):
        print("UnixFactory: create_pipe:")

    def create_thread(self):
        print("UnixFactory: create_thread:")


class NtFactory(Factory):
    def create_socket(self):
        print("NtFactory: create_socket:")

    def create_pipe(self):
        print("NtFactory: create_pipe:")

    def create_thread(self):
        print("NtFactory: create_thread:")


class VmsFactory(Factory):
    def create_socket(self):
        print("VmsFactory: create_socket:")

    def create_pipe(self):
        print("VmsFactory: create_pipe:")

    def create_thread(self):
        print("VmsFactory: create_thread:")


def do_one_lane_ipc(factory):
    factory.create_socket()


def do_two_lane_ipc(factory):
    factory.create_pipe()


def do_parallel_processing(factory):
    factory.create_thread()


if __name__ == "__main__":
    VMS = True
    UNIX = False
    NT = False
    f = None
    if UNIX:
        f = UnixFactory()
    elif VMS:
        f = VmsFactory()
    elif NT:
        f = NtFactory()
    do_one_lane_ipc(f)
    do_two_lane_ipc(f)
    do_parallel_processing(f)
    print("main: complete")

    """
     VmsFactory: create_socket
     VmsFactory: create_pipe
     VmsFactory: create_thread
     main: complete
    """