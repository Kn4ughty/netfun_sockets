import socket

PORT = 1237  # Port to listen on (non-privileged ports are > 1023)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()


def parse_http(s: str):
    out = {}
    lines = s.split("\r\n")

    for line in lines:
        key, value = line.split(":", 1)
        out[key] = value


while True:
    try:
        conn, addr = socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                s = data.decode('utf-8')
                parse_http(s)

                if not data:
                    break
                conn.sendall(data)
    except Exception as e:
        print(f"closing socket bc error {e}")
        socket.close()
