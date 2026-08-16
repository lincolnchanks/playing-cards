import json
import random

# PSEUDOCODE:

# Deck setup: Read data from the deck.json file into a new list.

def parse_json_list(filename):
    '''Turn a JSON file, formatted as a list, into a list.'''
    assert(type(filename) == type(""))
    assert(filename.endswith(".json"))

    with open(filename, "rt") as filehandle:
        deck_data = json.loads(filehandle.read())

    deck = deck_data["deck"]
    assert(type(deck) == type([]))
    for card in deck:
        assert(type(card) == type(""))

    return deck

# Open a menu for the player to choose actions.

# Action 1: Draw a Card
def draw_card(deck, discard_pile):
    '''Pick a random card from the deck list. Remove it from the
    deck and append it to the discard pile. Return it.

    This does NOT display the card name onscreen.'''
    assert(type(deck) == type([]))
    assert(type(discard_pile) == type([]))

    if len(deck) > 0:
        new_card = random.choice(deck)
        deck.remove(new_card)
        discard_pile.append(new_card)

        print(new_card)
        print(deck)
        print(discard_pile)

        return new_card

# Action 2: Reshuffle Deck
def reshuffle_deck(deck, discard_pile):
    '''Add each card from the discard pile back into the deck.
    Empty the discard pile.'''
    assert(type(deck) == type([]))
    assert(type(discard_pile) == type([]))

    deck = deck + discard_pile
    discard_pile = []

# Action 3: Add Jokers
def add_jokers(deck):
    '''Add "Red Roker" and "Black Joker" to the deck list.'''
    assert(type(deck) == type([]))

    deck.append("Red Joker")
    deck.append("Black Joker")

# Action 4: View Discard Pile
def display_discard_pile(discard_pile):
    '''Displays the Discard Pile.'''
    assert(type(discard_pile) == type([]))

    print(discard_pile)


def main():
    print("Hello world")
    deck = parse_json_list("deck.json")
    discard_pile = []
    # for card in deck:
    #     print(card)

    new_card1 = draw_card(deck, discard_pile)
    new_card2 = draw_card(deck, discard_pile)
    new_card3 = draw_card(deck, discard_pile)

    print(new_card1)
    print(new_card2)
    print(new_card3)

    print("RESHUFFLING:")

    reshuffle_deck(deck, discard_pile)

    add_jokers(deck)

    print(deck)

    draw_card(deck, discard_pile)
    draw_card(deck, discard_pile)
    draw_card(deck, discard_pile)
    draw_card(deck, discard_pile)
    draw_card(deck, discard_pile)

    display_discard_pile(discard_pile)

    
main()



# Misc:
    # A function to add or remove any card by name.