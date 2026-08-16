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
    If the deck is empty, return 0 to signal that it is empty.

    This does NOT display the card name onscreen.'''
    assert(type(deck) == type([]))
    assert(type(discard_pile) == type([]))

    if len(deck) > 0:
        new_card = random.choice(deck)
        deck.remove(new_card)
        discard_pile.append(new_card)

        return new_card

    return 0

# Action 2: Reshuffle Deck
def reshuffle_deck(deck, discard_pile):
    '''Add each card from the discard pile back into the deck.
    Empty the discard pile. Return both lists.'''
    assert(type(deck) == type([]))
    assert(type(discard_pile) == type([]))

    deck = deck + discard_pile
    discard_pile = []

    return deck, discard_pile

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
    # SETUP: Setting up the deck and discard pile.
    deck = parse_json_list("deck.json")
    discard_pile = []
    next_step = None

    while next_step != "stop":
        print("Type the number of your desired action:")
        print("1. Draw a Card")
        print("2. Reshuffle Deck")
        print("3. Add Jokers")
        print("4. View Discard Pile")

        next_step = input("Choose your action: ")
        if next_step == "1":
            new_card = draw_card(deck, discard_pile)
            if new_card != 0:
                print(new_card)
            else:
                print("Deck empty. Please reshuffle.")
            move_on = input("Press ENTER to continue.")

        elif next_step == "2":
            deck, discard_pile = reshuffle_deck(deck, discard_pile)
            print("Deck Reshuffled!")

            move_on = input("Press ENTER to continue.")

        elif next_step == "3":
            add_jokers(deck)
            move_on = input("Press ENTER to continue.")

        elif next_step == "4":
            display_discard_pile(discard_pile)
            move_on = input("Press ENTER to continue.")

    print("Goodbye!")

    
main()



# Misc:
    # A function to add or remove any card by name.