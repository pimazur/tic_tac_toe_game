from tic_tac_toe import make_a_move, has_player_won
import numpy as np


def test_make_a_move():
    board = np.zeros((3, 3), dtype=int)
    assert make_a_move(board, player_id=1, position=(1, 1))
    np.testing.assert_equal(board, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert not make_a_move(board, player_id=-1, position=(1, 1))
    np.testing.assert_equal(board, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert make_a_move(board, player_id=-1, position=(0, 0))
    np.testing.assert_equal(board, [[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert not make_a_move(board, player_id=1, position=(1, 1))
    np.testing.assert_equal(board, [[-1, 0, 0], [0, 1, 0], [0, 0, 0]])


def test_has_player_won():
    board = np.array([
        [1, -1, 0],
        [-1, 1, -1],
        [1, 0, 1],
    ])
    assert has_player_won(board, player_id=1)
    assert not has_player_won(board, player_id=-1)
    board = np.array([
        [1, 1, 1],
        [-1, -1, -1],
        [1, 0, 1],
    ])
    assert has_player_won(board, player_id=1)
    assert has_player_won(board, player_id=-1)
    board = np.array([
        [1, -1, 1],
        [-1, 1, -1],
        [-1, 1, -1],
    ])
    assert not has_player_won(board, player_id=1)
    assert not has_player_won(board, player_id=-1)
