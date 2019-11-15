import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),9000))
while True:
	m1=raw_input()
	s.send(m1)
	m2=s.recv(1024)
	print m2

