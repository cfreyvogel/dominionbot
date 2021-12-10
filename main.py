from gsc import GSC
import cards.basic_cards as basics
import cards.base_set as base_set
import text_interface

def test_setup():
    # add cards to supply
    cards_to_add = basics.basic_setup
    cards_to_add['smithy'] = base_set.Smithy

    GSC.create_supply(cards_to_add)
    GSC.initial_deck_setup()
    
    GSC.draw_hand(GSC.players[0])
    GSC.draw_hand(GSC.players[1])
    player_one_interface = text_interface.TextInterface(GSC.players[0])

    
test_setup()