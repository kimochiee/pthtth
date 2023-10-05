import socket
import threading


def reverse_and_capitalize(data):
    words = data.split()
    result = ' '.join([word.capitalize() for word in reversed(words)])
    return result


def calculate_sum(data):
    numbers = [int(num) for num in data.split()]
    result = sum(numbers)
    return str(result)


def handle_client(client_socket, addr):
    print(f"Kết nối từ {addr[0]}:{addr[1]}")
    while True:
        request = client_socket.recv(1024).decode()
        print(f"Đã nhận yêu cầu từ client: {request}")

        if request == "1":
            client_socket.send("Nhập chuỗi: ".encode())
            data = client_socket.recv(1024).decode()
            result = reverse_and_capitalize(data)
            client_socket.send(result.encode())
        elif request == "2":
            client_socket.send("Nhập chuỗi số nguyên: ".encode())
            data = client_socket.recv(1024).decode()
            result = calculate_sum(data)
            client_socket.send(result.encode())
        elif request == "3":
            client_socket.close()
            break
        else:
            result = "Yêu cầu không hợp lệ."
            client_socket.send(result.encode())


def main():
    server_ip = "127.0.0.1"
    server_port = 8890

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print("Server đang lắng nghe...")

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == "__main__":
    main()
