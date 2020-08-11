from deck import Deck
from card import Card, NormalCard, SpecialCard

class Player:
    """
    This class keeps track of the players' information. Such as his/her name, cards and her/his points
    """
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total_points = 0
    
    def increase_points(self, amount):
        
        """
        Increases the player's total points adding the parameter amount to the var self.total_points
        """
        self.total_points += amount
        print(f"Player {self.name} has {self.total_points} now.")
    
    def play(self):
        """
        Calls the helper method self.print_cards() to print all the cards, then it tries to take the user
        input and returns the card according to the index the user chose.
        """
        
        card_index = self.print_cards()
        
        try:
            user_choice = int(input("What's the card you wanna play?\n"))
            
            if user_choice < 0 or user_choice >= card_index:
                print("Please, enter a valid number")
                while user_choice < 0 or user_choice >= card_index:
                    card_index = self.print_cards()
                    user_choice = int(input("What's the card you wanna play?\n"))
                    
            return self.cards[user_choice]
        
        except ValueError:
            print("Please, digit a valid NUMBER.")
            
            return self.play()
    
    def get_cards_points(self):
        """
        Iterate trough the player's cards and return the total amount of points all the cards
        values together.
        """
        cards_total_points = 0
        if self.cards == []:
            return 0
        
        for card in self.cards:
            cards_total_points += card.get_card_points()
        
        return cards_total_points
    
    def draw_card_to_players_deck(self, current_deck):
        """
        Adds a card to the player's card calling the method from the Deck class draw_card()
        and prints the card the player got.
        """
        self.cards.append(current_deck.draw_card())
        print(f"The card you got is \n {self.cards[-1].name} -- {self.cards[-1].color}")
    
    def print_cards(self):
        """
        Helper method that prints all the player's card then return the card index resulted
        from printing all the cards
        """
        
        card_index = 0
        
        for card in self.cards:
            print(f"{card_index} --> {card.name} -- {card.color}")
            card_index += 1
            
        return card_index
    
    def remove_card_played(self, card_played):
        """
        Removes the card the player played and print Uno! if he/she is with just 2 cards.
        """
        card_index = self.cards.index(card_played)
        if len(self.cards) == 2:
            print(f"{self.name}: Uno!")
            
        del(self.cards[card_index])

import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.cards = []
        self.player = Player("Joao")
        self.deck = Deck(self.cards)
        self.special_card_1 = SpecialCard('Wild Draw Four')
        self.special_card_2 = SpecialCard('Draw Two', 'Yellow')
        self.special_card_3 = SpecialCard('Reverse', 'Green')
        self.normal_card_1 = NormalCard('Blue', 'One', 1)
        self.normal_card_2 = NormalCard('Yellow', 'Six', 6)
        self.normal_card_3 = NormalCard('Green', 'Zero', 0)
        self.test_cards = [
            self.special_card_1,
            self.special_card_2,
            self.special_card_3,
            self.normal_card_1,
            self.normal_card_2,
            self.normal_card_3
        ]
    
    def test_add_single_card(self):
        self.cards.append(NormalCard('Red', 'Test', 5))
        self.player.draw_card_to_players_deck(self.deck)
        self.assertEqual(self.player.cards[0].name, 'Test')
    
    def test_add_multiple_cards(self):
        self.cards += self.test_cards
        
        for i in range(6):
            self.player.draw_card_to_players_deck(self.deck)
        
        self.test_cards.reverse()
        self.assertEqual(self.player.cards, self.test_cards)
        
    def test_add_single_card_and_remove_it(self):
        self.cards.append(self.normal_card_1)
        self.player.draw_card_to_players_deck(self.deck)
        self.assertEqual(self.player.cards, [self.normal_card_1])
        
        self.player.remove_card_played(self.normal_card_1)
        self.assertEqual(self.player.cards, [])
    
    def test_add_multiple_cards_and_remove_one(self):
        self.cards += self.test_cards
        
        for i in range(6):
            self.player.draw_card_to_players_deck(self.deck)
            
        self.test_cards.reverse()
        self.assertEqual(self.player.cards, self.test_cards)
    
    def test_print_cards(self):
        self.assertEqual(self.player.print_cards(), 0)
        

if __name__ == '__main__':
    unittest.main()
        
        