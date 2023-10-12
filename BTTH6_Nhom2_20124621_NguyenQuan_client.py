import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 8890

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        data = ""

        while True:
            line = input("Nhập chuỗi số: ")
            if line == ".":
                break
            data += line + "\n"

        client.send(data.encode())
        result = client.recv(1024).decode()
        print(result)


if __name__ == "__main__":
    main()
