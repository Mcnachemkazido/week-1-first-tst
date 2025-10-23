from utils.deck import create_card ,compare_cards ,create_deck ,shuffle


def create_player(name:str= "AI") -> dict:
    player = {"name": name, "hand": [], "won_pile": []}
    return player


def init_game()->dict:
    p1 = create_player("menachem")
    p2 = create_player()
    deck = create_deck()
    shuffle_deck = shuffle(deck)
    p1["hand"] = shuffle_deck[:25]
    p2["hand"] = shuffle_deck[26:]
    return {"deck":shuffle_deck,"player_1":p1 ,"player_2":p2}



# x = init_game()

def play_round(p1: dict, p2: dict) :
    card_p1 = p1["hand"].pop()
    card_p2 = p2["hand"].pop()
    compare_card = compare_cards(card_p1,card_p2)
    if compare_card == "p1":
        p1["won_pile"].append(card_p1)
        p1["won_pile"].append(card_p2)
    elif compare_card == "p2":
        p2["won_pile"].append(card_p1)
        p2["won_pile"].append(card_p2)



# print(play_round(x["player_1"],x["player_2"]))