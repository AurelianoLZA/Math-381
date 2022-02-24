if (currentPlayer in [0]):

    cardThresh = 35 - linear_rate * players[currentPlayer].tokens
    # cardThresh = 20 + np.exp(3-players[currentPlayer].tokens)
    # this next conditional statement is the strategy for this/these players:
    # pick up the card if (1) it is adjacent to a card the player already has, or
    # (2) currentCard-curretTokens<cardThresh, so the number of tokens offsets the points of the cards sufficiently, or
    # (3) the player has no tokens
    adjacency = (currentCard + 1 in players[currentPlayer].cards) or (currentCard - 1 in players[currentPlayer].cards)
    #             gap = (currentCard+1 in players[currentPlayer].cards) and (currentCard+1 not in known)
    if (adjacency or (currentCard - currentTokens < cardThresh) or (players[currentPlayer].tokens == 0)):
        ## currentPlayer takes the card and the tokens, if any
        players[currentPlayer].tokens = players[currentPlayer].tokens + currentTokens
        players[currentPlayer].cards.append(currentCard)
        cardIndex = cardIndex + 1  ## get ready to turn over the next card
        currentTokens = 0
    else:  ## currentPlayer adds a token to the card
        currentTokens = currentTokens + 1
        players[currentPlayer].tokens = players[currentPlayer].tokens - 1