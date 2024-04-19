def dfs(node, destination, graph, visited_nodes):
    if node in visited_nodes:
        return
    visited_nodes.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited_nodes)


def existing_path(source, destination, graph):
    visited_nodes = set()
    dfs(source, destination, graph, visited_nodes)

    return destination in visited_nodes


n = int(input())
graph = {}

edges = []
for _ in range(n):
    line = input().split(" -> ")
    graph[line[0]] = [x for x in line[1].split()] if line[1] else []

    for child in graph[line[0]]:
        edges.append((line[0], child))

removed_edges = []

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if existing_path(source, destination, graph):
        removed_edges.append((source, destination))

    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
[print(f'{source} - {destination}') for source, destination in removed_edges]

