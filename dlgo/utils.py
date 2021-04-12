from dlgo import gotypes

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    gotypes.Player.black: ' x ',
    gotypes.Player.white: ' o ',
}

def print_move(player, move):
    """Print a player's move."""
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = '%s%d' % (COLS[move.point.col-1], move.point.row)
    print('%s %s' % (player, move_str))

def print_board(board):
    """Print the current board."""
    for row in range(board.num_rows, 0, -1):
        bump = " " if row <= 0 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('   ' + '  '.join(COLS[:board.num_cols]))

def point_from_coords(coords):
    """Transform human input into coordinates."""
    col = COLS.index(coords[0]) + 1
    row = int(coords[1:])
    return gotypes.Point(row=row, col=col)

def coords_from_point(point):
    """Transform coordinates into human input."""
    return '%s%d' % (COLS[point.col - 1], point.row)