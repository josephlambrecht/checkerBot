# checkerBot
AI to play checkers

CheckerBot is a checkers playing program. 

MVP flow: Opponents move is typed into the terminal. CheckerBot processes the move and, using an AI strategy, prints out a move of its own.
Moves represented as (starting square) (x for jump or - for move) (ending square) (K at end for promotion) e5-d4, e5xc3, e5xc3xe1K


Necessary steps (abstracted | specific)
- Creata object classes for pieces | pawn and king with properties: color
- Store board state | 2d array with piece representation
- Calculate possible moves | three types- move, jump, double jump. check diagonals- if blocked check next, if open check jump. if jump check for more jumps.
- choose a move (this is where the fun begins)
- display the move and update board state


Expansion ideas:
- abstract to multiple games (chess, sorry, clue, othello, mancala, etc.)
- UI to show board on screen
- robot hand!
- computer vision! these two would let checkerBot play irl :)
- NLP would be useful for some games (Two truths one lie would be a great start). Speech to text has value here too maybe
- adjustable difficulty?
