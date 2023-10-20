def is_safe(graph, v, c, color):
    # Hàm kiểm tra xem màu c có thể được sử dụng cho khu vực v không.
    # Duyệt qua các khu vực kề v (được biểu diễn trong ma trận đồng cấu graph).
    # Nếu có một khu vực kề đã được tô màu bằng màu c, trả về False, ngược lại trả về True.
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m, v, color):
    # Hàm thực hiện thuật toán tô màu.
    # Nếu tất cả các khu vực đã được tô màu, trả về True.
    if v == len(graph):
        return True

    # Thử tô các màu từ 1 đến m cho khu vực v.
    for c in range(1, m + 1):
        # Kiểm tra nếu màu c có thể được sử dụng cho khu vực v.
        if is_safe(graph, v, c, color):
            color[v] = c
            # Đệ quy để tô màu các khu vực tiếp theo.
            if graph_coloring(graph, m, v + 1, color):
                return True
            # Nếu không tìm thấy lời giải, quay lui bằng cách đặt lại màu của khu vực v.
            color[v] = 0

    # Nếu không tìm thấy lời giải tại đỉnh v, trả về False.
    return False

def print_solution(graph, color):
    # Hàm in ra lời giải bằng cách hiển thị màu của từng khu vực.
    for i in range(len(graph)):
        print("Khu vực {} được tô màu màu {}.".format(i + 1, color[i]))

def solve_graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n  # Tạo mảng lưu trữ màu của từng khu vực, ban đầu chúng đều chưa được tô màu.

    if not graph_coloring(graph, m, 0, color):
        print("Không tìm thấy lời giải.")
        return False

    print("Lời giải:")
    print_solution(graph, color)
    return True

# Ví dụ: Ma trận kề thể hiện bản đồ
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

m = 3  # Số lượng màu có sẵn

solve_graph_coloring(graph, m)
