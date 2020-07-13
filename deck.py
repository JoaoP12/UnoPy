from card import Card
from card import NormalCard
from card import SpecialCard
# from random import random
class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def draw_card(self):
        """
        Returns the top card of the deck to the
        player's cards.
        """
        has_cards = self.still_has_cards()
        if has_cards:
            card = self.cards.pop(-1)
            return card
        
        print("The deck is empty, you cannot take a card that isn't there\n")
        print("Creating new deck with the played cards...")
        
    def shuffle_deck(self):
        """
        Takes the self.cards list and shuffle using randint function.
        """
        pass
    
    def still_has_cards(self):
        """
        Returns False if the deck is empty, otherwise returns True
        """
        if self.cards is not None:
            return True
        
        return False
    
    def create_new_deck_with_played_cards(self):
        """
        It takes the played cards and create a new deck, then it shuffles the
        new deck and returns it.
        """
    
card1 = NormalCard('Green', 'One', 1)
card2 = NormalCard('Yellow', 'Seven', 7)
card3 = SpecialCard("Red", "Reverse", "Reverse")

new_deck = Deck([card1, card2, card3])
drown_card = new_deck.draw_card()
print(drown_card.card_name)
drown_card = new_deck.draw_card()
print(drown_card.card_name)
drown_card = new_deck.draw_card()
print(drown_card.card_name)
drown_card = new_deck.draw_card()


