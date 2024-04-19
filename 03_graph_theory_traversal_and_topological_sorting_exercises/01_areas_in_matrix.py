def dfs(row, col, matrix, visited, letter):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != letter:
        return

    visited[row][col] = True
    dfs(row + 1, col, matrix, visited, letter)
    dfs(row - 1, col, matrix, visited, letter)
    dfs(row, col + 1, matrix, visited, letter)
    dfs(row, col - 1, matrix, visited, letter)


n = int(input())
m = int(input())

matrix = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
areas = {}
total_areas = 0


for row in range(n):
    for col in range(m):
        if visited[row][col]:
            continue

        letter = matrix[row][col]
        dfs(row, col, matrix, visited, letter)

        if letter not in areas:
            areas[letter] = 0

        areas[letter] += 1
        total_areas += 1

sorted_areas = sorted(areas.items(), key=lambda kvp: kvp[0])
print(f"Areas: {total_areas}")
[print(f"Letter '{k}' -> {v}") for k, v in sorted_areas]