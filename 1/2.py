from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    numbers = [int(l) for l in lines]

    count = 0
    previous_sum = None
    for a, b, c, d in zip(numbers, numbers[1:], numbers[2:], numbers[3:]):
        if b + c + d > a + b + c:
            count += 1

    print(count)