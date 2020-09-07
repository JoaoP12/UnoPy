from deck import Deck
from card import Card, NormalCard, SpecialCard, CardType

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
        
    def ask_user_choice(self):
        '''
        Prints the user's cards and returns the answer of the user        
        '''
        self.print_cards()
        return int(input("What's the card you wanna play?\n"))
    
    def play(self):
        """
        Takes the user input, then checks it and returns it if valid, if not it will return None
        """
        
        user_choice = self.ask_user_choice()
        user_choice_checked = self.check_user_choice(user_choice)
        
        if user_choice_checked is None:
            print("Please, digit a valid NUMBER.")
            for i in range(3):
                user_choice = self.ask_user_choice()
                user_choice_checked = self.check_user_choice(user_choice)
                if user_choice_checked is not None:
                    return user_choice_checked
                
            return None
        
        return user_choice_checked
    
    def check_user_choice(self, user_choice):
        '''
        Checks if the user is entering a valid option, if so, returns the choice, otherwise return None
        '''
        try:
            if user_choice < 0 or user_choice >= len(self.cards):
                print("Please, enter a valid number")
                return None
                        
            return self.cards[user_choice]
        
        except (ValueError, IndexError):
            return None
        
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
    
    def draw_card_to_players_deck(self, card):
        """
        Adds a card to the player's cards
        """
        self.cards.append(card)
        if type(card) == NormalCard:
            print(f"The card you got is \n {card.name} [{card.color}]")
        elif card.name in [CardType.WILD, CardType.WILDFOUR]:
            print(f"The card you got is \n {card.name.value}")
        else:
            print(f"The card you got is \n {card.name.value} [{card.color}]")
            
            
    
    def print_cards(self):
        """
        Helper method that prints all the player's card then return the card index resulted
        from printing all the cards
        """
        
        card_index = 0
        
        for card in self.cards:
            if type(card) == NormalCard:
                print(f"{card_index} --> {card.name} [{card.color}]")
            elif card.name in [CardType.WILD, CardType.WILDFOUR]:
                print(f"{card_index} --> {card.name.value}")
            else:
                print(f"{card_index} --> {card.name.value} [{card.color}]")
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
from mock import MockInputFunction

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.cards = []
        self.player = Player("Joao")
        self.deck = Deck(self.cards)
        self.special_card_1 = SpecialCard(CardType.WILDFOUR)
        self.special_card_2 = SpecialCard(CardType.DRAWTWO, 'Yellow')
        self.special_card_3 = SpecialCard(CardType.REVERSE, 'Green')
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
        test_card = NormalCard('Red', 'Test', 5)
        self.cards.append(test_card)
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
        
        self.player.remove_card_played(self.special_card_2)
        self.assertNotIn(self.special_card_2, self.cards)
        
    def test_remove_card_from_empty_deck(self):
        with self.assertRaises(ValueError):
            self.player.remove_card_played(self.normal_card_2)
    
    def test_get_cards_points(self):
        self.cards += self.test_cards
        for i in range(6):
            self.player.draw_card_to_players_deck(self.deck)
            
        self.assertEqual(self.player.get_cards_points(), 97)
    
    def test_print_cards(self):
        self.assertEqual(self.player.print_cards(), 0)
    
    def test_increase_points(self):
        self.assertEqual(self.player.total_points, 0)
        
        self.player.increase_points(20)
        self.assertEqual(self.player.total_points, 20)
        

    def test_play_method_with_valid_entries(self):
        self.cards += self.test_cards
        
        for i in range(6):
            self.player.draw_card_to_players_deck(self.deck)
        
        self.test_cards.reverse()
        for i in range(6):
            with MockInputFunction(str(i)):
                self.assertEqual(self.player.play(), self.test_cards[i])
          
    def test_play_method_with_invalid_entries(self):
        self.cards += self.test_cards
        
        for card in self.cards:
            self.player.draw_card_to_players_deck(self.deck)
            
        with MockInputFunction('7'):
            self.assertEqual(self.player.play(), None)
        
        with MockInputFunction('159'):
            self.assertEqual(self.player.play(), None)
        
        with MockInputFunction(f'{10 ** 13}'):
            self.assertEqual(self.player.play(), None)

if __name__ == '__main__':
    unittest.main()
        
        