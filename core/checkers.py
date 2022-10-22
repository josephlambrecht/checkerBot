from core.io import to_square, from_square

def evaluate_move(start_square,end_square):
    return 1

def evaluate_moves(moves: dict):
    for start_square, possible_moves in moves.items():
        for end_square in possible_moves:
            # end square is a list
            if evaluate_move(start_square,end_square) == 1:
                return start_square, end_square
