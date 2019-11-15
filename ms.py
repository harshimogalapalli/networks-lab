import socket 
from thread import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),8901))
s.listen(11)
l=[]
def func(conn,addr):
	while True:
		m=conn.recv(1024)
		m='<'+addr[0]+'>'+m
		for i in l:
			if i!=conn:
				i.send(m)

while True:
	conn,addr=s.accept()
	l.append(conn)
	start_new_thread(func,(conn,addr))	
	
