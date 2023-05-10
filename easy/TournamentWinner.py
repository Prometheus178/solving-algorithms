# find winner 3 points who win 0 who lose

# time O(n^2)
# space O(M)  where M is count of command
def tournamentWinner(competitions, results):
    store = {}
    for i in range(len(competitions)):  # O(n)
        w = results[i]
        teams = competitions[i]
        winner = findWinner(teams, w)
        if store.__contains__(winner):
            val = store.get(winner)
            store.update({winner: val + 3})
        else:
            store[winner] = 3
    return max(store, key=store.get)  # O(n)


# time O(n)
# space O(M)  where M is count of command
def tournamentWinner2(competitions, results):
    bestWinnerName = "bestWinnerName"
    bestWinnerScore = "bestWinnerScore"
    store = {bestWinnerScore: 0}
    for i in range(len(competitions)):  # O(n)
        w = results[i]
        teams = competitions[i]
        winner = findWinner(teams, w)
        if store.__contains__(winner):
            val = store.get(winner)
            newVal = val + 3
            store.update({winner: newVal})
            valW = store.get(bestWinnerScore)
            if valW < newVal:
                store.update({bestWinnerName: winner})
                store.update({bestWinnerScore: newVal})
        else:
            store[winner] = 3
            valW = store.get(bestWinnerScore)
            if valW < 3:
                store.update({bestWinnerScore: 3})
                store.update({bestWinnerName: winner})
    return store.get(bestWinnerName)


def findWinner(teams, w):
    if w == 0:
        winner = teams[1]
    else:
        winner = teams[0]
    return winner


print(tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
], [0, 0, 1]))  # 1 mean win left , 0 mean win right
