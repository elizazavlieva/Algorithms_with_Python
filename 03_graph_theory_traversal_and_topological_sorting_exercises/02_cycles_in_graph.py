def find_dependencies(graph):
    result = {}
    for node, child in graph.items():
        if node not in result:
            result[node] = 0

        if child not in result:
            result[child] = 1

        else:
            result[child] += 1

    return result


def find_node_without_dependency(dependencies_by_node):
    for node, dep in dependencies_by_node.items():
        if dep == 0:
            return node

    return None


graph = {}

line = input()
while line != "End":
    nodes = line.split('-')
    graph[nodes[0]] = nodes[1]
    line = input()

dependencies_by_node = find_dependencies(graph)
is_valid = True

while True:
    node_to_remove = find_node_without_dependency(dependencies_by_node)
    if not node_to_remove:
        is_valid = False
        break

    dependencies_by_node.pop(node_to_remove)
    if not dependencies_by_node:
        break

    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

result = "Yes" if is_valid else "No"
print(f"Acyclic: {result}")
