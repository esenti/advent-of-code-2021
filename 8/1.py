from pathlib import Path
from functools import reduce

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    outputs = []

    for line in lines:
        i, o = line.split('|')
        outputs.extend(x.strip() for x in o.split())

    print(sum(1 for o in outputs if len(o) in (2, 4, 3, 7)))
