from game import Game
from generate_cards import GenerateCards
from player import Player
deck = GenerateCards().get_cards()
game_session = Game(deck)

def menu():
    invalid = True
    print("Welcome to UnoPy!\n")
    number_of_players = input("How many players will play today?\n Min: 2 players - Max: 10 players\n")
    while invalid:
        if number_of_players.isdigit(): 
            if int(number_of_players) >= 2 and int(number_of_players) <= 10:
                invalid = False
                number_of_players = int(number_of_players)
            else:
                number_of_players = int(input("How many players will play today?\n Min: 2 players - Max: 10 players\n"))
        else:
            print("You entered a non-integer value!")
        
    ask_players_names(number_of_players)

def ask_players_names(number_of_players):
    print("Now type all the players names...")
    players_string = ""
    for player in range(0, number_of_players):
        current_player_name = input(f"\nPlayer {player} name --> ")
        players_string += current_player_name + "\n"
        game_session.insert_player(Player(current_player_name))
    print("Players:\n")
    print(players_string)
    
def distribute_cards(players):
    for player in players:
        for card_drown in range(7):
            game_session.draw_card_to_player(player)
    
def main():
    menu()
    print("Distributing cards...\n")
    distribute_cards(game_session.players)
    print("Done!\n")
    print("Game Starting...\n")
    game_session.start_game()

main()