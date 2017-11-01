"""
observer before
"""

from abc import ABCMeta


# Observer class
class Customer(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.new_release_name = ""


# Subject class
class VideoStore(object):
    def __init__(self):
        self.new_release_name = ""
        # tight coupling of a few Observers to the Subject!
        self.mike = Customer("Mike")
        self.mehdi = Customer("Mehdi")
        self.trevor = Customer("Trevor")
        self.malcolm = Customer("Malcolm")

    def set_new_release(self, new_release):
        # This part is also not very flexible!!!!
        self.mike.new_release_name = new_release
        self.mehdi.new_release_name = new_release
        self.trevor.new_release_name = new_release
        self.malcolm.new_release_name = new_release


def main():
    # Test
    # create a subject instance object.
    video_store = VideoStore()
    # do something customers/Observers need to know about
    video_store.set_new_release("Scary Movie 44")
    # do the customers know?
    print(video_store.mike.name + ": The new release is " +
          video_store.mike.new_release_name)
    print(video_store.mehdi.name + ": The new release is " +
          video_store.mehdi.new_release_name)
    print(video_store.trevor.name + ": The new release is " +
          video_store.trevor.new_release_name)
    print(video_store.malcolm.name + ": The new release is " +
          video_store.malcolm.new_release_name)
    # Challenge - add a new customer: Luofeng


if __name__ == '__main__':
    main()
