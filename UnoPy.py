from game import Game
from generate_cards import GenerateCards

def menu():
    print("Welcome to UnoPy!\n")
    try:
        number_of_players = 0
        while number_of_players < 2 and number_of_players > 10:
            number_of_players = int(input("How many players will play today?\n Min: 2 players - Max: 10 players\n"))
            
    except ValueError:
        while True:
            try:
                number_of_players = 0
                print("Please type a valid number!")
                while number_of_players < 2 and number_of_players > 10:
                    number_of_players = int(input("How many players will play today?\n Min: 2 players - Max: 10 players\n"))
                    
                break
            except ValueError:
                continue
    print("Now type all the players names...")
    players_names = []
    for player in range(0, number_of_players):
        current_player_name = input(f"\nPlayer {player} name --> ")
        players_names.append(current_player_name)
    '''
    Cadastrar os players com a class Player.
    Distribuir cartas.
    '''
    
    

def main():
    pass