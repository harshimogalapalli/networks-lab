import socket
import sys
import select

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8901))

while True:
	socket_list=[sys.stdin,s]
	r,w,e=select.select(socket_list,[],[])
	for i in r:
		if i==s:
			m=s.recv(1024)
			print m
		else:
			st=raw_input()
			s.send(st)

		
