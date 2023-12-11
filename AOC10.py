from common import ingest, fmt, coord

fileloc = "C:/aoc2023"

#       N    -y
# -x  W + E  +x
#       S    +y

##
# okay this one is going to suck I think
class pipe(coord):
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.type = val
        self.linked = []
        self.links()

    # get the coords of the directions we link to
    def links(self):
        for l in self.pipelookup[self.type]:
            x, y = self.translate(c = l)
            self.linked.append(coord(x, y))

    # take other and check if we are a link to it + it links to us
    def isValidConnection(self, other):
        return other in self.linked and self in other.linked

    # for the panel that is S, switch it to the actually valid pipe
    def switchS(self, others):
        if not "S" == self.type:
            return None
        a = []
        for c in set(self.linked).intersection(others):
            if self.isValidConnection(c):
                a.append(self.difference(c))
        if (1, 0) in a:
            if (-1, 0) in a:
                self.type = "-"
            elif (0, 1) in a:
                self.type = "F"
            elif (0,-1) in a:
                self.type = "L"
        elif (-1, 0) in a:
            if (0, 1) in a:
                self.type = "J"
            elif (0,-1) in a:
                self.type = "7"
        else:
            self.type = "|"


    # given an input thats in self.linked, get the other item in linked
    def getOutput(self, input):
        if input not in self.linked:
            return []
        return self.linked[[1, 0][self.linked.index(input)]]

    pipelookup = {"|": [(0 , -1), (0 , 1)],
              "-": [(-1, 0),  (1 , 0)],
              "L": [(0 , -1), (1 , 0)],
              "J": [(0 , -1), (-1, 0)],
              "7": [(0 ,  1), (-1, 0)],
              "F": [(0 ,  1), (1 , 0)],
              "S": [(0 ,  1), (0, -1), (1, 0),(-1, 0)]}      # S is where la creatura starts so technically can link in all 4 dirs


# sequence is -
# if next isn't there, break out, else get the next pipe out of the list (and drop it out of the list)
# if next doesn't connect, break out
# if it connects, get the next pipe in the sequence , append nextpipe to pipes (our loop) and find 'next'
def followloop(start:pipe, next:coord, allpipes):
    prev = start
    pipes = [start]
    while next != start:
        if next not in allpipes:
            break
        nextpipe = allpipes.pop(allpipes.index(next))
        if not prev.isValidConnection(nextpipe):
            break
        pipes.append(nextpipe)
        next = nextpipe.getOutput(prev)
        prev = nextpipe
    else:
        return pipes
    return []


def getPipes(records):
    pipes = []
    for y in range(len(records)):
        for x in range(len(records[y])):
            v = records[y][x]
            if v != ".":
                pipes.append(pipe(x, y, v))
    return pipes


def fillRow(rowpipes):
    rowpipes.sort(key=lambda x: x.x)
    s = [" "]*(rowpipes[-1].x + 1)
    fill = False
    primed = " "
    for a in rowpipes:
        s[a.x] = a.type
    for i in range(rowpipes[0].x, rowpipes[-1].x + 1):
        if (s[i] == " ") and fill:
            s[i] = "."
        elif s[i] == "|":
            fill = not fill
        elif s[i] == "F":
            primed = "J"
        elif s[i] == "L":
            primed = "7"
        elif s[i] == "J":
            if primed == "J":
                fill = not fill
            primed = " "
        elif s[i] == "7":
            if primed == "7":
                fill = not fill
            primed = " "
    return len([x for x in s if x == "."])


def aoc10_1():
    records = ingest(fileloc, "AOC10.txt")
    pipes = getPipes(records)
    creatura = pipes[[x.type for x in pipes].index("S")]
    x = creatura.linked.copy()
    loop = []
    while len(loop) == 0:
        loop = (followloop(creatura, x.pop(0), pipes.copy()))
    return len(loop)/2


def aoc10_2():
    records = ingest(fileloc, "AOC10.txt")
    pipes = getPipes(records)
    creatura = pipes[[x.type for x in pipes].index("S")]
    x = creatura.linked.copy()
    loop = []
    while len(loop) == 0:
        loop = (followloop(creatura, x.pop(0), pipes.copy()))
    loop[0].switchS(loop)
    loop_y = [x.y for x in loop]
    n = 0
    for y in range(min(loop_y), max(loop_y)+1):
        p = [x for x in loop if x.y == y]
        n += fillRow(p)
    return n




if __name__ == "__main__":
    fmt(aoc10_1())
    fmt(aoc10_2())