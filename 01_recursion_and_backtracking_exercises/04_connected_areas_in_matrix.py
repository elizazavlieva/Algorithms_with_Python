def explore_area(row, col, matrix):

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

area = {}
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size != 0:
            area[(row, col)] = size

sorted_areas = sorted(area.items(), key=lambda x: -x[1])
result = [f"Total areas found: {len(sorted_areas)}"]
index = 1
for area, size in sorted_areas:
    result.append(f"Area #{index} at {area}, size: {size}")
    index += 1

print("\n".join(result))
