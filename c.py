import socket
import sys
import select
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),9904))

exp=1	

while True:
	m1=s.recv(1024)
	m=int(m1)
	print m
	if exp==m:
		exp=exp+1
	else:
		s.send("packet to be sent"+str(exp))
		
