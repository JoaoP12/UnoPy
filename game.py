from deck import Deck
from player import Player
from card import Card, NormalCard, SpecialCard, CardType

class Game:
    def __init__(self, gdeck):
        self.players = []
        self.number_of_players = len(self.players)
        self.gdeck = gdeck
        self.round = 0
        self.current_color_chosen_by_wild_card = None
    
    def start_game(self):
        while True:
            for player in self.players:
                if player.total_points >= 500:
                    print("Game Over!\n")
                    print(f"Player {player.name} won the game!\n")
                    self.show_scoreboard()
                    break
                    
                self.single_round()
    
    def single_round(self):
        """
        This method "plays" a single round of the game calling the necessary methods and classes
        and print messages so the players know what is happening.
        """
        skip_player = False
        number_of_cards_next_player_draws = None #  This variable stores how many cards does the 'next' player needs to draw
        cards_played = []
        pace = 1
        self.round += 1
        
        print("Starting round...")
        
        self.show_scoreboard()
        print("Drawing a card to be the first...\n")
        
        first_card = self.gdeck.draw_card()
        print("The first card is --> {first_card.name} -- {first_card.color}")
        cards_played.append(first_card)
        
        print(f"****** Round {self.round} ******\n")
        while True:
            for p in range(0, len(self.players), pace):
                player = self.players[p]
                if number_of_cards_next_player_draws is not None:
                    print(f"Player {player.name} needs to draw {number_of_cards_next_player_draws} cards due to the last card played!\n")
                    print(f"Drawing cards to {player.name}'s deck...\n")
                    
                    for time in range(0, number_of_cards_next_player_draws):
                        self.draw_card_to_player(player, cards_played)
                            
                    skip_player = True
                
                if skip_player:
                    print(f"{player.name} skipped!\n")
                    skip_player = False
                    continue
                
                print(f"{player.name}'s turn!")
                
                if self.has_valid_cards(player.cards, cards_played) == False:
                    print(f"It seems the player {player.name} doesn't have a playable card...\n")
                    print(f"Drawing a card to {player.name}'s deck...\n")
                    
                    self.draw_card_to_player(player, cards_played)
                    
                    if self.has_valid_cards(player.cards, cards_played) == False:
                        print(f"{player.name} still does not have a playable card!\n")
                        print(f"{player.name} skipped!\n")
                        continue
                    
                possible_card = player.play()
                    
                if self.valid_play(possible_card, cards_played):
                    print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")
                        
                    self.remove_card_from_player(player, possible_card)
                        
                    if self.player_won(player):
                        print(f"{player.name} won the round!\n")
                        print("Counting points...\n")
                        total_points_to_winner = self.count_points()
                        print(f"{player.name} got more {total_points_to_winner} points!\n")
                        player.increase_points(total_points_to_winner)
                        self.show_scoreboard()
                            
                    if type(possible_card) == SpecialCard:
                        
                        card_type = CardType(possible_card.name)
                            
                        if card_type == CardType.WILD:
                            self.current_color_chosen_by_wild_card = self.ask_color()
                            print(f"Now the color of the round is {self.current_color_chosen_by_wild_card}")
                                
                        elif card_type == CardType.WILDFOUR:
                            self.current_color_chosen_by_wild_card = self.ask_color()
                            number_of_cards_next_player_draws = 4
                            
                        elif card_type == CardType.DRAWTWO:
                            number_of_cards_next_player_draws = 2
                            
                        elif card_type == CardType.SKIP:
                            skip_player = True
                            
                        elif card_type == CardType.REVERSE:
                            pace = self.revert_game(pace)
                            
                        else:
                            print("Game: That's not a valid card! Try again!")
                            while self.valid_play(possible_card, cards_played) == False:
                                possible_card = player.play()
                            
                            print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")
                            
                        cards_played.append(possible_card)
    
    def count_points(self):
        """
        Iterate trough the players and call the method player.get_cards_points that returns the total points
        of all the cards from each player.
        """
        total_points = 0
        for player in self.players:
            total_points += player.get_cards_points()
        
        return total_points
    
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
        
    def player_won(self, player):
        '''
        Checks the cards of the player, if it is == 0, then the player won and True is returned, otherwise
        False is returned..
        '''
        if player.cards == []:
            return True
        return False
        
    
    def ask_color():
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
        
    def has_valid_cards(self, players_cards, cards_played):
        """
        Iterate trough the player's cards and return True if the player has at least one playable card.
        Otherwise return False.
        """
        for card in players_cards:
            if self.valid_play(card, cards_played):
                return True
        
        return False
        
    def revert_game(self, pace):
        """
        Takes the pace (that determines the order the players) and returns it times -1, that will literally
        revert the game.
        """
        return pace * -1
    
    def draw_card_to_player(self, player, cards_played=[]):
        '''
        Checks if there are any cards left on the deck to draw, if there aren't, it creates a new deck with
        the cards already played.
        '''
        try:
            player.draw_card_to_players_deck(self.gdeck)
                            
        except NoMoreCards:
            self.gdeck = self.gdeck.create_new_deck_with_played_cards(cards_played)
            player.draw_card_to_players_deck(self.gdeck)
    
    def remove_card_from_player(self, player, card_to_be_taken):
        '''
        Takes the card that was played and pops it from the player's card at the same time that returns it.
        '''
        
        player.remove_card_played(card_to_be_taken)
    
    def insert_player(self, name):
        '''
        Inserts a new player in the players variable.
        '''
        self.players.append(Player(name))