from card import Card
from card import NormalCard
from card import SpecialCard
from random import shuffle


class _Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def draw_card(self):
        """
        Returns the top card of the deck to the player's cards.
        
        If the deck has no more cards, it raises the exception NoMoreCards.
        """
        if self.is_empty():
            raise NoMoreCardsError
            
        else:
            return self.cards.pop(-1)
        
    def shuffle_deck(self):
        """
        Takes the self.cards list and shuffle using shuffle function.
        """
        shuffle(self.cards)
            
        
    def is_empty(self):
        """
        Returns True if the deck is empty, otherwise returns False
        """
        if self.cards == []:
            return True
        
        return False
    
    def create_new_deck_with_played_cards(self, played_cards):
        """
        It takes the played cards and create a new deck, then it returns
        an instance of itself with the new deck
        """
        print("Creating new deck with the cards played...\n")
        self.cards = played_cards
        self.shuffle_deck()
        return _Deck(self.cards)

import unittest

class TestDeck(unittest.TestCase):
    def test_empty_deck(self):
        deck = _Deck([])
        self.assertListEqual(deck.cards, [])

    def test_deck_with_cards(self):
        deck = _Deck([1,2,3,4,5])
        self.assertListEqual(deck.cards, [1,2,3,4,5])

    def test_shuffled_deck_other_than_base_deck(self):
        deck = _Deck([1,2,3,4,5])
        cards_before = deck.cards.copy()
        deck.shuffle_deck()
        self.assertNotEqual(deck.cards, cards_before)

    def test_draw_card(self):
        deck = _Deck([1,2,3,4,5])
        card = deck.draw_card()
        self.assertEqual(card, 5)
        self.assertEqual(len(deck.cards), 4)

if __name__ == "__main__":
    unittest.main()
    
class NoMoreCardsError(Exception):
    pass