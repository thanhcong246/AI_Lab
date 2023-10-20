import heapq

def astar_tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    path = [start]
    cost = 0

    def heuristic(node, visited):
        # Tìm thành phố chưa thăm gần nhất
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and graph[node][i] < min_dist:
                min_dist = graph[node][i]
        return min_dist

    def astar(node, visited, path, cost):
        if len(path) == n:
            return path, cost + graph[node][start]

        h = heuristic(node, visited)
        best_path = None
        best_cost = float('inf')

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                new_path = path + [i]
                new_cost = cost + graph[node][i]
                f = new_cost + heuristic(i, visited)
                result_path, result_cost = astar(i, visited, new_path, new_cost)
                visited[i] = False

                if result_cost < best_cost:
                    best_cost = result_cost
                    best_path = result_path

        return best_path, best_cost

    best_path, best_cost = astar(start, visited, path, cost)
    return best_path, best_cost

# Ma trận khoảng cách giữa các thành phố
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 16],
    [21, 18, 16, 0]
]

start_city = 0
best_path, best_cost = astar_tsp(graph, start_city)
print("Đường đi tối ưu:", best_path)
print("Chi phí tối ưu:", best_cost)
