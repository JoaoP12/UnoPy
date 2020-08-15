from deck import Deck, NoMoreCards
from player import Player
from card import Card, NormalCard, SpecialCard, CardType

class Game:
    def __init__(self, gdeck):
        self.players = []
        self.number_of_players = len(self.players)
        self.gdeck = Deck(gdeck)
        self.gdeck.shuffle_deck()
        self.round = 0
        self.current_color_chosen_by_wild_card = None
        self.cards_played = []
        self.pace = 1
        self.skip_player = False
    
    def start_game(self):
        while True:
            if self.player_won_game():
                break
                    
            self.single_round()
    
    def single_round(self):
        """
        This method "plays" a single round of the game calling the necessary methods and classes
        and print messages so the players know what is happening.
        """
        self.round += 1
        
        print("Starting round...")
        
        self.show_scoreboard()
        print("Drawing a card to be the first...\n")
        
        first_card = self.gdeck.draw_card()
        print(f"The first card is --> {first_card.name} -- {first_card.color}")
        self.cards_played.append(first_card)
        
        print(f"****** Round {self.round} ******\n")
        while True:
            
            for player in range(0, len(self.players), self.pace):
                if not self.player_won_round():
                    current_player = self.players[player]
                    
                    if self.skip_player:
                        print(f"{player.name} skipped!\n")
                        self.skip_player = False
                        continue
                
                    print(f"{current_player.name}'s turn!")
                
                    if self.check_players_cards(current_player):
                    
                        possible_card = current_player.play()
                    
                        if type(possible_card) == NormalCard:
                            if self.valid_play(possible_card):
                                print(f"Player {current_player.name} played a {possible_card.color} {possible_card.name} card!")
                        
                            else:
                                while True:
                                    possible_card = current_player.play()
                                    if type(possible_card) == NormalCard and self.valid_play(possible_card):
                                        break
                                    elif type(possible_card) == SpecialCard:
                                        self.check_special_card(current_player, possible_card, player+1)
                                        break
                    
                        else:
                            self.check_special_card(current_player, possible_card, player+1)
                        
                        self.remove_card_from_player(current_player, possible_card)
                        self.cards_played.append(possible_card)
                
    
    def count_points(self):
        """
        Iterate trough the players and call the method player.get_cards_points that returns the total points
        of all the cards from each player.
        """
        total_points = 0
        for player in self.players:
            total_points += player.get_cards_points()
        
        return total_points
    
    def valid_play(self, possible_card):
        """
        Checks if the card the player is trying to play is a valid play. It does that by checking
        the last card played in the game and checks if both the card that wants to enter the game
        and the card already played are compatible between them.
        """
        
        last_card_played = self.cards_played[-1]
        
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
        
        if possible_card == None:
            return False
            
    def show_scoreboard(self):
        """
        Iterate through the players and show their names and total points
        """
        print("====== Scoreboard ======\n")
        for player in self.players:
            print(f"{player.name}: {player.total_points} pts\n")
        
    def player_won_round(self):
        '''
        Checks the cards of the player, if it is None, then the player won and True is returned, otherwise
        False is returned..
        '''
        for player in self.players:
            if player.cards is None:
                print(f"{player.name} won the round!\n")
                print("Counting points...\n")
                total_points = self.count_points()
                print(f"Total points --> {total_points}")
                player.increase_points(total_points)
                self.show_scoreboard()
                return True
        return False
    
    def player_won_game(self):
        '''
        Iterate trough the self.players list and check each player's points, if any player has reached
        500 points, it returns True, otherwise returns False
        '''
        for player in self.players:
            if player.total_points >= 500:
                print("Game Over!\n")
                print(f"Player {player.name} won the game!\n")
                self.show_scoreboard()
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
        
    def has_valid_cards(self, players_cards):
        """
        Iterate trough the player's cards and return True if the player has at least one playable card.
        Otherwise return False.
        """
        for card in players_cards:
            if self.valid_play(card):
                return True
        
        return False
        
    def revert_game(self, pace):
        """
        Takes the pace (that determines the order the players) and multiply it by -1, that will literally
        revert the game.
        """
        self.pace += -1
    
    def draw_card_to_player(self, player):
        '''
        Checks if there are any cards left on the deck to draw, if there aren't, it creates a new deck with
        the cards already played.
        '''
        try:
            player.draw_card_to_players_deck(self.gdeck)
                            
        except NoMoreCards:
            self.gdeck = self.gdeck.create_new_deck_with_played_cards(self.cards_played)
            self.cards_played = []
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
    
    def check_players_cards(self, player):
        '''
        Check if the player has valid cards and if not, draw a card to his/her deck. Return True or False accor
        ding to the results of the check.
        If player has valid cards --> return True
        If not --> draw card to player --> if player has valid cards --> return True (otherwise) return False
        '''
        if not self.has_valid_cards(player.cards):
            print(f"It seems the player {player.name} doesn't have a playable card...\n")
            print(f"Drawing card to {player.name}'s deck...\n")
                    
            self.draw_card_to_player(player)
                    
            if not self.has_valid_cards(player.cards):
                print(f"{player.name} still does not have a playable card!\n")
                print("{player.name} skipped!")
                return False
            return True
        
        return True
    
    def skip_player(self, player_to_be_skipped):
        '''
        Helper method that ste the variable self.skip_player to True, then when the method single_round checks
        if it is needed to skip the current player, it will be done.
        '''
        self.skip_player = True
    
    
    def check_special_card(self, player, possible_card, next_players_index):
        '''
        Checks if the card played is a Special Card and if so, execute what would be its effects in the game,
        like reverting, changing de color etc.
        '''
        if type(possible_card) == SpecialCard:
                        
            card_type = CardType(possible_card.name)
                            
            if card_type == CardType.WILD:
                self.current_color_chosen_by_wild_card = self.ask_color()
                print(f"Now the color of the round is {self.current_color_chosen_by_wild_card}")
                                
            elif card_type == CardType.WILDFOUR:
                self.current_color_chosen_by_wild_card = self.ask_color()
            
                for time in range(4):
                    self.draw_card_to_player(self.players[next_players_index])
                self.skip_player(next_players_index)
                            
            elif card_type == CardType.DRAWTWO:
                for time in range(2):
                    self.draw_card_to_player(self.players[next_players_index])
                self.skip_player(next_players_index)
                
                            
            elif card_type == CardType.SKIP:
                self.skip_player(next_players_index)
                            
            elif card_type == CardType.REVERSE:
                self.revert_game()
                            
            else:
                print("Game: That's not a valid card! Try again!")
                while not self.valid_play(possible_card):
                    possible_card = player.play()
                            
                print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")

import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        pass
    