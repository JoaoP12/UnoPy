from card import SpecialCard, NormalCard
class GenerateCards:
    def __init__(self):
        self.colors = ['Blue', 'Yellow', 'Red', 'Green']
        self.names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.special_names = ['Skip', 'Reverse', 'Draw two', 'Wild draw four', 'Wild']

    def _generate_normal_cards(self):
        '''
        Generate the normal cards.
        '''
        normal_cards_info = []
        for color in self.colors:
            for number in range(0, 10):
                current_card = NormalCard(color, self.names[number], number)
                normal_cards_info.append(current_card)
                if number != 0:
                    normal_cards_info.append(current_card)
    
        return normal_cards_info

    def _generate_special_cards(self):
        '''
        It generates all the special cards and puts them into a list, than returns it.
        '''
        special_cards_info = []
        for color in self.colors:
            for name in self.special_names:
                if 'Wild' not in name:
                    for card in range(0, 2):
                        current_card = SpecialCard(name, color)
                        special_cards_info.append(current_card)
                        
                if color == self.colors[-1] and 'Wild' in name:
                    for card in range(0, 4):
                        current_card = SpecialCard(name)
                        special_cards_info.append(current_card)
                        
        return special_cards_info
    
    def get_cards(self):
        '''
        Calls the private methods that generate all the 108 cards and returns it.
        '''
        cards = self._generate_special_cards()
        cards += self._generate_normal_cards()
        return cards
