""" Replace this text with your name please"""


class Fixture(object):
    def __init__(self, name):
        self.name = name

    def describe(self):
        print('\t' + self.name)


class Venue(object):
    def __init__(self, name):
        self.name = name
        self.additions = []

    def build(self, a_new_bit):
        self.additions.append(a_new_bit)

    def map(self):
        print(self.name)
        for addition in self.additions:
            if type(addition) == Fixture:
                addition.describe()
            elif type(addition) == Venue:
                addition.map()

if __name__ == '__main__':
    park = Venue('AMI Stadium')
    stand1 = Venue('Tui Stand')
    stand2 = Venue('Paul Kelly Motor Company Stand')
    stand3 = Venue('Hadlee Stand')

    park.build(stand1)
    park.build(stand2)
    park.build(stand3)

    stand1.build(Fixture('Toilets'))
    stand1.build(Fixture('Box 18'))
    stand1.build(Fixture('Box 19'))
    stand1.build(Fixture('Box 20'))
    stand1.build(Fixture('Box 21'))

    stand2.build(Fixture('Toilets'))
    for box in range(1, 18):
        stand2.build(Fixture('Box ' + str(box)))

    stand3.build(Fixture('Main Office'))

    park.map()

'''
expected output:

AMI Stadium
Tui Stand
    Toilets
    Box 18
    Box 19
    Box 20
    Box 21
Paul Kelly Motor Company Stand
    Toilets
    Box 1
    Box 2
    Box 3
    Box 4
    Box 5
    Box 6
    Box 7
    Box 8
    Box 9
    Box 10
    Box 11
    Box 12
    Box 13
    Box 14
    Box 15
    Box 16
    Box 17
Hadlee Stand
    Main Office
'''