
fileloc = "C:/Users/zbels/Documents2/"

mapping = {"one":"o1e",
            "two":"t2o",
            "three":"th3ee",
            "four":"fo4r",
            "five":"fi5ve",
            "six":"si6x",
            "seven":"se7en",
            "eight":"ei8ht",
            "nine":"ni9ne"
            }


def ingest(*args):
    with open(file="{}/{}".format(*args)) as f:
        contents = f.readlines()
    return [x.strip() for x in contents]


def substitute(map:dict, string:str):
    for (x, y) in map.items():
        string = string.replace(x, y)
    return string


def aoc1_1():
    records = ingest(fileloc, "AOC1-1.txt")
    cnt = 0
    for onerow in records:
        r = [x for x in onerow if x.isnumeric()]
        cnt += int(r[0] + r[-1])
    return cnt


def aoc1_2():
    records = ingest(fileloc, "AOC1-1.txt")
    records = [substitute(mapping, x) for x in records]
    cnt = 0
    for onerow in records:
        r = [x for x in onerow if x.isnumeric()]
        s = int(r[0] + r[-1])
        cnt += s
    return cnt


if __name__ == "__main__":
    print(aoc1_1())
    print(aoc1_2())
