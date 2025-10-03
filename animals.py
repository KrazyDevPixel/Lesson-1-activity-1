#import necceseyry modules
from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def move(self):
        pass
class human(Animals):
    def move(self):
        print("I can WALK AND TALK")
class Dog(Animals):
    def move(self):
        print("I can BARK WOOF")
class Snake(Animals):
    def move(self):
        print("I can SLITHER")
class Lion(Animals):
    def move(self):
        print("I can ROAR[hertywhfsdgsyefwefgbuwehuifhgteg]")
R=human()
R.move()
K=Dog()
K.move()
R=Snake()
R.move()
K=Lion()
K.move()