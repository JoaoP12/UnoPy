from deck import Deck
from player import Player
from card import Card, NormalCard, SpecialCard, CardType




'''
    deixado --> 19/07/20
    
    **** Implementar testes para deck.py
    
    **** Terminar single_round
        * Determinar se um player ganhou ou não
        
        * Determinar se é a última carta do jogador e printa UNO!
        
        * Implementar funções especiais Reverse, Skip e Draw.
    
'''

class Game:
    def __init__(self, players, gdeck):
        self.players = players
        self.number_of_players = len(self.players)
        self.gdeck = gdeck
        self.round = 0
        self.current_color_chosen_by_wild_card = None
    
    def start_game(self):
        pass
    
    def single_round(self):
        """
        This method "plays" a single round of the game calling the necessary methods and classes
        and print messages so the players know what is happening.
        """
        cards_played = []
        self.round += 1
        
        print("Starting round...")
        
        self.show_scoreboard()
        print("Drawing a card to be the first...\n")
        
        first_card = self.gdeck.draw_card()
        print("The first card is --> {first_card.name} -- {first_card.color}")
        cards_played.append(first_card)
        
        print(f"****** Round {self.round} ******\n")
        while self.player_won(self.players) == None:
            for player in self.players:
                
                print(f"{player.name}'s turn!")
                possible_card = player.play()
                
                if self.valid_play(possible_card, cards_played):
                    print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")
                    
                    if type(possible_card) == SpecialCard:
                        card_type = CardType(possible_card.name)
                        
                        if card_type == CardType.WILD:
                            self.current_color_chosen_by_wild_card = self.colors_menu()
                            print(f"Now the color of the round is {self.current_color_chosen_by_wild_card}")
                            
                            # Parei aqui
                            
                        elif card_type == CardType.WILDFOUR:
                            pass
                        
                        elif card_type == CardType.DRAWTWO:
                            pass
                        
                        elif card_type == CardType.SKIP:
                            pass
                        
                        else:
                            pass
                        
                    cards_played.append(possible_card)
                else:
                    print("Game: That's not a valid card! Try again!")
                    while self.valid_play(possible_card, cards_played) == False:
                        possible_card = player.play()
                        
                    print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")
                    cards_played.append(possible_card)
    
    def skip_player(self):
        pass
    
    def count_points(self):
        pass
    
    def challenge_uno(self):
        pass
    
    def valid_play(self, possible_card, cards_played):
        """
        Checks if the card the player is trying to play is a valid play. It does that by checking
        the last card played in the game and checks if both the card that wants to enter the game
        and the card already played are compatible between them.
        """
        
        last_card_played = cards_played[-1]
        
        if type(possible_card) == NormalCard and type(last_card_played) == NormalCard:
            if possible_card.color == last_card_played.color or possible_card.number == last_card_played.number:
                return True
            
            return False
        
        elif type(last_card_played) == SpecialCard and type(possible_card) == SpecialCard and last_card_played.name == possible_card.name:
            
            return True
        
        elif last_card_played.name == "Wild" or last_card_played.name == "Wild draw four":
            
            if possible_card.color == self.current_color_chosen_by_wild_card:
                return True
            
            return False
            
    def show_scoreboard(self):
        """
        Iterate through the players and show their names and total points
        """
        print("====== Scoreboard ======\n")
        for player in self.players:
            print(f"{player.name}: {player.get_total_score} pts\n")
        
    def player_won(self, players):
        pass
    
    def colors_menu():
        """
        Takes the input of the player that played a Wild card, in the input he/shee needs to
        choose the color they want to impose in the game.
        """
        
        colors_list = ['Blue', 'Green', 'Red', 'Yellow']
        print("Choose a color:\n")
        
        while True:
            try:
                color = int(input("1 - Blue\n2 - Green\n3 - Red\n4 - Yellow\n"))
                
            except ValueError:
                while True:
                    
                    try:
                        print("Please, type a valid option.\n")
                        color = int(input("1 - Blue\n2 - Green\n3 - Red\n4 - Yellow\n"))
                        break
                    
                    except ValueError:
                        continue
                    
            if color not in [number for number in range(1, 5)]:
                continue
            
            else:
                return colors_list[color-1]