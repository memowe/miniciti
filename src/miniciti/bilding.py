from anglr import Angle

class Bilding:

    floor_height = 3

    def __init__(self, stories=1, angle=Angle(90, "degrees")):
        self.stories    = stories
        self.angle      = angle

    def height(self):
        return self.stories * self.floor_height

    def is_upright(self):
        return self.angle == Angle(90, "degrees")
