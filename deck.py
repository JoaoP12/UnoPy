from card import Card
from card import NormalCard
from card import SpecialCard
# from random import random
class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def draw_card(self):
        """
        Returns the top card of the deck to the player's cards.
        
        P.S.: This function will never be called if the deck is empty.
        That will be more understandable when the class Game be implemented.
        That class will check if it has cards on the deck, and if doesn't, it
        will call the create_new_deck_with_played_cards method.
        """
        
        return self.cards.pop(-1)
        
    def shuffle_deck(self):
        """
        Takes the self.cards list and shuffle using randint function.
        """
        pass
    
    def still_has_cards(self):
        """
        Returns False if the deck is empty, otherwise returns True
        """
        if self.cards != []:
            return True
        
        return False
    
    def create_new_deck_with_played_cards(self, played_cards):
        """
        It takes the played cards and create a new deck, then it shuffles the
        new deck and returns it.
        """
        pass
    
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


