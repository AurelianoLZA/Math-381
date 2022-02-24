import itertools,random
import numpy as np
import matplotlib.pyplot as plt

import calc_score
import init_game
import strat0
import strat1
import strat3


class Player:

    def __init__(self, tokens, cards):
        self.tokens = tokens
        self.cards = cards

class GameState: # I don't actually use this class!!!

    def __init__(self, tokens, card): ## the current state of the game is the number of tokens on the
        self.tokens = tokens          ## current card, and which card is current
        self.card = card
def play(linear_rate = 3):  # default is 3
    res = []
    for i in range(2):
        numberOfPlayers = 4 ## the number of players
        numberOfGames = 100000;

        track = []
        wins=[] # array to keep track of how many times each player wins
        for i in range(numberOfPlayers):
            wins.append(0)

        for game in range(numberOfGames): ## main game loop

            #initialization
            deck, players = init_game.init_game(numberOfPlayers)

            #### start playing

            currentPlayer = game % numberOfPlayers ## start with a different player each time
            cardIndex = 0 # start at one end of the deck of cards
            currentTokens = 0 # initially there are no tokens on the current card
            known = set()
            while(cardIndex<24):
                currentCard = deck[cardIndex]
                known.add(currentCard)
                ## currentPlayer either adds a token, or takes the card
                if (currentPlayer in [0]):
                    players[currentPlayer].tokens, players[currentPlayer].cards, cardIndex, currentTokens = \
                        strat3.strat3(linear_rate,players,currentPlayer,currentCard,currentTokens,cardIndex)

                if (currentPlayer in [1,2,3]):
                    players[currentPlayer].tokens, players[currentPlayer].cards, cardIndex, currentTokens = strat0.strat0(
                        currentCard,players, currentPlayer, currentTokens,cardIndex
                    )

                # next players turn
                currentPlayer = (currentPlayer+1) % numberOfPlayers

            # calculate and update wins, and track if it is used
            wins, track = calc_score.score(numberOfPlayers,players,game, wins, track)

        ## output winning wins for all the players
        # for i in range(numberOfPlayers):
        #     print (i," ",wins[i]*1./numberOfGames)
        res.append(wins[0]*1.0/numberOfGames)
    # res_max = max(res)
    # res_min = min(res)
    return  res


    