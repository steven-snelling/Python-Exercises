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


def create_unix_socket():
    print("create_unix_socket:")


def create_vms_socket():
    print("create_vms_socket:")


def create_nt_socket():
    print("create_nt_socket:")


def create_unix_pipe():
    print("create_unix_pipe:")


def create_vms_pipe():
    print("create_vms_pipe:")


def create_nt_pipe():
    print("create_nt_pipe:")


def create_unix_thread():
    print("create_unix_thread:")


def create_vms_thread():
    print("create_vms_thread:")


def create_nt_thread():
    print("create_nt_thread:")


def do_one_lane_ipc():
    if UNIX:
        create_unix_socket()
    elif VMS:
        create_vms_socket()
    elif NT:
        create_nt_socket()


def do_two_lane_ipc():
    if UNIX:
        create_unix_pipe()
    elif VMS:
        create_vms_pipe()
    elif NT:
        create_nt_pipe()


def do_parallel_processing():
    if UNIX:
        create_unix_thread()
    elif VMS:
        create_vms_thread()
    elif NT:
        create_nt_thread()


if __name__ == "__main__":
    VMS = 1
    UNIX = 0
    NT = 0
    do_one_lane_ipc()
    do_two_lane_ipc()
    do_parallel_processing()
    print("main: complete")

    """
    -- current output --
     create_vms_socket:
     create_vms_pipe:
     create_vms_thread:
     main: complete

     -- target output --
     VmsFactory: create_socket
     VmsFactory: create_pipe
     VmsFactory: create_thread
     main: complete
    """