
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'G', 'H'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['C']
}


def dfs_stack(graph: dict, root: str):
    stack = []
    visit = []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


print(dfs_stack(graph, 'A'))


def dfs_recursive(graph, start, visit):
    visit.apend(start)
    for node in graph[start]:
        if node not in visit:
            dfs_recursive(graph, node, visit)

    return visit
