import random

def create_card(rank:str,suite:str) -> dict:
    value = 0
    if rank in "2345678910":
        value = rank
    elif rank == "J":
        value = 11
    elif rank == "Q":
        value = 12
    elif rank == "K":
        value = 13
    elif rank == "A":
        value = 14

    return {"rank": rank, "suite": suite, "value":value}


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    big = 0
    if p1_card["value"] > p2_card["value"]:
        big = "p1"
    elif p1_card["value"] < p2_card["value"]:
        big = "p2"
    else:
        big = 'WAR'
    return big


def create_deck() -> list[dict]:
    list_catd = []
    rank =  ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suite = ['H','S','D','C']
    for i in rank:
        for j in suite:
            card = create_card(i,j)
            list_catd.append(card)
    return list_catd


def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        index1 =  random.randint(0,len(deck)-1)
        index2 =  random.randint(0,len(deck)-1)
        if index1 == index2:
            continue
        deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck

