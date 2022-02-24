import  random

class Player:

    def __init__(self, tokens, cards):
        self.tokens = tokens
        self.cards = cards

def init_game(numberOfPlayers):
    ### prepare the deck for a game

    # generate the deck
    deck = list(range(3, 36))
    # shuffle the cards
    random.shuffle(deck)
    # remove 9 cards
    deck = deck[:-9]

    ### initialize players array
    # Each player needs two things: an integer indicating how many
    # tokens they have, and a list of the cards they have

    players = []
    #     for i in range(numberOfPlayers):
    #         players.append(1)

    # initialize each player with 11 tokens and an empty list of cards

    for i in range(numberOfPlayers):
        players.append(Player(11, []))

    return  deck, players