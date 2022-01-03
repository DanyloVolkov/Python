from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def usage(self):
        pass

class Coat(Clothing):
    @property
    def usage(self):
        return self.param / 6.5 + 0.5

class Suit(Clothing):
    @property
    def usage(self):
        return self.param * 2 + 0.3

coat = Coat(13)
suit = Suit(2.35)
print(coat.usage)
print(suit.usage)