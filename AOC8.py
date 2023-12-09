from common import fmt, ingest

fileloc = "C:/aoc2023"


def parseinput(lines):
    d = {}
    sequence = lines[0]
    for line in lines:
        if "=" in line:
            k, v = line.split("=")
            d[k.strip()] = [x.strip() for x in v.strip("() ").split(",")]
    return sequence, d


# proceed through maps from start to finish, following sequence and counting steps along the way
# loop seq if we reach end of it before finish
def journey(jumps:dict, sequence:str, start:str="AAA", finish:str="ZZZ"):
    sequence = [{"L":0, "R":1}[x] for x in sequence]            # this feels bad? works though so eh
    n = 0
    while True:
        for x in sequence:
            if start == finish:
                break
            start = jumps[start][x]
            n += 1
        if start == finish:
            break
    return n


# after getting to a 'z' the first time, its a fixed loop size
def journeySingle(jumps:dict, sequence:str, start:str="A", finishChar:str="Z"):
    sequence = [{"L":0, "R":1}[x] for x in sequence]            # this feels bad? works though so eh
    n = 0
    l = []
    tracker = 0
    while True:
        for x in sequence:
            if start[-1] == finishChar:
                tracker += 1
                l.append(n)
            if tracker == 2:
                break
            start = jumps[start][x]
            n += 1
        if tracker == 2:
            break
    return l


def aoc8_1():
    sequence, jumps = parseinput(ingest(fileloc, "AOC8.txt"))
    return journey(jumps, sequence)


def aoc8_2():
    sequence, jumps = parseinput(ingest(fileloc, "AOC8.txt"))
    starts = [x for x in jumps.keys() if x[-1] == "A"]
    j = [journeySingle(jumps, sequence, start=x) for x in starts]
    j = sorted(j, key=lambda x: x[1], reverse=True)
    return iterate(j[0][0], j[0][1], j[1:])


def iterate(start:int, step:int, others:list):
    while True:
        start += step
        for x, y in others:
            if 0 != (start - x) % y:
                break
        else:
            break
    return start


if __name__ == "__main__":
    fmt(aoc8_1())
    fmt(aoc8_2())
