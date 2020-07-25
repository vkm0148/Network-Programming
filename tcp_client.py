import socket
import time

target_host = "127.0.0.1"
target_port = 8080

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connect the client
client.connect((target_host,target_port))

# send some data
print ("[*] Connected to {}:{}".format(target_host,target_port))

diff = []
i = 0
while i<5:
	# receive some data
	msg = input("Enter your message:") 
	print (f"sending : {msg}")
	t1 = time.time_ns()
	client.send(msg.encode())
	response = client.recv(4096).decode()
	t2 = time.time_ns()
	
	print (i+1,". received from server : ",response)
	print ("throughput : ",len(response))
	diff.append((t2-t1)/2)
	print (f"diff = ",diff[i])
	i+=1

print (f"[*] Average delay : {sum(diff)/len(diff)} nanosecs")