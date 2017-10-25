"""
>>> import observer_before
>>> oc = observer_before.OilCartel()
>>> shell = observer_before.OCShell()
>>> mobil = observer_before.OCMobil()
>>> caltex = observer_before.OCCaltex()
>>> challenge = observer_before.OCChallenge()
>>> oc.attach(shell)
>>> oc.attach(mobil)
>>> oc.attach(caltex)
>>> oc.attach(challenge)
>>> oc.priceFix(1.15, 1.17, 0.69)
OCShell now charges the following:
Unleaded : $1.15 per litre.
High octane : $1.17 per litre.
Diesel : $0.69 per litre.
OCMobil now charges the following:
Unleaded : $1.15 per litre.
High octane : $1.17 per litre.
Diesel : $0.69 per litre.
OCCaltex now charges the following:
Unleaded : $1.15 per litre.
High octane : $1.17 per litre.
Diesel : $0.69 per litre.
OCChallenge now charges the following:
Unleaded : $1.15 per litre.
High octane : $1.17 per litre.
Diesel : $0.69 per litre.
>>> oc.price_fix(1.19, 1.25, 0.81)
OCShell now charges the following:
Unleaded : $1.19 per litre.
High octane : $1.25 per litre.
Diesel : $0.81 per litre.
OCMobil now charges the following:
Unleaded : $1.19 per litre.
High octane : $1.25 per litre.
Diesel : $0.81 per litre.
OCCaltex now charges the following:
Unleaded : $1.19 per litre.
High octane : $1.25 per litre.
Diesel : $0.81 per litre.
OCChallenge now charges the following:
Unleaded : $1.19 per litre.
High octane : $1.25 per litre.
Diesel : $0.81 per litre.
"""

from abc import ABCMeta, abstractmethod


class Cartel(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.unleaded = None
        self.hi_octane = None
        self.diesel = None


class OilCartel(Cartel):
    def __init__(self):
        Cartel.__init__(self)

    def get_unleaded(self):
        return self.unleaded

    def get_hi_octane(self):
        return self.hi_octane

    def get_diesel(self):
        return self.diesel


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def update(self, cartel):
        pass


class OCShell(Observer):
    def __init__(self):
        super().__init__()
        self.unleaded = 0
        self.hi_octane = 0
        self.diesel = 0

    def report(self):
        print("OCShell now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCMobil(Observer):
    def __init__(self):
        super().__init__()
        self.unleaded = 0
        self.hi_octane = 0
        self.diesel = 0

    def report(self):
        print("OCMobil now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCCaltex(Observer):
    def __init__(self):
        super().__init__()
        self.unleaded = 0
        self.hi_octane = 0
        self.diesel = 0

    def report(self):
        print("OCCaltex now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCChallenge(Observer):
    def __init__(self):
        super().__init__()
        self.unleaded = 0
        self.hi_octane = 0
        self.diesel = 0

    def report(self):
        print("OCChallenge now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


def _test():
    # import doctest, observer_before
    import doctest
    return doctest.testmod(verbose=True)
    # import observer_before
    # return doctest.testmod(observer_before, verbose=True)


if __name__ == "__main__":
    _test()
