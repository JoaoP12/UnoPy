from card import Card
from card import SpecialCard
from card import NormalCard
from game import Game # Game is not implemented yet
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
        Prints all the cards the player has and then ask him which one will he/she play
        """
        cards = self.get_cards()
        card_index = 0
        for cd in cards:
            print(f"{card_index} --> {cd.name} -- {cd.color}\n")
            card_index += 1
        user_choice = imt(input("Type the number of the card you wanna play: "))
        
        if user_choice >= card_index or user_choice < 0:
            while user_choice >= card_index or user_choice < 0:
                user_choice = int(input("Please, type a valid number: "))
        
        if game.valid_play():
            self.cards
        
        
    def get_cards(self):
        return self.cards
        