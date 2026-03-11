import socket

PORT = 1238  # Port to listen on (non-privileged ports are > 1023)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()


def get_target_filename(s: str) -> str:
    out = {}
    lines = s.split("\r\n")
    target = lines.pop(0).split(" ")[1]
    print(f"get req: {target}")

    for line in lines:
        # print(f"parsing line {line}")
        if len(line) == 0:
            # print("skipping")
            continue
        key, value = line.split(":", 1)
        out[key] = value

    # print(out)
    return f".{target}"


while True:
    try:
        conn, addr = socket.accept()
        with conn:
            print(f"Connected by {addr}")

            data = conn.recv(1024)
            s = data.decode('utf-8')
            try:
                path = get_target_filename(s)
                print(f"getting path: {path}")
                with open(path, 'r') as f:
                    data = f.read()
                conn.sendall(f"HTTP/1.1 200 OK \r\n\
                        Content-Length: {len(data)} \r\n\
                        {data}\r\n\r\n".encode())
            except FileNotFoundError:
                conn.sendall("HTTP/1.1 404 Not Found \r\n\r\n".encode())

    except KeyboardInterrupt as e:
        print(f"git exception {e}")
        conn.close()
        break

socket.close()
