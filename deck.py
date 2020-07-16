from card import Card
from card import NormalCard
from card import SpecialCard
from random import random
class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    
    def get_deck(self):
        """
        Returns the deck 'updated', after shuffling it.
        """
        self.shuffle_deck()
        return self.cards
        
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
        amount_of_cards_available = len(self.cards)
        indexes_shuffled = []
        deck_shuffled = []
        for i in range(amount_of_cards_available):
            num = random.randint(0, amount_of_cards_available)
            if num not in indexes_shuffled:
                indexes_shuffled.append(num)
        
        for i in range(amount_of_cards_available):
            deck_shuffled.append(self.cards[indexes_shuffled[i]])
        
        self.cards = deck_shuffled
            
        
    def still_has_cards(self):
        """
        Returns False if the deck is empty, otherwise returns True
        """
        if self.cards != []:
            return True
        
        return False
    
    def create_new_deck_with_played_cards(self, played_cards):
        """
        It takes the played cards and create a new deck, then it returns
        the self.get_deck() method that shuffles the deck and returns it
        """
        self.cards = played_cards
        return self.get_deck()
