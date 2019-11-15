import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),9000))
s.listen(10)
conn,addr=s.accept()
while True:
	msg=conn.recv(1024)
	print msg
	m=raw_input()
	conn.send(m)
	
