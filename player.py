from zone import Deck, Discard, Hand, EndGamePile
#from gsc import GSC

class Player():
    def __init__(self, PID):
        self.PID = PID
        self.hand = Hand()
        self.deck = Deck()
        self.discard = Discard()
        self.end_game_pile = EndGamePile()

    def score(self):
        return 0

    def draw_hand(self, size=5):
        while self.hand.size() < size:
            pass

