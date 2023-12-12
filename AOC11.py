from common import ingest, fmt, coord
fileloc = "C:/aoc2023"

class vector:
    def __init__(self, n:int, star:bool, m:int=1):
        self.number = n
        self.star = star
        self.mult = m

    def setMult(self, m):
        self.mult = m

def getPairs(stars):
    pairs = []
    for i in range(len(stars)):
        for j in range(i+1 ,len(stars)):
            pairs.append([stars[i], stars[j]])
    return pairs


def calcDistance(pair, rows, columns):
    if pair[0].x < pair[1].x:
        c = range(pair[0].x, pair[1].x)
    else:
        c = range(pair[1].x, pair[0].x)
    if pair[0].y < pair[1].y:
        r = range(pair[0].y, pair[1].y)
    else:
        r = range(pair[1].y, pair[0].y)
    return sum([columns[x].mult for x in c]) + sum([rows[x].mult for x in r])


def aoc11(mult):
    records = ingest(fileloc, "AOC11.txt")
    grid = [[y for y in x] for x in records]
    rows = []
    columns = []
    stars = []
    for y in range(len(grid)):
        rows.append(vector(y, "#" in grid[y]))
    for x in range(len(grid[0])):
        columns.append(vector(x, "#" in [y[x] for y in grid]))
    [x.setMult(mult) for x in columns if not x.star]
    [x.setMult(mult) for x in rows if not x.star]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                stars.append(coord(x, y))
    pairs = getPairs(stars)
    n = 0
    for pair in pairs:
        n += calcDistance(pair, rows, columns)
    return n

if __name__ == "__main__":
    fmt(aoc11(2))
    fmt(aoc11(10 ** 6))