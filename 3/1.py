from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    most_common = [0] * len(lines[0])

    for line in lines:
        for i, bit in enumerate(line):
            most_common[i] += 1 if bit == '1' else -1

    most_common_bits = ''.join('1' if x > 0 else '0' for x in most_common)
    least_common_bits = ''.join('0' if x > 0 else '1' for x in most_common)
    gamma = int(most_common_bits, 2)
    epsilon = int(least_common_bits, 2)

    print(gamma * epsilon)
