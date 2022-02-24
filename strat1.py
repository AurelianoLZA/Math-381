def strat1(currentCard, players,currentTokens, currentPlayer, cardIndex ):
        cardThresh = 12

        adjacency = (currentCard + 1 in players[currentPlayer].cards) or (
                    currentCard - 1 in players[currentPlayer].cards)
        # whether the card is smaller or thrshold or alreay on the table for 1 round
        largeOrSmall = currentTokens > 1 or currentCard < 19
        if ((adjacency and largeOrSmall) or (currentCard - currentTokens < cardThresh) or (
                players[currentPlayer].tokens == 0)):
            ## currentPlayer takes the card and the tokens, if any
            players[currentPlayer].tokens = players[currentPlayer].tokens + currentTokens
            players[currentPlayer].cards.append(currentCard)
            cardIndex = cardIndex + 1  ## get ready to turn over the next card
            currentTokens = 0
        else:  ## currentPlayer adds a token to the card
            currentTokens = currentTokens + 1
            players[currentPlayer].tokens = players[currentPlayer].tokens - 1
        return players[currentPlayer].tokens, players[currentPlayer].cards, cardIndex, currentTokens
