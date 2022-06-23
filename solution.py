board = [4, 3]
snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0], [0, 1]]
depth = 3


def initialize_board(board):
    """helper function to inicialize the array with zeros using the board dimentions"""
    return [[0] * board[1] for i in range(board[0])]  # multiply the quantity of column by the quantity of rows


def board_with_snake_coordinates(snake, board_array):
    """ setting up the snake into de bidimentional -array """
    for i, j in snake:
        board_array[i][j] = 1

    return board_array


def is_cell_empty(snake, cell):
    """Look for an empty cell"""
    snake = snake[0:len(snake) - 1] #removing the tail of the snake before search for an empty cell
    if cell not in snake:
        return True


def head_next_cell(snake, board):
    """Look for the posibles neigboor cells that the snake can go.
    In order to calculate it, we take in account that the snake can
    only move verticaly ([1,0] and [-1,0]) and horizontaly ([0,1],[0,-1]) from head"""
    head = snake[0]

    possible_next_cell = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    head_next_cell = []

    for i, j in possible_next_cell:
        n = head[0] + i
        m = head[1] + j

        if n >= board[0] or n < 0: #if the cell is out of the board, skip the cell
            continue

        if m >= board[1] or n < 0:
            continue

        if is_cell_empty(snake, [n, m]):
            head_next_cell.append([[n, m]] + snake[0:-1])

    return head_next_cell


def numberOfAvailableDifferentPaths(board, snake, depth):

    #Helper function only to visualize the result. Not necesary for the solution
    #board_array = initialize_board(board)
    #board_array = board_with_snake_coordinates(snake, board_array)

    pos_head_cell = head_next_cell(snake, board)

    if depth == 1:
        return len(pos_head_cell)

    higher_dimentions = []
    for i in range(depth-1):

        if (len(higher_dimentions) > 1):
            pos_head_cell = higher_dimentions
            higher_dimentions = []

        for item in pos_head_cell:
            higher_dimentions.extend(head_next_cell(item, board))

    print(len(higher_dimentions))
    return higher_dimentions


if __name__ == '__main__':

   numberOfAvailableDifferentPaths(board, snake, depth)









