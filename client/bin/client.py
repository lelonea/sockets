import socket

def run():
	sock = socket.socket()
	sock.connect(('localhost', 9090))
	while sock:
		message = input("enter:")
		sock.send(message.encode('utf-8'))

		raw_data = sock.recv(1024)
		data = raw_data.decode("utf-8")
		print(f"Get: {data}")
		if data == 'kill':
			sock.close()
			break
