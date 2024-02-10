def shortest(graph, src, target):
    previous_node = {node: None for node in graph.keys()}
    distances = {node: float('inf') for node in graph.keys()}
    distances[src] = 0
    unvisited = [node for node in graph.keys()]
    path = []

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        if current_node == target:
            break

        else:
            unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:
                d = distances[current_node] + weight
                if d < distances[neighbor]:
                    distances[neighbor] = d
                    previous_node[neighbor] = current_node

    curr_node = target
    while curr_node:
        path.insert(0, curr_node)
        curr_node = previous_node[curr_node]

    return path, distances[target]


graph = {
    "A": {"B": 1, "C": 1},
    "B": {"D": 1, "E": 1, "F": 1},
    "C": {"D": 1},
    "D": {"F": 1, "J": 1},
    "E": {"I": 0.2},
    "F": {"E": 1, "G": 1},
    "G": {},
    "I": {"O": 0.2},
    "O": {"G": 0.2},
    "J": {"C": 1}
}

path, distance = shortest(graph, "A", "G")
print("Minimum distance: ", distance)
print(*path, sep=" => ")
