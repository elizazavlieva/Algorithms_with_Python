def depth_first_search(node, graph, visited_nodes, result):
    if node in visited_nodes:
        return

    visited_nodes.add(node)
    for children in graph[node]:
        depth_first_search(children, graph, visited_nodes, result)

    result.append(node)


n = int(input())
graph = {}
visited_nodes = set()
for i in range(n):
    line = input()
    child = [] if line == "" else [int(x) for x in line.split()]
    graph[i] = child


for node in graph:
    if node in visited_nodes:
        continue
    result = []
    depth_first_search(node, graph, visited_nodes, result)
    print(f"Connected component: {' '.join([str(x) for x in result])}")