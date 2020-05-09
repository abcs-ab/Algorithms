"""Python implementation of Dijkstra's shortest path algorithm."""

import heapq


testcase = {
    'a': {'b': 4, 'c': 3, 'e': 7},
    'b': {'a': 4, 'c': 6, 'd': 5},
    'c': {'a': 3, 'b': 6, 'd': 11, 'e': 8},
    'd': {'b': 5, 'c': 11, 'e': 2, 'f': 2, 'g': 10},
    'e': {'a': 7, 'c': 8, 'd': 2, 'g': 5},
    'f': {'d': 2, 'g': 3},
    'g': {'d': 10, 'e': 5, 'f': 3}
}


def dijkstra(graph, start, end=None):
    visited = {start}
    distances = {start: 0}
    paths = {start: [start]}
    edges = []  # priority queue
    tail = start
    for _ in range(len(graph) - 1):
        prev_dist = distances[tail]
        for head, dist in graph[tail].items():
            if head in visited:
                continue

            edge = (prev_dist + dist, head, tail)
            heapq.heappush(edges, edge)

        while edges:
            d, h, t = heapq.heappop(edges)  # dist, head, tail
            if h not in visited:
                visited.add(h)
                distances[h] = d
                paths[h] = paths[t] + [h]
                tail = h

                if h == end:
                    return distances[h], paths[h]
                break

    return distances, paths


if __name__ == "__main__":
    from display_graph import display_graph

    _, shortest_path = dijkstra(testcase, 'a', 'f')
    shortest_path_edges = [tuple(shortest_path[i:i + 2]) for i in range(len(shortest_path) - 1)]

    display_graph(testcase, shortest_path_edges)
