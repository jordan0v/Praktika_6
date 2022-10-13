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
