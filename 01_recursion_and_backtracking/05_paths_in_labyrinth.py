def labyrinth_paths(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)
    if lab[row][col] == 'e':
        print("".join(path))

    else:
        lab[row][col] = 'v'

        labyrinth_paths(row - 1, col, lab, "U", path)
        labyrinth_paths(row + 1, col, lab, "D", path)
        labyrinth_paths(row, col + 1, lab, "R", path)
        labyrinth_paths(row, col - 1, lab, "L", path)
        lab[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())
labyrinth = []

for _ in range(rows):
    labyrinth.append(list(input()))



labyrinth_paths(0, 0, labyrinth, '', [])
