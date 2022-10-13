positions = [[' ' for i in range(3)], [' ' for i in range(3)], [
    ' ' for i in range(3)]]

welcomeMessage = '''
Добро пожаловать в игру крестики-нолики!
     столбец
 с  1 | 2 | 3 
 т ---|---|---
 р  4 | 5 | 6
 о ---|---|---
 к  7 | 8 | 9
 а
Ход вводится в виде двух символов: строка, столбец.
Пример: 0,0 или 2,2
Удачи!
'''


def isAllThreeInRow() -> tuple:
    xRow = ['X' for i in range(3)]
    oRow = ['O' for i in range(3)]
    for row in positions:
        if row == xRow:
            return True, 'Игрок1 выиграл!'
        elif row == oRow:
            return True, 'Игрок2 выиграл!'
    return False, ''


def isAllThreeInColumn() -> tuple:
    xColumn = ['X']*3
    oColumn = ['O']*3
    columns = []
    for col in range(3):
        column = [positions[row][col] for row in range(3)]
        columns.append(column)
    if xColumn in columns:
        return True, 'Игрок1 выиграл!'
    elif oColumn in columns:
        return True, 'Игрок2 выиграл!'
    else:
        return False, ''


def isAllThreeDiagonal() -> tuple:
    leftDiagonal = [positions[0][0], positions[1][1], positions[2][2]]
    rightDiagonal = [positions[0][2], positions[1][1], positions[2][0]]

    if (leftDiagonal == ['X']*3) or (rightDiagonal == ['X']*3):
        return True, 'Игрок1 выиграл!'
    elif (leftDiagonal == ['O']*3) or (rightDiagonal == ['O']*3):
        return True, 'Игрок2 выиграл!'
    return False, ''


def isDraw() -> tuple:
    countOfMovesMade = 0
    for row in positions:
        for item in row:
            if item != ' ':
                countOfMovesMade += 1

    if countOfMovesMade == 9:
        return True
    return False



def isGameOver() -> tuple:
    if isAllThreeInRow()[0]:
        return isAllThreeInRow()

    elif isAllThreeInColumn()[0]:
        return isAllThreeInColumn()

    elif isAllThreeDiagonal()[0]:
        return isAllThreeDiagonal()

    elif isDraw():
        return True, 'Ничья!'
    else:
        return False, ''


def isValidMove(row: int, column: int) -> bool:
    try:
        if positions[row][column] != ' ':
            return False
        return True
    except IndexError:
        return False



def makeMove(row: int, column: int, mark: str) -> None:
    positions[row][column] = mark



def takeInput(player: str) -> tuple:
    move = input(f'{player} введите свой ход: ')
    row, column = [int(i) for i in move.split(',')]
    return row, column


def generateBoard(x: list) -> None:
    board = f' {x[0][0]} | {x[0][1]} | {x[0][2]} \n---|---|---\n {x[1][0]} | {x[1][1]} | {x[1][2]} \n---|---|---\n {x[2][0]} | {x[2][1]} | {x[2][2]} '
    print(board)

def main() -> None:
    print(welcomeMessage)
    generateBoard(positions)
    players = {'X': 'Игрок1', 'O': 'Игрок2'}
    moves = 0
    while not isGameOver()[0]:

        if moves % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'

        player = players[mark]

        try:
            row, column = takeInput(player)
        except ValueError:
            print('Неправильный ввод, попробуйте ещё')
            continue

        if not isValidMove(row, column):
            print('Недоступный ход, попробуйте снова')
            continue

        makeMove(row, column, mark)
        generateBoard(positions)
        moves += 1
    else:
        print(isGameOver()[1])


if __name__ == "__main__":
    main()