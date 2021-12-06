from pathlib import Path
from collections import defaultdict
from math import copysign

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    points = defaultdict(int)

    for line in lines:
        a, b = line.split(' -> ')
        ax, ay = a.split(',')
        bx, by = b.split(',')

        ax, ay = int(ax), int(ay)
        bx, by = int(bx), int(by)

        if ax == bx:
            d = int(copysign(1, by - ay))
            for y in range(ay, by + d, d):
                points[(ax, y)] += 1
        elif ay == by:
            d = int(copysign(1, bx - ax))
            for x in range(ax, bx + d, d):
                points[(x, ay)] += 1

    print(len([v for v in points.values() if v > 1]))