from pathlib import Path

def mark_board(board, mark, n):
    try:
        mark[board.index(n)] = True
    except ValueError:
        pass

def is_board_winning(mark):
    for i in range(5):
        if mark[5*i:5*i+5] == [True] * 5:
            return True
        
        if [mark[i], mark[i + 5], mark[i + 10], mark[i + 15], mark[i + 20]] == [True] * 5:
            return True

    return False

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as f:
        content = f.read()

    fragments = content.split('\n\n')

    numbers = [int(x) for x in fragments[0].split(',')]
    boards = []
    marks = []

    for fragment in fragments[1:]:
        board = [int(x) for x in fragment.split()]
        mark = [False] * len(board)
        boards.append(board)
        marks.append(mark)

    won_boards = []
    end = False

    for n in numbers:
        for board, mark in zip(boards, marks):
            if board in won_boards:
                continue

            mark_board(board, mark, n)
            if is_board_winning(mark):
                won_boards.append(board)
                if len(won_boards) == len(boards):
                    s = sum(b for i, b in enumerate(board) if not mark[i])
                    end = True
                    break

        if end:
            print(n * s)
            break