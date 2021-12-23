from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

    ages = [int(x) for x in content.split(',')]

    for d in range(256):
        print(d)
        for i in range(len(ages)):
            ages[i] -= 1
            if ages[i] < 0:
                ages.append(8)
                ages[i] = 6

    print(len(ages))