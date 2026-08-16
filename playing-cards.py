import random

# PSEUDOCODE:

# Deck setup: Read data from the deck.json file into a new list.

# Open a menu for the player to choose actions.

# Action 1: Draw a Card

    # Pick a random card from the deck list. Remove it from the deck list and append it
    # to the discard pile list.
    # Display the card name on the screen.

# Action 2: Reshuffle Deck

    # Option 1:
        # Add each card from the discard pile list to the deck list. Empty the discard pile list.
    # Option 2:
        # Re-copy the deck list from deck.json, then empty the discard pile.

# Action 3: Add Jokers

    # Add "Red Joker" and "Black Joker" to the deck list.

# Action 4: View Discard Pile

    # Display each card in the discard pile.


def main():
    print("Hello world")

main()



# Misc:
    # A function to add or remove any card by name.