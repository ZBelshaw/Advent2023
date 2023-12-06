from common import ingest,fmt
import math

fileloc = "C:/aoc2023"

# tuples time, distance record
races = [(52, 426), (94, 1374), (75, 1279), (94, 1216)]


def quadratic(a:int, b:int, c:int):
    sqrt = (b ** 2 - 4 * a * c) ** 0.5
    return int(math.ceil((b - sqrt)/2)), int((b + sqrt)//2)


def merge(list):
    a = ""
    for x in list:
        a += x
    return a


def aoc6_1(races):
    results = []
    for time, distance in races:
        short, long = quadratic(-1, time, -distance)
        results.append(1+long-short)
    return math.prod(results)


def aoc6_2():
    records = ingest(fileloc, "AOC6.txt")
    time = int(merge([x for x in records[0] if x.isdigit()]))
    distance = int(merge([x for x in records[1] if x.isdigit()]))
    short, long = quadratic(-1, time, -distance)
    return 1 + long - short


if __name__ == "__main__":
    fmt(aoc6_1(races))
    fmt(aoc6_2())
