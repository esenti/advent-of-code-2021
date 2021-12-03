from pathlib import Path


def find_most_common_bit(values, i):
    x = 0
    for v in values:
        x += 1 if v[i] == '1' else -1

    return '1' if x >= 0 else '0'


if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    numbers = lines[:]

    i = 0
    while len(numbers) > 1:
        bit = find_most_common_bit(numbers, i)
        numbers = [n for n in numbers if n[i] == bit]
        i += 1

    oxygen = int(numbers[0], 2)

    numbers = lines[:]

    i = 0
    while len(numbers) > 1:
        bit = find_most_common_bit(numbers, i)
        bit = '0' if bit == '1' else '1'
        numbers = [n for n in numbers if n[i] == bit]
        i += 1

    co2 = int(numbers[0], 2)

    print(oxygen * co2)