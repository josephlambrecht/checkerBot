from core.io import to_square, from_square
import numpy as np

def evaluate_move(move):
    if 'x' in move:
        return len(move)
    return 0

def evaluate_moves(moves):
    ranking = np.zeros(len(moves))
    for i in range(len(moves)):
        ranking[i] = evaluate_move(moves[i])
    move = moves[np.argmax(ranking)]
    return move
