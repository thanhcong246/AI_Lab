import numpy as np

def greedy_tsp(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = [0]  # Bắt đầu từ thành phố 0
    visited[0] = True

    for _ in range(num_cities - 1):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None

        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < min_distance:
                min_distance = graph[current_city][city]
                nearest_city = city

        if nearest_city is not None:
            tour.append(nearest_city)
            visited[nearest_city] = True

    # Quay trở lại thành phố ban đầu
    tour.append(tour[0])

    total_distance = sum(graph[tour[i]][tour[i + 1]] for i in range(num_cities))

    return tour, total_distance

# Ma trận khoảng cách giữa các thành phố
graph = np.array([
    [0, 29, 20, 21],
    [29, 0, 15, 12],
    [20, 15, 0, 25],
    [21, 12, 25, 0]
])

tour, total_distance = greedy_tsp(graph)
print("Chuỗi thăm các thành phố:", tour)
print("Tổng khoảng cách:", total_distance)
