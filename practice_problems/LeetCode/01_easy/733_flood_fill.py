# https://leetcode.com/problems/flood-fill/description/

from collections import deque


def flood_fill_bfs(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if image[sr][sc] == color:
        return image

    m = len(image)
    n = len(image[0])

    queue = deque([(sr, sc)])
    original_color = image[sr][sc]

    while queue:
        row, col = queue.popleft()
        image[row][col] = color
        neighbour_cells = get_cell_neighbours(row, col, m, n)
        for neighbour_row, neighbour_col in neighbour_cells:
            if image[neighbour_row][neighbour_col] == original_color:
                image[neighbour_row][neighbour_col] = color
                queue.append((neighbour_row, neighbour_col))

    return image


def flood_fill_dfs(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if image[sr][sc] == color:
        return image

    m = len(image)
    n = len(image[0])
    original_color = image[sr][sc]

    def flood_fill_recursive(row, col):
        if image[row][col] != original_color:
            return

        image[row][col] = color
        neighbour_cells = get_cell_neighbours(row, col, m, n)
        if not neighbour_cells:
            return

        for neighbour_row, neighbour_col in neighbour_cells:
            if image[neighbour_row][neighbour_col] == original_color:
                flood_fill_recursive(neighbour_row, neighbour_col)

    flood_fill_recursive(sr, sc)
    return image


def get_cell_neighbours(cell_row, cell_col, m, n):
    up_row = cell_row - 1
    down_row = cell_row + 1
    left_col = cell_col - 1
    right_col = cell_col + 1
    neighbours = []

    if up_row >= 0:
        neighbours.append((up_row, cell_col))

    if down_row < m:
        neighbours.append((down_row, cell_col))

    if left_col >= 0:
        neighbours.append((cell_row, left_col))

    if right_col < n:
        neighbours.append((cell_row, right_col))

    return neighbours


print(flood_fill_bfs([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(flood_fill_bfs([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
