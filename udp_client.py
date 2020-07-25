import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip = '127.0.0.1'
server_port = 1000

message = "This is from client."

try:
	t1 = time.time_ns()
	print (f"sending {message} to {server_ip}")
	sent = server.sendto(message.encode(),(server_ip,server_port))
	data, serve = server.recvfrom(1024)
	t2 = time.time_ns()
	print (f"received {data.decode()} from {serve}")
	print (f"Delay : {(t2-t1)/2} ns")
	print ("throughput : ",len(data))

finally:
	print ("closing socket")
	server.close()