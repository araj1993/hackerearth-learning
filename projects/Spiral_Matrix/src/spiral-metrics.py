"""
Generate a square matrix of given size filled with numbers from 1 to size^2 in a spiral order.

Input: An integer representing the size of the matrix (size x size).
Output: A 2D list (matrix) filled in spiral order.

Example:
Input: 4

Output:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

def spiral_metrics(metrics_size, direction):

    if direction == "cw":
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif direction == "acw":
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    else:
        raise ValueError("Direction must be 'cw' or 'acw'")

    matrix = [[0] * metrics_size for _ in range(metrics_size)]
    row = col = 0
    dir_idx = 0
    num = 1

    while num <= metrics_size * metrics_size:
        matrix[row][col] = num
        num += 1

        next_row = row + directions[dir_idx][0]
        next_col = col + directions[dir_idx][1]

        if (0 <= next_row < metrics_size and 0 <= next_col < metrics_size and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            dir_idx = (dir_idx + 1) % 4
            row += directions[dir_idx][0]
            col += directions[dir_idx][1]

    for row in matrix:
        print(*[str(x).rjust(3) for x in row])

spiral_metrics(int(input("Enter the size of the matrix: ")), input("Enter the direction (cw/acw): ").strip().lower())