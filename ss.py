import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),8178))
s.listen(10)
conn,addr=s.accept()

while True:
	msg=conn.recv(1024)
	print msg
	msg1= ''
	for i in msg:
		msg1=i+msg1
	conn.send(msg1)
	
conn.close()

