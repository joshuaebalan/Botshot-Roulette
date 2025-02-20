def SolveOPT(live, blank, turn):
    if live == 0: #base case: no live bullets left, so nothing to do
        return 0
    if live == 1 and blank == 0 and turn: #base case: only one shell left and it's live: whoever has gun gets turn
        return 1 #player turn
    if live == 1 and blank == 0 and !turn:
        return -1 #opponent turn

    #otherwise, score recursively:

    total = live + blank
    liveChance = live / total
    blankChance = blank / total
    ShootOpponent = (liveChance * (1 + SolveOPT((live - 1)), blank, !turn)) + (blankChance * SolveOPT(live, (blank - 1), !turn))
    ShootSelf = (liveChance * (-1 + SolveOPT((live - 1), blank, !turn))) + (blankChance * SolveOPT(live, (blank -1), turn))
    opt = max(ShootSelf, ShootOpponent)
    if !turn:
        return -1 * opt
    else:
        return opt
