from enum import Enum

class Card:
    '''
    The parent class of the cards. It keeps track of the cards' names and colors.
    '''
    
    def __init__(self, name, color=None):
        self.color = color
        self.name = name

class NormalCard(Card):
    '''
    This class inherits from Card class and it is responsible for keeping track of the
    normal cards, that doesn't have a special function, just a color and number
    '''
    
    def __init__(self, color, name, points):
        super().__init__(name, color)
        self.points = points
    
    def get_card_points(self):
        '''
        Helper method that returns the points of the card. It was implemented to avoid the player method
        get_card_points to be verbose.
        '''
        return self.points
        
class SpecialCard(Card):
    '''
    Stores the special cards of the game, those ones that have a special function
    such as reverse, draw 2 cards and, draw 4 cards etc.
    The constructor takes the card's name and color as the normalCard class, but 
    instead of a number, it takes the card's special function that will generate
    a different effect in the game.
    '''
    
    def __init__(self, name, color=None):
        super().__init__(name, color)
    
    def get_special_cards_name(self):
        '''
        Returns a dictionary with the names of all the special cards' names and
        the points according to each one.
        '''
        names = {
            'Reverse': 20,
            'Skip': 20,
            'Draw two': 20,
            'Wild': 50,
            'Wild draw four': 50
        }
        return names
    
    def get_card_points(self):
        '''
        Filters the name of the card according to the self.name instance variable.
        After comparing it with the names of the special cards got from the self.get
        _special_cards_name method.
        Then it returns how many points does the card values according to its name.
        '''
        special_cards_name = self.get_special_cards_name()
        
        for name in special_cards_name.keys():
            if name == self.name:
                return special_cards_name[name]
    
class CardType(Enum):
    WILD = "Wild"
    WILDFOUR = "Wild draw four"
    DRAWTWO = "Draw two"
    SKIP = "Skip"
    REVERSE = "Reverse"
