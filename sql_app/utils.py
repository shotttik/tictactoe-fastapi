WIN_PATTERN = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def check_game_finished(board: list):
    for wp in WIN_PATTERN:
        if board[wp[0]] is None or board[wp[1]] is None or board[wp[2]] is None:
            continue
        if board[wp[0]] == board[wp[1]] and board[wp[1]] == board[wp[2]]:
            return True


def error_message(text: str) -> dict:
    return {"result": "error", "error_code": text}


def draw_board(db_board):
    board = """"""
    for i, t in enumerate(db_board):
        new_lines = [2, 5]
        if t == 0:
            board += "X |"
        elif t == 1:
            board += "Y |"
        else:
            board += "  |"
        if i in new_lines:
            board += "\n"
    return board
