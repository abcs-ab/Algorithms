"""Python implementation of Bellman-Ford algorithm."""


class NegativeWeightCycle(Exception):
    """Bellman-Ford negative weight cycle exception."""


def bellman_ford(graph, start):
    """Takes directed graph in a form of an adjacency list and a starting node.
    Returns distances and shortest paths from a starting node to every other vertex.
    graph example = {'s': {'t': 6, 'y': 7}, 't': {'x': 5, 'y': 8, 'z': -4}, ...}
    """

    # Initialize vertexes with distances set to inf and predecessor set to None.
    distances = {vertex: [float('inf'), None] for vertex in graph}
    distances[start] = [0, start]
    paths = {}

    # One more loop to detect cycles.
    is_any_dist_changed = False
    for _ in range(len(graph)):
        is_any_dist_changed = False
        for tail in graph:
            for head, dist in graph[tail].items():
                if distances[head][0] > distances[tail][0] + dist:
                    distances[head][0] = distances[tail][0] + dist
                    distances[head][1] = tail
                    is_any_dist_changed = True

        # If no distance has been changed, we can assume
        # the shortest path is already found, thus we can
        # break the loop and finish earlier.
        if not is_any_dist_changed:
            break

    # If any distance is changed in the last loop, than there's a cycle,
    # since max number of loops needed to construct the shortest path is |V|-1.
    if is_any_dist_changed:
        raise NegativeWeightCycle("Negative weight cycle detected.")

    # Reconstruct paths.
    for node in distances:
        predecessor = distances[node][1]
        node_path = [predecessor]
        while predecessor != start:
            predecessor = distances[predecessor][1]
            if predecessor in paths:
                node_path.extend(paths[predecessor])
                break
            else:
                node_path.append(predecessor)

        paths[node] = node_path

    paths = {i[0]: list(reversed(i[1])) + [i[0]] for i in paths.items()}

    return distances, paths


if __name__ == "__main__":
    no_cycle = {'s': {'t': 6, 'y': 7},
                't': {'x': 5, 'y': 8, 'z': -4},
                'y': {'z': 9, 'x': -3},
                'z': {'x': 7, 's': 2},
                'x': {'t': -2, 'y': 4}}

    cycle = {'s': {'t': 6, 'y': 7},
             't': {'x': 5, 'y': 8, 'z': -4},
             'y': {'z': 9, 'x': -3},
             'z': {'x': 7, 's': 2},
             'x': {'t': -2, 'y': 2}}

    print(bellman_ford(no_cycle, 's'))
    print(bellman_ford(cycle, 's'))
