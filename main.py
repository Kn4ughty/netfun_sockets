import socket

PORT = 1234  # Port to listen on (non-privileged ports are > 1023)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()


def parse_http(s: str):
    out = {}
    lines = s.split("\r\n")
    print(lines)
    #for line in lines:
        #key, value = line.split(":", 1)
        #out[key] = value


try:
    while True:
        conn, addr = socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                s = data.decode('utf-8')
                parse_http(s)

                if not data:
                    print("broke")
                    break
                #conn.sendall(data)
            print("out")
            conn.sendall("HTTP/1.1 204 No Content".encode("UTF-8"))
            conn.close()
except KeyboardInterrupt:
    print("FUCKKKKKk")
    socket.close()
