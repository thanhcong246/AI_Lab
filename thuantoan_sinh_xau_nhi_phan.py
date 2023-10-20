def generate_binary_strings(N):
    def backtrack(current):
        # Nếu độ dài hiện tại của xâu bằng N, in ra xâu đó và kết thúc
        if len(current) == N:
            print(current)
            return
        # Thử thêm ký tự '0' và '1' vào xâu hiện tại
        backtrack(current + '0')
        backtrack(current + '1')

    # Bắt đầu quá trình backtrack với xâu rỗng
    backtrack('')

try:
    # Lấy giá trị N từ người dùng và chuyển thành số nguyên
    N = int(input("Nhập giá trị của N: "))
    
    # Kiểm tra xem N có hợp lệ không (lớn hơn hoặc bằng 0)
    if N < 0:
        print("N phải là số nguyên không âm.")
    else:
        # Gọi hàm để tạo ra các xâu nhị phân có độ dài N
        generate_binary_strings(N)
except ValueError:
    print("Vui lòng nhập một số nguyên.")
