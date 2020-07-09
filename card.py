class Card:
    '''
    The parent class of the cards. It keeps track of the cards' names and colors.
    '''
    
    def __init__(self, color, name):
        self.color = color
        self.card_name = name

class normalCard(Card):
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

class specialCard(Card):
    
    def __init__(self):
        pass
        