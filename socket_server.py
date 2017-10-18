# -*- coding: utf-8 -*-
import socket
import sys
import time
from thread import *

global flog
HOST = '192.168.0.104'
PORT = 8888

# def _clientthread(conn):
# 	conn.send('Welcome to the server. Type something and hit enter\n\r\n\r\n\r')
# 	while True:
# 		data = conn.recv(1024)
# 		reply = 'OK...' + data
# 		if data == 'close\r\n':
# 			print 'Server Closed !'
# 			conn.close()
# 			break
# 		elif data == ' \r\n':
# 			print 'I\'m a space!'
# 			conn.sendall('\r\n')
# 		else:
# 			print reply
# 			conn.sendall(reply)
# 	#conn.close()

def _clientthread(conn):
	conn.send('Welcome to the server. Type something and hit enter\n\r')
	while True:
		data = conn.recv(1024)
		reply = 'OK...' + data
		if data == 'close\r\n':
			print 'Server Closed !'
			conn.close()
			break
		elif data == ' \r\n':
			print 'I\'m a space!'
			conn.sendall('\r\n')
		else:
			print reply
			conn.sendall(reply)
		time.sleep(3)


server_HOST = '192.168.0.104'
server_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
print 'HOST is ' +  HOST
print 'PORT is ' +  str(PORT)
try:
	print 'I \'m Here'
	s.bind((HOST, PORT))
	print 'I \'m Here Here'
except socket.error, msg:
	print 'Bind failed. Error Code: ' + str(msg[0]) + 'Message ' + str(msg[1])
	sys.exit()
print 'Socket bind complete'
s.listen(10)
print 'Socket now listening'
while True:
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(_clientthread, (conn,))
	#_clientthread(conn)
	print "i am a marker!"



