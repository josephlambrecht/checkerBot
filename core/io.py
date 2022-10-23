FILE_MAP = {
    'a':7,
    'b':6,
    'c':5,
    'd':4,
    'e':3,
    'f':2,
    'g':1,
    'h':0,
}
RANK_MAP = {
    '1':0,
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
    '8':7
}
ALPHA_MAP = 'hgfedcba'

def from_square(square):
    file = FILE_MAP[square[0]]
    rank = RANK_MAP[square[1]]
    return rank,file

def to_square(rank,file):
    rank = int(rank) + 1
    return ALPHA_MAP[file] + str(rank)

def square(square):
    return from_square(square)

