def ingest(*args):
    with open(file="{}/{}".format(*args)) as f:
        contents = f.readlines()
    return [x.strip() for x in contents]


def fmt(item):
    print("="*80)
    print("{:=^80}".format("---  {}  ---".format(item)))
    print("="*80)
