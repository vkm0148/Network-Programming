import socket
# import threading
import time

ip = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print ("server value",server)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind((ip,port))

#No. of clients waiting for connections that can be queued
server.listen(5)

print ("[*] Listening on {}:{}".format(ip,port))
# print ("Ctrl+C to close server")

while True:
	client,addr = server.accept()
	i = 1
	try:
		print (f"[*] Accepted connection from {addr[0]}:{addr[1]}\n")
		while True:
			# handle_client(client,addr)
			req = client.recv(1024).decode()
			# mili = time.time_ns()
			if req == '':
				break
			text = "This is message from server."
			print (f"{i}. sent : {text}")
			client.send(text.encode())
			print (f"Received : {req} \n Throughput : {len(req)}"),
			# print (f"")
			i+=1
	finally:
		print (f"\n[*]Closing client {addr[0]}:{addr[0]}")
		client.close()
		print (f"client {addr[0]}:{addr[1]} closed\n\n")

print ("closing server")
server.close()
print ("server closed")
