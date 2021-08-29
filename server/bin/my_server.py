import socket

import bin.settings as s


def action(data):
    return data.upper().encode("utf-8")


def run():
    sock = socket.socket()
    sock.bind((s.IP, s.PORT))

    sock.listen(1)

    print(f"start listen port {s.PORT}:")

    conn, addr = sock.accept()

    print("--- conection ---")

    while True:
        raw_data = conn.recv(1024)
        data = raw_data.decode("utf-8")

        if not data:
            break

        if data == 'stop':
            conn.send('kill'.encode("utf-8"))
            break

        print(f"ADDR: {addr} DATA: {data}")

        conn.send(action(data))

    conn.close()

