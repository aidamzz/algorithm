def dfs(node, graph, visited):
    stack = [node]
    visited[node] = True
    edges_count = 0
    
    while stack:
        u = stack.pop()
        for v in graph[u]:
            edges_count += 1
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    return edges_count // 2  # Each edge counted twice in undirected graph

def count_components_and_excess_edges(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1  # Convert to 0-based indexing
        v -= 1  # Convert to 0-based indexing
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    components = 0
    total_edges = 0
    
    for i in range(n):
        if not visited[i]:
            components += 1
            total_edges += dfs(i, graph, visited)
    
    excess_edges = len(edges) - (n - components)
    
    return components, excess_edges

def min_steps_to_tree(n, edges):
    components, excess_edges = count_components_and_excess_edges(n, edges)
    
    edges_to_add = components - 1
    
    return edges_to_add + excess_edges

# Example usage:
# Read input values
m, n = map(int, input().split())
edges = []

# Read edges
for _ in range(n):
    a, b = map(int, input().split())
    edges.append((a, b))

# Output the result
print(min_steps_to_tree(m, edges))
