def strat0(currentCard, players,currentPlayer, currentTokens, cardIndex):
    cardThresh = 12

    if ((currentCard + 1 in players[currentPlayer].cards) or (currentCard - 1 in players[currentPlayer].cards) or
            (currentCard - currentTokens < cardThresh) or (players[currentPlayer].tokens == 0)):
        ## currentPlayer takes the card and the tokens, if any
        players[currentPlayer].tokens = players[currentPlayer].tokens + currentTokens
        players[currentPlayer].cards.append(currentCard)
        cardIndex = cardIndex + 1  ## get ready to turn over the next card
        currentTokens = 0
    else:  ## currentPlayer adds a token to the card
        currentTokens = currentTokens + 1
        players[currentPlayer].tokens = players[currentPlayer].tokens - 1
    return players[currentPlayer].tokens, players[currentPlayer].cards, cardIndex, currentTokens