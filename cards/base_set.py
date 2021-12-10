from .card import Card


# Cost two
class Cellar(Card):
    pass

class Chapel(Card):
    pass

class Moat(Card):
    pass

# Cost three
class Harbinger(Card):
    def __init__(self):
        super().__init__("Harbinger", ["Action"], 4, "+1 Card, +1 Action, Look through your discard pile. You may put a card from it onto your deck.")
    def on_play(self, GSC):
        GSC.draw_card()
        GSC.gain_action()
        target = GSC.get_player_selection(GSC.current_player.discard, False)
        GSC.move_card(GSC.current_player.discard, GSC.current_player.deck, target, 0)

class Merchant(Card):
    pass

class Vassal(Card):
    pass

class Village(Card):
    def __init__(self):
        super().__init__("Village", ["Action"], 3, "+1 Card, +2 Actions")
    def on_play(self, GSC):
        GSC.draw_card()
        GSC.gain_action(2)

class Workshop(Card):
    pass

# Cost four

class Bureaucrat(Card):
    pass

class Garden(Card):
    def __init__(self):
        super().__init__("Garden", ["Victory"], 8, "Worth 1 VP per 10 cards in your deck")
    def score(self):
        return GSC.get_endgame_pile().size() // 10
    
class Militia(Card):
    pass

class Moneylender(Card):
    pass

class Poacher(Card):
    pass

class Remodel(Card):
    pass

class Smithy(Card):
    def __init__(self):
        super().__init__("Smithy", ["Action"], 4, "+3 Cards")
    def on_play(self, GSC):
        for i in range(3):
            GSC.draw_card()

class ThroneRoom(Card):
    pass

# Cost five

class Bandit(Card):
    pass

class CouncilRoom(Card):
    pass

class Festival(Card):
    def __init__(self):
        super().__init__("Festival", ["Action"], 5, "+2 Actions, +1 Buy, $2")
    def on_play(self, GSC):
        GSC.gain_action(2)
        GSC.gain_buy()
        GSC.gain_money(2)

class Laboratory(Card):
    def __init__(self):
        super().__init__("Laboratory", ["Action"], 3, "+2 Cards, +1 Actions")
    def on_play(self, GSC):
        GSC.draw_card()
        GSC.draw_card()
        GSC.gain_action(1)

class Library(Card):
    pass

class Market(Card):
    def __init__(self):
        super().__init__("Market", ["Action"], 5, "+1 Card, +1 Actions, +1 Buy, $1")
    def on_play(self, GSC):
        GSC.draw_card()
        GSC.gain_action()
        GSC.gain_buy()
        GSC.gain_money(1)

class Mine(Card):
    pass

class Sentry(Card):
    pass

class Witch(Card):
    pass

# Cost six
class Artisan(Card):
    pass









