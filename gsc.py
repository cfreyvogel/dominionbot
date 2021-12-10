#from player import Player
from effect import Effect
from board import Board
from zone import Zone, Supply, Trash
import cards.basic_cards 
import cards.base_set
from player import Player






class GameStateController:
    """The GSC is a singleton that controls the main gameplay. It handles instructional IO and can have any
    interfact built on top of it"""
    def __init__(self):
        self.players = [Player(0), Player(1)]
        self.trash = Trash()
        self.supply = Supply()
        self.zones = [self.trash, self.supply]
        self.current_player_index = 0
        self.current_player = self.players[0]
        self.money_count = 0
        self.buys = 0
        self.actions = 0
        self.AM = self.ActionManager(self)
        self.phase_manager = self.PhaseManager(self)
        self.temp_zone = Zone()
        self.board = Board()
        self.potential_actions = []
    
    class ActionManager:
        """Handles all Action IDs"""
        def __init__(self, GSC):
            self.GSC = GSC
            self.options = {
                'pass_phase': ([0,1,2,3], self.pass_phase)
            }
            banned_phrases = ['Card', 'basic_setup']
            for i in [cards.basic_cards,]:#, base_set]:
                print(i.__name__)
                print(dir(i))
                for j in list(filter(lambda x: x not in banned_phrases and '__' not in x, dir(i))):
                    self.temp_card = None
                    exec("self.temp_card = {}.{}()".format(i.__name__,j))
                    print(i, self.temp_card)
                    available_phases = []
                    # Card types sorted out here
                    # Phase numbers are defined in the PhaseManager and repeated here for convenience:
                    #0: 'action',
                    #1: 'buy',
                    #2: 'cleanup',
                    #3: 'night',
                    #4: 'temp'
                    if "Treasure" in self.temp_card._type:
                        available_phases.append(1)
                    if "Action" in self.temp_card._type:
                        available_phases.append(0)

                        
            #print(dir(basics))
        def pass_phase(self):
            self.GSC.phase_manager.goto_next_phase()

    class PhaseManager:
        """The phase manager handles passing between phases and contextualizes what cards actions are available"""
        def __init__(self, GSC):
            self.main_phases = {
                0: 'action',
                1: 'buy',
                2: 'cleanup',
                3: 'night',
                4: 'temp'
            }
            self.temp_phases = {  # each card may have its own phase if it's necessary
                0: 'discard' 
            }
            self.current_phase = 0
        def goto_next_phase(self):
            if self.current_phase in [0,1,2,3]:
                self.current_phase = (self.current_phase + 1) % 4

    def get_options(self):
        if self.current_phase == 0:
            pass
    
    def get_player_selection(self, choices, mandatory):
        choice = -1
        if not mandatory:
            print("pass: None")
        for i in range(len(choices)):
            print("{}, {}".format(i, choices[i]))
        while (choice < 0 or choice > len(choices) - 1) and choice != 'pass':
            choice = input("Enter your choice: ")
        return choice

    def get_player_selection_multiple(self, choices, mandatory):
        pass
    
    def setup(self):
        self.create_supply()
        
    def move_card(self, source_zone, target_zone, source_index=0, target_index=0):
        target_zone.insert(source_zone.draw(source_index), target_index)
    
    def pass_turn(self):
        self.money_count = 0
        self.current_player_index += 1 % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def create_supply(self, card_list=None):
        if not card_list:
            pass # default stuff goes here
        else:
            for k in card_list.keys():
                card_copy = card_list[k]() # a base class is passed here and created
                print("Adding: {} {}s".format(card_copy.base_amount, k))
                for i in range(card_copy.base_amount):
                    self.supply.insert(card_list[k](), k)
    
    def gain_money(self, amt=1):
        self.money_count += amt
    
    #def score(self, player_index):
    #    return players[player_index].score()
    
    def draw_card(self):
        if not self.current_player.deck.has_cards():
            self.reshuffle()
        self.move_card(self.current_player.deck, self.current_player.hand)
    
    def gain_action(self, amt=1):
        self.actions += amt

    def gain_buy(self, amt=1):
        self.buys += amt

    def reshuffle_player(self, player: Player):
        while player.discard.has_cards():
            self.move_card(player.discard, player.deck)
        player.deck.shuffle()

    def get_endgame_pile(self):
        return self.current_player.end_game_pile
    
    def initial_deck_setup(self):
        for p in self.players:
            for i in range(3):
                self.move_card(self.supply.cards['estate'], p.deck)
            for i in range(7):
                self.move_card(self.supply.cards['copper'], p.deck)
            p.deck.shuffle()

    def draw_card(self, player: Player):
        if not player.deck.size():
            self.reshuffle_player(player)
        self.move_card(player.deck, player.hand)
    
    def draw_hand(self, player: Player, amt: int = 5):
        for i in range(amt):
            self.draw_card(player)
            

global GSC
GSC = GameStateController()

