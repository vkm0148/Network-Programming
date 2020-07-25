DESCRIPTION 

1) TCP client-server:
	
	The tcp client-server model written in python where the server is started by default in localhost with a port which is available. The client is connected to the server using the ip and port on which the server is running and sends a message to the server and simultaneously records the time at of sending the message. The server after accepting the connection and receiving the message from client, prints the message and calculates the throughput of the message received and returns a confirmation message to the client where the client also calculates the throughput of the message received and records the time of receiving the message and displays the RTT of the message transfer.

		Usage : python3 tcp_server.py  - to start the server
			python3 tcp_server.py  - to start the client

2) UDP client-server:

	The udp client-server model is same as the tcp client-server but uses UDP connection instead of TCP connection where no handshake between server and client takes place. The data transfer takes place purely on the basis of address specified.

		Usage : python3 udp_server.py  - to start the server
			python3 udp_server.py  - to start the client

3) HTTP client-server:
	
	This model written in C language, has a server which starts and accepts connection and a client which connects to the server using IP address and port number on which the server is running. The client after connection sends the name of a file which may or may not be present in the server to which the server responds with the first 10 characters of the file or an error message for the file if the file specified is present or not respectively.

		Usage : ./http_server <port>
			./http_client <hostname/ip> <port>

			PS : Run these to compile C code if changing the source code or executable not working
					gcc -o http_server -w http_server.c
					gcc -o http_client -w http_client.c


NOTE : 

1) In some cases, your system might require explicit permissions to create a new socket. Please use "sudo" (without quotes) at 	
	the beginning of the command or if using command prompt, run it as administrator.
	
2) For python codes if you encounter an error saying "No module found name <xyz>",
	   	  sudo pip3 install <xyz>



