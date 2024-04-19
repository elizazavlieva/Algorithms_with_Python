def dfs(emp, graph, salaries):
    if salaries[emp]:
        return salaries[emp]

    if len(graph[emp]) == 0:
        salaries[emp] = 1
        return 1

    salary = 0
    for child in graph[emp]:
        salary += dfs(child, graph, salaries)

    salaries[emp] = salary
    return salary


n = int(input())
graph = []

for _ in range(n):
    line = list(input())
    children = []
    for idx in range(len(line)):
        if line[idx] == 'Y':
            children.append(idx)

    graph.append(children)

salaries = [None] * n
total_salary = 0


for emp in range(n):
    total_salary += dfs(emp, graph, salaries)

print(total_salary)
