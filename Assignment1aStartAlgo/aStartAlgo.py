def a_star_algorithm(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g_cost = {start_node: 0}
    parents = {start_node: None}

    while open_set:
        # Select the node with the lowest f(n) = g(n) + h(n)
        current_node = min(open_set, key=lambda n: g_cost[n] + heuristic(n))

        # If the goal node is reached, reconstruct the path
        if current_node == stop_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]  # Return reversed path

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor, weight in graph.get(current_node, []):
            if neighbor in closed_set:
                continue
            tentative_g_cost = g_cost[current_node] + weight

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_cost >= g_cost[neighbor]:
                continue

            # Update cost and parent
            g_cost[neighbor] = tentative_g_cost
            parents[neighbor] = current_node

    print("Path does not exist!")
    return None

def heuristic(node):
    h_distances = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return h_distances.get(node, float('inf'))

# Graph in adjacency list format
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)],
}
 
if __name__ == "__main__":
    path = a_star_algorithm('A', 'G')
    if path:
        print("Path found:", path)
