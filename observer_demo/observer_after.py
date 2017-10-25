"""
>>> import observer_after
>>> oc = observer_after.OilCartel()
>>> shell = observer_after.OCShell()
>>> mobil = observer_after.OCMobil()
>>> caltex = observer_after.OCCaltex()
>>> challenge = observer_after.OCChallenge()
>>> oc.attach(shell)
>>> oc.attach(mobil)
>>> oc.attach(caltex)
>>> oc.attach(challenge)
>>> oc.price_fix(1.15, 1.17, 0.69)
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
    # Subject
    def __init__(self):
        self.all_companies = []

    def attach(self, observer):
        self.all_companies.append(observer)

    def detach(self, observer):
        self.all_companies.remove(observer)

    def notify(self):
        for subsidiary in self.all_companies:
            subsidiary.update(self)


class OilCartel(Cartel):
    # ConcreteSubject
    def __init__(self):
        Cartel.__init__(self)
        self.unleaded = 1.08
        self.hi_octane = 1.13
        self.diesel = 0.67

    def get_unleaded(self):
        return self.unleaded

    def get_hi_octane(self):
        return self.hi_octane

    def get_diesel(self):
        return self.diesel

    def price_fix(self, unleaded, hi_octane, diesel):
        self.unleaded = unleaded
        self.hi_octane = hi_octane
        self.diesel = diesel
        Cartel.notify(self)


class Observer(metaclass=ABCMeta):
    def __init__(self):
        self.unleaded = 0
        self.hi_octane = 0
        self.diesel = 0

    @abstractmethod
    def update(self, oil_cartel):
        pass


class OCShell(Observer):
    def update(self, oil_cartel):
        self.unleaded = oil_cartel.get_unleaded()
        self.hi_octane = oil_cartel.get_hi_octane()
        self.diesel = oil_cartel.get_diesel()
        self.report()

    def report(self):
        print("OCShell now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCMobil(Observer):
    def update(self, oil_cartel):
        self.unleaded = oil_cartel.get_unleaded()
        self.hi_octane = oil_cartel.get_hi_octane()
        self.diesel = oil_cartel.get_diesel()
        self.report()

    def report(self):
        print("OCMobil now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCCaltex(Observer):
    def update(self, oil_cartel):
        self.unleaded = oil_cartel.get_unleaded()
        self.hi_octane = oil_cartel.get_hi_octane()
        self.diesel = oil_cartel.get_diesel()
        self.report()

    def report(self):
        print("OCCaltex now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


class OCChallenge(Observer):
    def update(self, oil_cartel):
        self.unleaded = oil_cartel.get_unleaded()
        self.hi_octane = oil_cartel.get_hi_octane()
        self.diesel = oil_cartel.get_diesel()
        self.report()

    def report(self):
        print("OCChallenge now charges the following:")
        print("Unleaded : $" + str(self.unleaded) + " per litre.")
        print("High octane : $" + str(self.hi_octane) + " per litre.")
        print("Diesel : $" + str(self.diesel) + " per litre.")


def _test():
    # import doctest, observer_after
    import doctest
    return doctest.testmod(verbose=True)
    # import observer_after
    # return doctest.testmod(observer_after, verbose=True)


if __name__ == "__main__":
    _test()
