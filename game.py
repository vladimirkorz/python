# Крестики нолики
# Надо добавить в блок except в gamy.py обработку исключения ValueError.
# В случае, если пользователь ввел буквы, должно выводится два сообщения:
# 1. Буквы вводить нельзя. Только числаю 
# 2. Пожалуйста введите значение для строки и столбца заново.

print('aboba')

from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    while running:
        print(f'ход делает{current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' '
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
            except ValueError
                print('Буквы вводить нельзя. Только числаю')
                print('Пожалуйста введите значение для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала, предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except Exception as e:
                print(f'возникла ошибка')
            else:
                # ...значит, введённые значения прошли все проверки и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()


game.make_move(row, column, current_player)
game.display()

class FieldIndexError(IndexError):
    def __str__()

class CellOccupiedError(Exception):

    def __str__(self):
        return 'попытка изменить занятую ячейку'




def dislpay(self):

def is_board_ful(self):
    for i in range(self.field_size):
        for j in range(self.field_size):
            if self.board[i][j] == ' ':
                return False
    return True

def check_win(self, player):
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False
    