import socket

PORT = 1234  # Port to listen on (non-privileged ports are > 1023)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()


def parse_http(s: str):
    out = {}
    lines = s.split("\r\n")
    get = lines.pop(0)
    print(f"get req: {get}")

    for line in lines:
        print(f"parsing line {line}")
        if len(line) == 0:
            print("skipping")
            continue
        key, value = line.split(":", 1)
        out[key] = value

    print(out)


while True:
    try:
        conn, addr = socket.accept()
        with conn:
            print(f"Connected by {addr}")

            data = conn.recv(1024)
            s = data.decode('utf-8')
            parse_http(s)

            conn.sendall("HTTP/1.1 200 OK \r\n\r\n".encode())
    except KeyboardInterrupt as e:
        print(f"git exception {e}")
        conn.close()
        break

socket.close()
