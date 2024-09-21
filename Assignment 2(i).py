from collections import deque


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


def find_position(board, value):
    for i in range(3):
        for j in range(3):
            if board[i][j] == value:
                return i, j


def get_neighbors(board):
    neighbors = []
    x, y = find_position(board, 0)
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for dx, dy in directions:
        if 0 <= dx < 3 and 0 <= dy < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[dx][dy] = new_board[dx][dy], new_board[x][y]
            neighbors.append(new_board)

    return neighbors


def is_solved(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current_board, path = queue.popleft()
        visited.add(tuple(map(tuple, current_board)))

        if is_solved(current_board):
            return path + [current_board]

        for neighbor in get_neighbors(current_board):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [current_board]))

    return None


def print_solution(solution):
    for step in solution:
        print_board(step)
    print(f"Total moves: {len(solution) - 1}")


if __name__ == "__main__":
    print("Enter the initial board configuration (row by row, space-separated):")
    initial_board = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_board.append(row)

    print("Initial board:")
    print_board(initial_board)

    solution = bfs(initial_board)

    if solution:
        print("Solution found! Steps to solve the puzzle:")
        print_solution(solution)
    else:
        print("No solution exists!")