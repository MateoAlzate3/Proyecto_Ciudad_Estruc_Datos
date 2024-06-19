import heapq


def dijkstra_shortest_path(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    shortest_path_tree = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    path, node = [], end
    while node in shortest_path_tree:
        path.insert(0, node)
        node = shortest_path_tree[node]

    if path:
        path.insert(0, start)

    return path