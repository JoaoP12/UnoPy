class Card:
    '''
    The parent class of the cards. It keeps track of the cards' names and colors.
    '''
    
    def __init__(self, color, name):
        self.color = color
        self.card_name = name

class NormalCard(Card):
    '''
    This class inherits from Card class and it is responsible for keeping track of the
    normal cards, that doesn't have a special function, just a color and number
    '''
    
    def __init__(self, color, name, points):
        super().__init__(color, name)
        self.card_points = points
    
    def get_card_points(self):
        '''
        Returns the amount of points the card values. That is stored in the self.
        card_points instance variable. The normal cards have their points based on
        their number, being number == points.
        '''
        return self.card_points

class SpecialCard(Card):
    '''
    Stores the special cards of the game, those ones that have a special function
    such as reverse, draw 2 cards and, draw 4 cards etc.
    The constructor takes the card's name and color as the normalCard class, but 
    instead of a number, it takes the card's special function that will generate
    a different effect in the game.
    '''
    
    def __init__(self, color, name, function):
        super().__init__(color, name)
        self.effect_in_game = function
    
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
            if name == self.card_name:
                return special_cards_name[name]