def score(numberOfPlayers,players, game, wins, track = []):
    ## calculate the players' scores

    # initialize score array
    scores = []
    for i in range(numberOfPlayers):
        scores.append(1)

    minScore = 0  # clear minScore
    for i in range(numberOfPlayers):
        # calculate player i's score, find minimum score
        scores[i] = -players[i].tokens  # start by subtracting the tokens
        players[i].cards.sort()  # put the cards list in increasing order
        for j in range(len(players[i].cards)):
            # the lowest cards count, and all other cards count only if they are not one more
            # than the previous cards in the list
            if ((j == 0) or (players[i].cards[j - 1] != players[i].cards[j] - 1)):
                scores[i] = scores[i] + players[i].cards[j]
        if ((scores[i] < minScore) or (i == 0)):
            minScore = scores[i]
    numWithMinScore = 0
    for i in range(numberOfPlayers):
        # count number of players with minimum score
        if (scores[i] == minScore):
            numWithMinScore += 1
    # if a tie, each tying player gets an equal fraction of the win (i.e., if two tie, they each get 0.5, etc.)
    for i in range(numberOfPlayers):
        if (scores[i] == minScore):
            wins[i] += 1. / numWithMinScore

    # print out current estimated win probability for player zero every so often
    if ((game % 10000 == 0) and (game > 0)):
        # print (wins[0]*1./game)
        #     #track[game] = wins[0]*1./game
        track.append(wins[0] * 1. / game)
    #     #print game
    #     #for jj in range(numberOfPlayers):
    #     #	print jj," ",wins[jj]*1./game
    # if game == numberOfGames - 1: # the last game:
    #       print(track)
    return wins, track