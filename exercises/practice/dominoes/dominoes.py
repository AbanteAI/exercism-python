from collections import defaultdict

def dfs(node, graph, visited, chain, target_length):
    if len(chain) == target_length:
        return chain

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(neighbor, graph, visited, chain + [(node, neighbor)], target_length)
            if result:
                return result
    visited.remove(node)
    return None

def can_chain(dominoes):
    if not dominoes:
        return []

    graph = defaultdict(set)
    for (a, b) in dominoes:
        graph[a].add(b)
        graph[b].add(a)

    start = dominoes[0][0]
    visited = set()
    domino_chain = dfs(start, graph, visited, [], len(dominoes))

    if domino_chain:
        return domino_chain
    else:
        return []