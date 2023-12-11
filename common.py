def ingest(*args):
    with open(file="{}/{}".format(*args)) as f:
        contents = f.readlines()
    return [x.strip() for x in contents]


def fmt(item):
    print("="*80)
    print("{:=^80}".format("---  {}  ---".format(item)))
    print("="*80)

class coord:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def pos(self):
        return self.x, self.y

    def translate(self, x=0, y=0, c=(0, 0)):
        """return the coord that is x, y, c away from this position"""
        return self.x + x + c[0], self.y + y + c[1]

    def adjacent(self):
        all = [[coord(self.x + x, self.y + y) for y in [-1,0,1]] for x in [-1,0,1]]
        track = []
        for x in all:
            for y in x:
                if self != y:
                    track.append(y)
        return set(track)

    # return those cells which are cardinally adjacent to this one
    def cardinallyAdjacent(self):
        return set([[coord(self.x + x, self.y + y) for x in [-1, 1]] for y in [-1, 1]])

    def isAdjacent(self, other):
        return other in self.adjacent()

    # return the translation to take self -> other
    def difference(self, other):
        return other.x - self.x, other.y - self.y
