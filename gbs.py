import socket
import sys
import select
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),9091))
s.listen(20)
conn,addr=s.accept()
while True:
	select_list=[sys.stdin,conn]
	r,w,e=select.select(select_list,[],[])
	for i in r:
		if i==conn:
			m=conn.recv(1024)
			print m
		else:
			st=raw_input()
			conn.send(st)
	
