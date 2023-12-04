from common import ingest, fmt
fileloc = "C:/aoc2023"


def parseLine(line:str):
    line = line.replace("  ", " ")
    win_num, player_num = line.partition(":")[2].split("|")
    win_num = set([int(x) for x in win_num.strip().split(" ")])
    player_num = set([int(x) for x in player_num.strip().split(" ")])
    return win_num, player_num


def aoc4_1():
    records = ingest(fileloc, "AOC4.txt")
    games = [parseLine(x) for x in records]
    cnt = 0
    for win_num, player_num in games:
        n = len(win_num.intersection(player_num))

        if n > 0:
            #print("{} -=> {}".format(n, pow(2, -1+n)))
            cnt += pow(2, -1 + n)
    return cnt


def aoc4_2():
    records = ingest(fileloc, "AOC4.txt")
    games = [parseLine(x) for x in records]
    num_games = len(games)
    n_match = [len(win_num.intersection(player_num)) for win_num, player_num in games]
    n_cards = [1]*num_games
    # for each element in n_match, for the next match entries, + n_cards[i]
    for i in range(num_games):
        if 0 == n_match[i]:
            continue
        upper = min([i + 1 + n_match[i], num_games])
        n_cards[i+1:upper] = [x + n_cards[i] for x in n_cards[i+1:upper]]
    return sum(n_cards)


if __name__ == "__main__":
    fmt(aoc4_1())
    fmt(aoc4_2())
