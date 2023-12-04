from common import ingest, fmt, coord
fileloc = "C:/aoc2023"

# as a number can be over multiple locations
# return a tuple ([symbol indices], [number indices, the number])
def scanString(string:str, symChar:str=" "):
    symbols = []
    numbers = []
    for i in range(len(string)):
        if string[i] == ".":
            continue
        elif string[i].isdigit():
            numbers.append((i, string[i]))
        else:
            if symChar == " " or symChar == string[i]:
                symbols.append(i)
    else:
        numbers = mergeNumbers(numbers)
    return symbols, numbers


# take the list of tuples [(index, number) ...] and merge together continuous items
def mergeNumbers(x:list):
    merged = []
    npos, n = x[0]
    npos = [npos]
    for (idx, number) in x[1:]:
        if idx == npos[-1] + 1:
            npos.append(idx)
            n += number
        else:
            merged.append((npos, int(n)))
            npos = [idx]
            n = number
    else:               # end of the line, append whatever's in the tracker
        merged.append((npos, int(n)))
    return merged


def aoc3_1():
    records = ingest(fileloc, "AOC3.txt")
    symbol_locations = []
    number_locations = []
    for i in range(len(records)):
        symbols, numbers = scanString(records[i])
        symbol_locations.extend([coord(x, i) for x in symbols])
        number_locations.extend([(set([coord(x, i) for x in loc]), n) for loc, n in numbers])           # expand the locations here to be a set of coords

    symbol_adjacent = []
    for x in symbol_locations:
        symbol_adjacent.extend(x.adjacent())
    symbol_adjacent = set(symbol_adjacent)
    cnt = 0
    for locs, n in number_locations:
        if locs.intersection(symbol_adjacent):
            cnt += n
    return cnt


def aoc3_2():
    records = ingest(fileloc, "AOC3.txt")
    symbol_locations = []
    number_locations = []
    for i in range(len(records)):
        symbols, numbers = scanString(records[i], symChar="*")
        symbol_locations.extend([coord(x, i) for x in symbols])
        number_locations.extend([(set([coord(x, i) for x in loc]), n) for loc, n in numbers])  # expand the locations here to be a set of coords
    cnt = 0
    for x in symbol_locations:
        adj_n = [n for y, n in number_locations if x.adjacent().intersection(y)]
        if 2 == len(adj_n):
            cnt += adj_n[0] * adj_n[1]
    return cnt


if __name__ == "__main__":
    fmt(aoc3_1())
    fmt(aoc3_2())
