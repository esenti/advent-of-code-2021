from pathlib import Path

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()

    x = y = 0
    for line in lines:
        command, arg = line.split()

        if command == 'forward':
            x += int(arg)
        elif command == 'up':
            y -= int(arg)
        elif command == 'down':
            y += int(arg)

    print(x * y)