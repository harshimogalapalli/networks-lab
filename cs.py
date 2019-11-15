import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8178))
while True:
	st=raw_input("enter")
	s.send(st)
	msg11=s.recv(1024)
	print msg11
	
s.close()
	

