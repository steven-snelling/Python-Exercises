# Tasks
# 1. use class adapter to charge iPod battery with EuropeanSocket
# by Steven Snelling


class NewZealandSocket(object):
    def turn_on(self):
        print("Socket on")

    def turn_off(self):
        print("Socket off")

    def get_electricity(self):
        print("Power")


class EuropeanSocket(object):
    def schakel_in(self):  # turn on
        print("Aan geschakel")

    def schakel_uit(self):  # turn off
        print("Uit geschakel")

    def krijg_eleltriciteit(self):  # get electricity
        print("electriciteit")


class IPod(object):
    def __init__(self, power_point_type):
        self.power_point = power_point_type

    def charge_battery(self):
        print("Charging battery")
        self.power_point.turn_on()
        self.power_point.get_electricity()
        self.power_point.turn_off()


class SocketAdaptor(NewZealandSocket):

    def __init__(self):
        self.socket = EuropeanSocket()

    def turn_on(self):
        self.socket.schakel_in()

    def turn_off(self):
        self.socket.schakel_uit()

    def get_electricity(self):
        self.socket.krijg_eleltriciteit()


if __name__ == '__main__':
    a_ipod = IPod(NewZealandSocket())
    a_ipod.charge_battery()

    b_ipod = IPod(SocketAdaptor())
    b_ipod.charge_battery()