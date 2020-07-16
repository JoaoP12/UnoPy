from deck import Deck as deck
from game import Game as game # Game is not implemented yet
import card


class Player:
    """
    This class keeps track of the players' information. Such as his/her name, cards and her/his points
    """
    
    def __init__(self, name, cards):
        self.name = name
        self.cards = []
        self.total_points = 0
    
    def increase_points(self, amount):
        
        """
        Increases the player's total points adding the parameter amount to the var self.total_points
        """
        self.total_points += amount
        print(f"Player {self.name} has {self.total_points} now.")
    
    def get_name(self):
        
        """
        Returns the player's name
        """
        
        return self.name
    
    def play(self):
        """
        First, filters all the cards that are playable and put them into a list.
        If the list does not have any cards inside it, the player draws a card from the deck
        and the method checks if the card drawn is playable, if so, the player has the option to
        play it, otherwise it calls the self.skip() method.
        """
        cards = self.get_cards()
        card_index = 0
        valid_cards = [possible_valid_card for possible_valid_card in cards if game.valid_card(possible_valid_card)]
        
        if valid_cards is not None:
            for possible_card in valid_cards:
                print(f"{card_index} --> {possible_card.name} -- {possible_card.color}\n")
                card_index += 0
            user_choice = int(input("Type the number of the card you wanna play: "))
            if user_choice >= card_index or user_choice < 0:
               while user_choice >= card_index or user_choice < 0:
                   user_choice = int(input("Please, type a valid number: "))
            
            card_to_be_played_index = cards.index(valid_cards[user_choice])
            card_to_be_played = self.cards.pop(card_to_be_played_index)
            return card_to_be_played
            
        else:
            print("You don't have any playable cards. Drawing one card from deck...")
            card_drawn = deck.draw_card()
            print(f"You've drawn the card below:\n")
            print(f"{card_drawn.name} -- {card_drawn.color}")
            if game.valid_play(card_drawn):
                user_choice = input("This card is playable. Do you want to play it? (y/n)")
                if user_choice != "y" and user_choice != "n":
                    while user_choice != "y" and user_choice != "n":
                        print("Please, enter a valid option.")
                        user_choice = input("Do you want to play the drawn card? (y/n)")
                if user_choice == "y":
                    
                    return card_drawn
                
                else:
                    
                    return self.skip_play()
                
            return self.skip_play()
        
    def skip_play(self):
        
        """
        Helper method that returns None. That means the player didn't play.
        """
        return None
    
    def get_cards(self):
        """
        Returns the cards of the player.
        """
        return self.cards
    
    
    def get_total_score(self):
        """
        Returns the amount of points the player has. That is done by returning the instance
        variable self.total_points
        """
        return self.total_points
    
    def get_cards_points(self):
        """
        Iterate trough the player's cards and return the total amount of points all the cards
        values together.
        """
        cards = self.get_cards()
        cards_total_points = 0
        for cd in cards:
            cards_total_points += cd.get_card_points()
        
        return cards_total_points
