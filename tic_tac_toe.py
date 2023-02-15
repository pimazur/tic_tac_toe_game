import numpy as np
from typing import Tuple

lines = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def make_a_move(board: np.ndarray, player_id: int, position: Tuple[int, int]) -> bool:
    if board[position] == 0:
        board[position] = player_id
        return True
    return False


def has_player_won(board: np.ndarray, player_id: int) -> bool:
    for line in lines:
        if all(board[position] == player_id for position in line):
            return True
    return False
