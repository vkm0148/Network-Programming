import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

ip = '127.0.0.1'
port = 1000

server.bind((ip,port))

while True:
	data, addr = server.recvfrom(1024)
	print (f"received : {data.decode()} from {addr}")
	if data:
		send = "This is from the server"
		sent = server.sendto(send.encode(),addr)
		print (f"sent: {send} to {addr}")
