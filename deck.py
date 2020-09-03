from card import Card
from card import NormalCard
from card import SpecialCard
from random import shuffle


class Deck:
    def __init__(self, cards):
        self._cards = cards
        
    def draw_card(self):
        """
        Returns the top card of the deck to the player's cards.
        
        If the deck has no more cards, it raises the exception NoMoreCards.
        """
        if self.is_empty():
            raise NoMoreCardsError
            
        else:
            return self._cards.pop(-1)
        
    def shuffle_deck(self):
        """
        Takes the self.cards list and shuffle using shuffle function.
        """
        shuffle(self._cards)
            
        
    def is_empty(self):
        """
        Returns True if the deck is empty, otherwise returns False
        """
        if self._cards == []:
            return True
        
        return False
    
    def create_new_deck_with_played_cards(self, played_cards):
        """
        It takes the played cards and create a new deck, then it returns
        an instance of itself with the new deck
        """
        print("Creating new deck with the cards played...\n")
        self._cards = played_cards
        self.shuffle_deck()
        return Deck(self._cards)

import unittest

class TestDeck(unittest.TestCase):
    def test_empty_deck(self):
        deck = Deck([])
        self.assertListEqual(deck._cards, [])

    def test_deck_with_cards(self):
        deck = Deck([1,2,3,4,5])
        self.assertListEqual(deck._cards, [1,2,3,4,5])

    def test_shuffled_deck_other_than_base_deck(self):
        deck = Deck([1,2,3,4,5])
        cards_before = deck._cards.copy()
        deck.shuffle_deck()
        self.assertNotEqual(deck._cards, cards_before)

    def test_draw_card(self):
        deck = Deck([1,2,3,4,5])
        card = deck.draw_card()
        self.assertEqual(card, 5)
        self.assertEqual(len(deck._cards), 4)

if __name__ == "__main__":
    unittest.main()
    
class NoMoreCardsError(Exception):
    '''Exception raised when there are no cards left on the deck'''