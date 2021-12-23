from pathlib import Path
from functools import reduce

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

    positions = [int(x) for x in content.split(',')]
    
    print(min(reduce(lambda x, y: x + abs(y - i), positions, 0) for i in range(min(positions), max(positions) + 1)))