import heapq


# ---------------- Dijkstra's Algorithm ----------------

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """

    n = len(graph)

    dist = [float("inf")] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]      # (distance, vertex)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


# ---------------- Path Reconstruction ----------------

def reconstruct_path(prev, source, target):
    path = []

    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ---------------- Main Program ----------------

# Changed Graph
graph = {
    0: [(1, 2), (2, 6)],
    1: [(2, 3), (3, 1)],
    2: [(3, 2), (4, 4)],
    3: [(4, 2), (5, 5)],
    4: [(5, 1)],
    5: []
}

source = 0

dist, prev = dijkstra(graph, source)

print(f"Shortest Paths from Vertex {source}\n")

print(f'{"Vertex":>8} {"Distance":>10} {"Path":>25}')
print("-" * 50)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)

    if path:
        path_str = " -> ".join(map(str, path))
    else:
        path_str = "No Path"

    print(f"{v:>8} {dist[v]:>10} {path_str:>25}")
