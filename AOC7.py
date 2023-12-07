from common import fmt, ingest

fileloc = "C:/aoc2023"
###
# 7 hand groups
#6/ five of a kind 5
#5/ four of a kind 1, 4
#4/ full house (3+2) 2, 3
#3/ three of a kind 1, 1, 3
#2/ two pairs 1, 2, 2
#1/ one pair 1, 1, 1, 2
#0/ high card 1, 1, 1, 1, 1
lookup = [
    [0, 0, 0, 0, 0, 6],
    [0, 0, 0, 4, 5],
    [0, 0, 2, 3],
    [0, 0, 1],
    [0, 0]
]
cardVal = {"2": "02",
           "3": "03",
           "4": "04",
           "5": "05",
           "6": "06",
           "7": "07",
           "8": "08",
           "9": "09",
           "T": "10",
           "J": "11",
           "Q": "12",
           "K": "13",
           "A": "14"}

cardValJoker = cardVal.copy()
cardValJoker["J"] = "01"

#parse input line into (hand, bid)
def parseline(line):
    return line.strip().split(" ")


# id #occurances of unique vals in hand, decide from there
# for hand, return the index of its group
def handidx(hand, Joker:bool=False):
    d = dict(zip(set(hand), [0]*len(set(hand))))
    for x in hand:
        d[x] += 1
    if Joker:
        j = d.pop("J", 0)
        if j == 5:
            return 6
        v = sorted(d.values())
        return lookup[len(v) - 1][v[-1] + j]
    else:
        v = sorted(d.values())
        return lookup[len(v) - 1][v[-1]]


def groupHands(hands, Joker:bool=False):
    groups = [[]]*7
    for x in range(7):
        groups[x] = []
    for hand in hands:
        idx = handidx(hand[0], Joker)
        groups[idx].append(hand)
    return groups


def handsortval(hand, Joker:bool=False):
    s = ""
    for x in hand:
        if Joker:
            s += cardValJoker[x]
        else:
            s += cardVal[x]
    return int(s)

def sortHands(list, Joker:bool=False):
    list.sort(key=lambda x: handsortval(x[0], Joker))


def aoc7_1():
    lines = ingest(fileloc, "AOC7.txt")
    hands = [parseline(x) for x in lines]
    hands = groupHands(hands)
    [sortHands(x) for x in hands]
    rank = 1
    cnt = 0
    for handgroup in hands:
        if len(handgroup) != 0:
            for x in handgroup:
                cnt += int(x[1].strip())*rank
                rank += 1
    return cnt


# the presence of jokers changes the groups something is sorted into, and changed J from val 11 to 01, but that's it?
def aoc7_2():
    lines = ingest(fileloc, "AOC7.txt")
    hands = [parseline(x) for x in lines]
    hands = groupHands(hands, Joker=True)
    [sortHands(x, Joker=True) for x in hands]
    rank = 1
    cnt = 0
    for handgroup in hands:
        if len(handgroup) != 0:
            for x in handgroup:
                cnt += int(x[1].strip())*rank
                rank += 1
    return cnt


if __name__ == "__main__":
    fmt(aoc7_1())
    fmt(aoc7_2())