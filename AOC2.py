from common import ingest, fmt
fileloc = "C:/aoc2023"

names = ["red", "green", "blue"]
limit_1 = dict(zip(names, [12, 13, 14]))


def parseInput(line):
    (idx, line) = line.split(":")
    idx = int(idx.split(" ")[1])
    dat = []
    for part in line.split(";"):
        tmp = {y: int(x) for (x, y) in [x.strip().split(" ") for x in part.split(",")]}
        dat.append(tmp)
    return idx, dat


def listProduct(x):
    c = 1
    for n in x:
        c *= n
    return c


def aoc2_1(limits:dict):
    records = ingest(fileloc, "AOC2.txt")
    dat = [parseInput(x) for x in records]              # dat now a list of tuples (int, dicts)
    cnt = 0
    for (idx, contents) in dat:
        for colour in limits.keys():
            if max([x[colour] for x in contents if colour in x.keys()]) > limits[colour]:
                break
        else:
           cnt += idx
    return cnt


def aoc2_2():
    records = ingest(fileloc, "AOC2.txt")
    dat = [parseInput(x) for x in records]  # dat now a list of tuples (int, dicts)
    cnt = 0
    for (idx, contents) in dat:
        cnt += listProduct([max([x[y] for x in contents if y in x.keys()]) for y in names])
    return cnt


fmt(aoc2_1(limit_1))

fmt(aoc2_2())
