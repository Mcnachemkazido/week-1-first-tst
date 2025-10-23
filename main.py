import game_logic.game
from game_logic.game import init_game, play_round
game = init_game()



if __name__ == "__main__":
    flag = True
    while flag:
        init_game()
        play_round(game["player_1"],game["player_2"])
        if not game["player_1"] or not game["player_2"]:
            flag = False

    if len(game["player_1"]["won_pile"]) > len(game["player_2"]["won_pile"]):
        print("player_1 big")
    elif len(game["player_1"]["won_pile"]) > len(game["player_2"]["won_pile"]):
        print("player_2 big")
    else:
        print("no big")
