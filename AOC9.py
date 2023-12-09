from common import ingest, fmt

fileloc = "C:/aoc2023"


def isAllZero(list):
    return len(set(list)) == 1 and list[0] == 0


# take a line, break it into numbers, then step through and find the sequence for each layer
def processLine(line):
    n = [int(x.strip()) for x in line.split(" ")]
    seq = [n]
    while not isAllZero(n):
        n = [n[x]-n[x-1] for x in range(1, len(n))]
        seq.append(n)
    return seq


# for a sequence, calculate the next number (work up through the lists, n[-1]=n[-2] + m[-1])
def extrapolate(seq):
    for x in range(len(seq)-2, -1, -1):
        seq[x].append(seq[x][-1] + seq[x+1][-1])
    return seq


# for a sequence, calculate the previous numbers n[0]=n[1]-m[0]
def extrapolateBack(seq):
    for x in range(len(seq)-2, -1, -1):
        seq[x] = [seq[x][0]-seq[x+1][0]] + seq[x]
    return seq


def getNextVal(seq):
    return extrapolate(seq)[0][-1]


def getPrevVal(seq):
    return extrapolateBack(seq)[0][0]


def aoc9_1():
    records = ingest(fileloc, "AOC9.txt")
    n = 0
    for line in records:
        seq = processLine(line)
        n += getNextVal(seq)
    return n


def aoc9_2():
    records = ingest(fileloc, "AOC9.txt")
    n = 0
    for line in records:
        seq = processLine(line)
        n += getPrevVal(seq)
    return n

if __name__ == "__main__":
    fmt(aoc9_1())
    fmt(aoc9_2())
