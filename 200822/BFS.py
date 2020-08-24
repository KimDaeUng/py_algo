# Breadth First Search
# * Use queue -> collections.deque 
# * Use set

# Example Graph(Use dict and list)


# BFS
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

if __name__ == "__main__":
    graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'G', 'H', 'I'],
            'D': ['B', 'E', 'F'],
            'E': ['D'],
            'F': ['D'],
            'G': ['C'],
            'H': ['C'],
            'I': ['C', 'J'],
            'J': ['I']
            }
    print(bfs(graph, 'A'))