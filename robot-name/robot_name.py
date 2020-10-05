from random import randint
from string import ascii_uppercase as ABC


def randomLetter():
    """Returns random uppercase letter"""
    return ABC[randint(0, len(ABC) - 1)]


class Robot:
    """Generate robots with random names"""

    prevNames = {}

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.__class__.newName()

    @classmethod
    def newName(cls):
        name = "{}{}{}".format(randomLetter(), randomLetter(), randint(100, 999))
        if name in cls.prevNames:  # dict key check is O(1)
            return cls.newName()

        # Only the key is meaningful so using None as value for less mem
        cls.prevNames[name] = None
        return name
