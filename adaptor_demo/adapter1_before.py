class Shape(object):
    def __init__(self):
        pass

    def whatami(self):
        print("\nI am a Shape")

    def bounding_box(self, top, left, bottom, right):
        print("My TopLeft co-ordinate is " + str(top) + "," + str(left))
        print("My BottomRight co-ordinate is " + str(bottom) + "," + str(right))


class TextView(object):
    def __init__(self):
        pass

    def whatami(self):
        print("\nI am a TextView")

    def get_origin(self, top, left):
        print("My TopLeft co-ordinate is " + str(top) + "," + str(left))

    def get_extent(self, width, height):
        print("My Width is " + str(width))
        print("My Height is " + str(height))


class TextShape(Shape):
    def __init__(self):
        self.text_view = TextView()

    def bounding_box(self, top, left, bottom, right):
        print("i am an Adaptor")
        print("This is my BoundingBox procedure which outputs TextView")

        width = right - left
        height = bottom - top

        self.text_view.get_origin(top, left)
        self.text_view.get_extent(width, height)


if __name__ == '__main__':
    myshape = Shape()
    myshape.whatami()
    myshape.bounding_box(6, 6, 60, 60)

    mytext = TextView()
    mytext.whatami()
    mytext.get_origin(5, 5)
    mytext.get_extent(50, 50)

    # write an adapter that makes the next two lines work
    mytextshape = TextShape()
    mytextshape.bounding_box(8, 8, 80, 80)
