import socket


def calculate_sum(numbers):
    lines = numbers.strip().split('\n')
    sums = []
    for line in lines:
        nums = line.split()
        nums = [int(num) for num in nums]
        line_sum = sum(nums)
        sums.append(line_sum)
    return sums


def handle_client(client_socket, addr):
    print(f"Kết nối từ {addr[0]}:{addr[1]}")
    while True:
        data = client_socket.recv(1024).decode()
        sums = calculate_sum(data)
        response = '\n'.join(str(sum) for sum in sums)
        client_socket.send(response.encode())


def main():
    server_ip = "127.0.0.1"
    server_port = 8890

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(1)
    print("Server đang lắng nghe...")

    while True:
        client_socket, addr = server.accept()
        handle_client(client_socket, addr)


if __name__ == "__main__":
    main()
