from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    numbers = [int(l) for l in lines]

    count = 0
    for a, b in zip(numbers, numbers[1:]):
        if b > a:
            count += 1

    print(count)