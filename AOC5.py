from common import ingest, fmt

fileloc = "C:/aoc2023"


# a mapping of source types to dest types, containing a bunch of range items
# ie - srctyp = seed
# desttyp = soil
# then need a method like map.addMapping(srcStart,destStart,length)
# then a map method, which takes an input number and maps it to destination
class AlmanacMap:
    def __init__(self, srctyp: str, desttyp: str):
        self.src = srctyp
        self.dest = desttyp
        self.ranges = []

    def addMappingRange(self, srcstart: int, deststart: int, length: int):
        self.ranges.append((srcstart, deststart, length))

    # sort the mapping range list by src
    def sortMap(self):
        self.ranges.sort()

    # map through available ranges, n if not in range
    def map(self, n) -> int:
        for srcStart, destStart, length in self.ranges:
            if srcStart <= n < (srcStart + length):
                n = destStart + n - srcStart
                break
        return n

    # split a range of integers into multiple lists around start/end of ranges, then translate them by the map of the given range
    def splitListByRanges(self, listBounds):
        self.sortMap()
        sublists = []
        for srcStart, destStart, length in self.ranges:
            srcEnd = srcStart + length - 1
            translation = destStart - srcStart
            pre, mod, post = self.listTranslate(listBounds, [srcStart, srcEnd], translation)
            if len(pre) == 2:
                sublists.append(pre)
            if len(mod) == 2:
                sublists.append(mod)
            if len(post) == 2:
                listBounds = post
            else:
                break
        return sublists

    # just a helper for the below idk this is so untidy now
    @staticmethod
    def __translateListItems(list, translate):
        return [x + translate for x in list]

    # modify the intersection of list and range by translate, returning 3 lists in a list, empty list of can be disregarded
    # i fucking hate this jesus christ
    @staticmethod
    def listTranslate(list, range, translate):
        if list[1] < range[0]:  # list ends before range starts
            return [list, [], []]
        elif list[0] > range[1]:  # list starts after range ends
            return [[], [], list]
        elif list[0] == range[0]:  # list and range start at same place
            if list[1] <= range[1]:  # and list ends within range
                return [[], AlmanacMap.__translateListItems(list, translate), []]
            elif list[1] > range[1]:  # and list ends after range
                return [[], AlmanacMap.__translateListItems(range, translate), [range[1] + 1, list[1]]]
        elif list[1] == range[1]:  # list and range end in same place
            if list[0] >= range[0]:  # list starts within range
                return [[], AlmanacMap.__translateListItems(list, translate), []]
            elif list[0] < range[0]:  # list starts before range
                return [[list[0], range[0] - 1], AlmanacMap.__translateListItems(range, translate), []]
        elif list[0] < range[0]:  # list starts before range
            if list[1] < range[1]:  # and ends before range
                return [[list[0], range[0] - 1], AlmanacMap.__translateListItems([range[0], list[1]], translate), []]
            elif list[1] > range[1]:  # and ends after range
                return [[list[0], range[0] - 1], AlmanacMap.__translateListItems(range, translate),
                        [range[1] + 1, list[1]]]
        elif list[0] > range[0]:  # list starts after range
            if list[1] < range[1]:  # and ends before range
                return [[], AlmanacMap.__translateListItems(list, translate), []]
            elif list[1] > range[1]:  # and ends after range
                return [[], AlmanacMap.__translateListItems([list[0], range[1]], translate), [range[1] + 1, list[1]]]


def parseInput(lines):
    maps = []
    current_map = None
    for line in lines:
        if 0 == len(line):
            continue
        elif "seeds" in line:
            seeds = [int(x.strip()) for x in line.partition(":")[2].strip().split(" ")]
        elif "map" in line:
            if current_map is not None:
                maps.append(current_map)
            x = line.partition(" ")[0].split("-")
            current_map = AlmanacMap(x[0], x[2])
        else:
            x = [int(x.strip()) for x in line.strip().split(" ")]
            current_map.addMappingRange(x[1], x[0], x[2])
    else:
        maps.append(current_map)
    return maps, seeds


# Take n through a bunch of map translations - maps may not be ordered
def translate(maps, n, start: str = "seed", end: str = "location"):
    srcs = [x.src for x in maps]
    while True:
        if (start not in srcs) or start == end:
            break
        m = maps[srcs.index(start)]
        n = m.map(n)
        start = m.dest
    return n


# using map m, for vector v produce and apply a translation map
def translateVector(maps, v, start: str = "seed", end: str = "location"):
    srcs = [x.src for x in maps]
    v = [v]
    while True:
        if (start not in srcs) or start == end:
            break
        m = maps[srcs.index(start)]
        lists = []
        for x in v:
            lists.extend(m.splitListByRanges(x))
        v = lists
        start = m.dest
    return lists


def aoc5_1():
    maps, seeds = parseInput(ingest(fileloc, "AOC5.txt"))
    locations = []
    for seed in seeds:
        locations.append(translate(maps, seed))
    return min(locations)


def aoc5_2():
    maps, seeds = parseInput(ingest(fileloc, "AOC5.txt"))
    locs = []
    for start, length in zip(seeds[::2], seeds[1::2]):
        for l in translateVector(maps, [start, start + length - 1]):
            locs.extend(l)
    return min(locs)


if __name__ == "__main__":
    fmt(aoc5_1())
    fmt(aoc5_2())
