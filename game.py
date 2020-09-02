from deck import _Deck, NoMoreCardsError
from player import Player
from card import Card, NormalCard, SpecialCard, CardType

class Game:
    def __init__(self, cards):
        self.players = []
        self.number_of_players = len(self.players)
        self.deck = _Deck(cards)
        self.deck.shuffle_deck()
        self.round = 0
        self.current_round_color = None
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
        
        first_card = self.draw_first_card()
        print(f"The first card is --> {first_card.name} -- {first_card.color}")
        self.cards_played.append(first_card)
        self.current_round_color = first_card.color
        
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
                
    def draw_first_card(self):
        """
        Iterate trough the deck and return the first NormalCard to start the game
        """
        for card in self.deck.cards:
            if type(card) == NormalCard:
                return self.deck.cards.pop(self.deck.cards.index(card))
    
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
            if possible_card.color == self.current_round_color or possible_card.points == last_card_played.points:
                return True
            
        elif type(last_card_played) == SpecialCard and type(possible_card) == SpecialCard:
            if last_card_played.name == possible_card.name:
                return True
            
        elif possible_card.name in [CardType.WILD, CardType.WILDFOUR]:
            return True
            
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
    
    def ask_color(self):
        """
        Takes the input of the player that played a Wild card, in the input he/shee needs to
        choose the color they want to impose in the game.
        """
        
        colors_list = ['Blue', 'Green', 'Red', 'Yellow']
        print("Choose a color:\n")
        
        for i in range(3):
            try:
                color = int(input("1. Blue\n2. Green\n3. Red\n4. Yellow\n"))
                
            except ValueError:
                while True:
                    
                    try:
                        print("Please, type a valid option.\n")
                        color = int(input("1. Blue\n2. Green\n3. Red\n4. Yellow\n"))
                        break
                    
                    except ValueError:
                        continue
                    
            if color not in [number for number in range(1, 5)]:
                continue
            
            else:
                self.current_round_color = colors_list[color-1]
                break
        else:
            print("You lost your turn because of many invalid entries")
            self.skip_player_turn()
        
    def has_valid_cards(self, players_cards):
        """
        Iterate trough the player's cards and return True if the player has at least one playable card.
        Otherwise return False.
        """
        for card in players_cards:
            if self.valid_play(card):
                return True
        
        return False
        
    def revert_game(self):
        """
        Takes the pace (that determines the order the players) and multiply it by -1, that will literally
        revert the game.
        """
        self.pace *= -1
    
    def draw_card_to_player(self, player):
        '''
        Checks if there are any cards left on the deck to draw, if there aren't, it creates a new deck with
        the cards already played.
        '''
        try:
            card_to_draw = self.deck.draw_card()
            player.draw_card_to_players_deck(card_to_draw)
                            
        except NoMoreCardsError:
            if len(self.cards_played) == 1:
                self.skip_player = True
                
            self.deck = self.deck.create_new_deck_with_played_cards(self.cards_played)
            self.cards_played = []
            card_to_draw = self.deck.draw_card()
            player.draw_card_to_players_deck(card_to_draw)
    
    def remove_card_from_player(self, player, card_to_be_taken):
        '''
        Takes the card that was played and pops it from the player's card at the same time that returns it.
        '''
        
        player.remove_card_played(card_to_be_taken)
    
    def insert_player(self, player):
        '''
        Inserts a new player in the players variable.
        '''
        self.players.append(player)
    
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
            if self.skip_player:
                return False
                    
            if not self.has_valid_cards(player.cards):
                print(f"{player.name} still does not have a playable card!\n")
                print("{player.name} skipped!")
                return False
        
        return True
    
    def skip_player_turn(self):
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
                self.ask_color()
                print(f"Now the color of the round is {self.current_round_color}")
                                
            elif card_type == CardType.WILDFOUR:
                self.ask_color()
            
                for time in range(4):
                    try:
                        self.draw_card_to_player(self.players[next_players_index])
                    except IndexError:
                        next_player_index = 0
                        self.draw_card_to_player(self.players[next_player_index])
                        
                self.skip_player_turn()
                            
            elif card_type == CardType.DRAWTWO:
                for time in range(2):
                    try:
                        self.draw_card_to_player(self.players[next_players_index])
                    except IndexError:
                        next_player_index = 0
                        self.draw_card_to_player(self.players[next_player_index])
                self.skip_player_turn()
                            
            elif card_type == CardType.SKIP:
                self.skip_player_turn()
                            
            elif card_type == CardType.REVERSE:
                self.revert_game()
                            
            else:
                print("Game: That's not a valid card! Try again!")
                while not self.valid_play(possible_card):
                    possible_card = player.play()
                            
                print(f"Player {player.name} played a {possible_card.color} {possible_card.name} card!")

import unittest
from generate_cards import GenerateCards
from mock import MockInputFunction

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("John")
        self.player_2 = Player("Jaroslaw")
        self.cards = GenerateCards().get_cards()
        self.game_example = Game(self.cards)
        self.special_card_1 = SpecialCard(CardType.WILDFOUR)
        self.special_card_2 = SpecialCard(CardType.DRAWTWO, 'Yellow')
        self.special_card_3 = SpecialCard(CardType.REVERSE, 'Green')
        self.normal_card_1 = NormalCard('Blue', 'One', 1)
        self.normal_card_2 = NormalCard('Yellow', 'Six', 6)
        self.normal_card_3 = NormalCard('Green', 'Zero', 0)
        self.test_cards = [
            self.special_card_1,
            self.special_card_2,
            self.special_card_3,
            self.normal_card_1,
            self.normal_card_2,
            self.normal_card_3
        ]
        
    
    def test_insert_player(self):
        self.game_example.insert_player(self.player_1)
        self.assertIn(self.player_1, self.game_example.players)
    
    def test_valid_play(self):
        self.game_example.cards_played += self.test_cards[:4]
        self.assertFalse(self.game_example.valid_play(self.normal_card_3))
        self.game_example.cards_played = self.test_cards[1:]
        self.assertTrue(self.game_example.valid_play(self.special_card_1))
    
    def test_ask_color_with_valid_entries(self):
        with MockInputFunction('4'):
            self.game_example.ask_color()
            self.assertEqual(self.game_example.current_round_color, 'Yellow')
        with MockInputFunction('1'):
            self.game_example.ask_color()
            self.assertEqual(self.game_example.current_round_color, 'Blue')
    
    def test_ask_color_with_invalid_entries(self):
        with MockInputFunction('5'):
            self.game_example.ask_color()
            self.assertIsNone(self.game_example.current_round_color)
            self.assertTrue(self.game_example.skip_player)
        with MockInputFunction('0'):
            self.game_example.ask_color()
            self.assertIsNone(self.game_example.current_round_color)
            self.assertTrue(self.game_example.skip_player)
    
    def insert_players_on_the_game(self):
        self.game_example.insert_player(self.player_1)
        self.game_example.insert_player(self.player_2)
        
    def test_check_special_card_wild_and_wild_draw_four_cards(self):
        self.insert_players_on_the_game()
        with MockInputFunction('1'):
            # Wild
            self.game_example.check_special_card(self.player_1, SpecialCard("Wild"), 1)
            self.assertEqual(self.game_example.current_round_color, 'Blue')
            # Wild +4
            self.game_example.check_special_card(self.player_2, self.special_card_1, 2) 
            '''The next player index = '2' above was put ON PURPOSE to test if the method is recognizing
            that the player on Index 2 does not exist and assign cards to the player at Index 0, in this case
            the player_1
            '''
            self.assertEqual(self.game_example.current_round_color, 'Blue')
            self.assertEqual(len(self.player_1.cards), 4)
    
    def test_check_special_card_draw_two_card(self):
        self.insert_players_on_the_game()
        self.game_example.check_special_card(self.player_1, self.special_card_2, 1)
        self.assertEqual(len(self.player_2.cards), 2)
        
        self.game_example.check_special_card(self.player_2, self.special_card_2, 2)
        self.assertEqual(len(self.player_1.cards), 2)
    
    def test_check_special_card_reverse_card(self):
        self.insert_players_on_the_game()
        self.game_example.check_special_card(self.player_1, self.special_card_3, 1)
        self.assertEqual(self.game_example.pace, -1)
        self.game_example.check_special_card(self.player_2, self.special_card_3, 0)
        self.assertEqual(self.game_example.pace, 1)
    
    def test_check_special_card_skip_card(self):
        self.insert_players_on_the_game()
        self.game_example.check_special_card(self.player_1, SpecialCard('Skip'), 1)
        self.assertTrue(self.game_example.skip_player)
    
    def test_check_players_cards(self):
        self.game_example.deck = _Deck([self.special_card_1])
        self.game_example.cards_played.append(self.normal_card_1)
        self.game_example.draw_card_to_player(self.player_1)
        self.assertTrue(self.game_example.check_players_cards(self.player_1))
        
        self.game_example.cards_played = []
        
        self.game_example.deck = _Deck([self.normal_card_2])
        self.game_example.cards_played.append(self.normal_card_1)
        
        self.game_example.draw_card_to_player(self.player_2)
        self.assertFalse(self.game_example.check_players_cards(self.player_2))
        
        '''
        There's a tricky thing here.
        When we call check_players_cards, it checks if the player has valid cards, if not, then it draws a 
        card to him/her. HOWEVER, after it checks again if the player has valid cards
        '''
        
if __name__ == "__main__":
    unittest.main()
    