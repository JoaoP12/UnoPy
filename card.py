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
        self._points = points
    
    def get_card_points(self):
        '''
        Returns the points of the card
        '''
        return self._points
    
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
        self._special_cards_names = {
            CardType.REVERSE: 20,
            CardType.SKIP: 20,
            CardType.DRAWTWO: 20,
            CardType.WILD: 50,
            CardType.WILDFOUR: 50
        }
    
    def get_card_points(self):
        '''
        It returns how many points does the card values according to its name.
        '''
        
        return self._special_cards_name[self.name]
    
class CardType(Enum):
    WILD = "Wild"
    WILDFOUR = "Wild draw four"
    DRAWTWO = "Draw two"
    SKIP = "Skip"
    REVERSE = "Reverse"
