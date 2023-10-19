import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 8890

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        print("Menu:")
        print("1. Nhập dữ liệu")
        print("2. Đọc từ tệp data.txt")
        print("3. Kết thúc")

        choice = input("Chọn một tùy chọn (1/2/3): ")

        if choice == '1':
            data = ""

            while True:
                line = input("Nhập chuỗi số: ")
                if line == ".":
                    break
                data += line + "\n"

            with open("data.txt", "w") as file:
                file.write(data)

            client.send(data.encode())
            result = client.recv(1024).decode()
            print(result)
        elif choice == '2':
            with open("data.txt", "r") as file:
                data = file.read()
            client.send(data.encode())

            datas = client.recv(1024).decode().split('\n')
            for data in datas:
                if data:
                    print(data)
        elif choice == '3':
            break


if __name__ == "__main__":
    main()
