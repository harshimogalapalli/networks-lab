import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),9090))

exp=1
l=[]
def notp(m,l):
	l.sort()
	for i in l:
		if i==m:
			return 0
	return 1 
def nextexp(m,l):
	for i in l:
		if i==m+1:
			m=m+1
	return m+1
	
	 

while True:
	m1=s.recv(1024)
	print m1
	m=int(m1)
	if exp==m:
		if notp(m,l):
			l.append(m)
			l.sort()
		else :
			print "dup"
		exp=nextexp(m,l)
	else:
		if notp(m,l):
			l.append(m)
			l.sort()
		else :
			print "dup"
		s.send("expected packet"+str(exp))	
