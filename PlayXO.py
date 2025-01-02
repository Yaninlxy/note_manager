def print_board(board):
    """Выводит текущее состояние игрового поля."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Проверяет, есть ли победитель."""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Проверяет, заполнено ли поле."""
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    """Запрашивает у игрока его ход."""
    while True:
        try:
            move = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row][col] == " ":
                return row, col
            else:
                print("Клетка занята или введён некорректный номер. Попробуйте снова.")
        except ValueError:
            print("Введите число от 1 до 9.")

def play_game():
    """Основная функция игры."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print("Номера клеток: ")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
    print("-" * 20)

    current_player = 0

    while True:
        print_board(board)
        row, col = get_move(players[current_player], board)
        board[row][col] = players[current_player]

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Поздравляем! Игрок {winner} выиграл!")
            break

        if is_full(board):
            print_board(board)
            print("Ничья! Поле заполнено.")
            break

        current_player = 1 - current_player  # Переключение между игроками

if __name__ == "__main__":
    play_game()
