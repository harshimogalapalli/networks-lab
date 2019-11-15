import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),9091))

exp=1
l=[]
	 

while True:
	m1=s.recv(1024)
	print m1
	m=int(m1)
	if exp==m:
		exp=exp+1
	else:
		s.send("expected packet"+str(exp))	
