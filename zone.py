from cards.card import Card
from random import shuffle

class Zone:
    def __init__(self):
        self.cards = []
    def __str__(self):
        return str(self.cards)
    def size(self):
        return len(self.cards)
    def has_cards(self):
        return self.size() > 0
    def draw(self, index=0):
        return self.cards.pop(index)
    def shuffle(self):
        shuffle(self.cards)
    def insert(self, to_insert: Card, index=None):
        if not index:
            self.cards.insert(len(self.cards), to_insert)
        else:
            self.cards.insert(index, to_insert)
    def get_contents(self):
        return [x.name for x in self.cards]
    def get_indices_by_tag(self, tag):
        is_tagged = lambda x: tag in x._type
        indices = [idx for idx, ele in enumerate(self.cards) if is_tagged(ele)] 
        return indices

class Supply(Zone):
    def __init__(self):
        self.cards = {}
    def insert(self, to_insert: Card, pile: str):
        if not pile in self.cards.keys():
            print("Creating new pile: {}".format(pile))
            self.cards[pile] = Deck()
        self.cards[pile].insert(to_insert)
        
    def get_indices_by_tag(self, target, tag):
        return target.get_indices_by_tag(tag)
    def draw(self, pile):
        return self.cards[pile].pop()
    def size(self, pile=None):
        if pile:
            return self.cards[pile].size()
        else:
            return sum([self.size(i) for i in self.cards.keys()])
    def has_cards(self, pile):
        return self.cards[pile].size(pile) > 0
    def game_ending(self):
        return sum([self.has_cards(i) for i in self.cards.keys()]) >= 3
    def shuffle(self):
        print("Function disabled, why would you need to shuffle an unordered pile?")
    def get_contents(self):
        to_ret = {}
        for i in sorted(self.cards.keys()):
            to_ret[i] = self.cards[i].size()
        return to_ret

class Trash(Zone):
    pass

class Play(Zone):
    pass

class Hand(Zone):
    pass

class Deck(Zone):
    pass

class Discard(Zone):
    pass

class EndGamePile(Zone):
    def score(self):
        sc = 0
        for card in self.cards:
            if "victory" in card._type or "curse" in card._type:
                sc += card.score()
        return sc