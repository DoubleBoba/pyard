import socket, threading, sys, time

sock = socket.socket()

def reciver():
	while True:
		data = sock.recv(1023)
		if not data: break
		print('recv:', data.decode('windows 1251'))
		time.sleep(0.05)
thread = threading.Thread(target=reciver)

def main():
	sock.connect((sys.argv[1], int(sys.argv[2]),))
	thread.daemon = True
	thread.start()
	while True:
		data = input()
		sock.send(data.encode('windows 1251'))

if __name__ == '__main__':
	main()