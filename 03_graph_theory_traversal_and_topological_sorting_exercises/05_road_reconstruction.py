def dfs(source, destination, graph, visited):
    if source in visited:
        return
    visited.add(source)

    if source == destination:
        return

    for child in graph[source]:
        dfs(child, destination, graph, visited)


def not_path(source, destination, graph):
    visited = set()
    dfs(source, destination, graph, visited)

    return destination not in visited


buildings = int(input())
str_count = int(input())

graph = {}
streets = []
for _ in range(str_count):
    line = input().split(" - ")
    streets.append((line[0], line[1]))
    streets.append((line[1], line[0]))

    if line[0] not in graph:
        graph[line[0]] = []

    graph[line[0]].append(line[1])
    if line[1] not in graph:
        graph[line[1]] = []

    graph[line[1]].append(line[0])

valuable_streets = []

for source, destination in sorted(streets, key=lambda x: (x[0], x[1])):
    if source not in graph[destination] or destination not in graph[source]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if not_path(source, destination, graph):
        valuable_streets.append((source, destination))

    else:
        graph[source].append(destination)
        graph[destination].append(source)

print('Important streets:')
[print(f'{source} {destination}') for source, destination in valuable_streets]

