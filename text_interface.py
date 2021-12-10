from gsc import GSC
from player import Player
class TextInterface:
    def __init__(self, player: Player):
        self.player = player

    def get_actions(self):
        return self.player.hand.get_indices_by_tag("Action")

    def get_treasures(self):
        return self.player.hand.get_indices_by_tag("Treasure")
    
class TextMenu:
    def __init__(self, options_dict: dict):
        self.options_dict = options_dict

    