# Function to check if it is safe to color vertex 'v' with color 'c'
def is_safe(graph, colors, v, c):
    for neighbor in graph[v]:
        if colors[neighbor] == c:
            return False
    return True

# Utility function to solve graph coloring problem recursively
def graph_coloring_util(graph, colors, v, color_list):
    if v == len(graph):  # Base case: If all vertices are assigned a color
        return True

    for c in color_list:
        if is_safe(graph, colors, v, c):
            colors[v] = c
            if graph_coloring_util(graph, colors, v + 1, color_list):
                return True
            colors[v] = None  # Backtrack

    return False

# Example graph as an adjacency list
graph = [
    [1, 2, 3],
    [0, 3],
    [0, 3],
    [0, 1, 2]
]
color_list = ["Red", "Green", "Blue"]
colors = [None] * len(graph)

# Solve the graph coloring problem
if not graph_coloring_util(graph, colors, 0, color_list):
    print("Solution does not exist")
else:
    for i in range(len(graph)):
        print(f"Vertex {i}: {colors[i]}")
