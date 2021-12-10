#print(__name__)
#
#import sys
#$sys.path.append("..")

from .card import Card
#from ..gsc import GSC

class Copper(Card):
    def __init__(self):
        super().__init__("Copper", ["Treasure"], 0, "$1")
        self.base_amount = 60
    def on_play(self, GSC):
        GSC.gain_money(1)
    
class Silver(Card):
    def __init__(self):
        super().__init__("Silver", ["Treasure"], 3, "$2")
        self.base_amount = 40
    def on_play(self, GSC):
        GSC.gain_money(2)
    
class Gold(Card):
    def __init__(self):
        super().__init__("Gold", ["Treasure"], 6, "$3")
        self.base_amount = 30
    def on_play(self, GSC):
        GSC.gain_money(3)

class Estate(Card):
    def __init__(self):
        super().__init__("Estate", ["Victory"], 2, "1 VP")
        self.base_amount = 14
    def score(self):
        return 1

class Duchy(Card):
    def __init__(self):
        super().__init__("Duchy", ["Victory"], 5, "3 VP")
        self.base_amount = 8
    def score(self):
        return 3

class Province(Card):
    def __init__(self):
        super().__init__("Province", ["Victory"], 8, "6 VP")
        self.base_amount = 8
    def score(self):
        return 6

class Curse(Card):
    def __init__(self):
        super().__init__("Curse", ["Curse"], 0, "-1 VP")
    def score(self):
        return -1

basic_setup = {
    'copper': Copper,
    'silver': Silver,
    'gold': Gold,
    'estate': Estate,
    'duchy': Duchy,
    'province': Province,
    'curse': Curse
}