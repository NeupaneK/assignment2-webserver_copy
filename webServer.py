# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("127.0.0.1", port))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection

        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = serverSocket.recv(1024).decode()  # -a client is sending you a message 
            filename = message.split()[1]
            f = open(filename[1:], 'rb')
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
            connectionSocket.send(b"Content-Type: text/html; charset=UTF-8\r\n")
            connectionSocket.send(b"\r\n")

            

            # Send the content of the requested file to the client
            for i in f:  # for line in file
                connectionSocket.send(i)

            connectionSocket.close()  # closing the connection socket

        except IOError:
            # Send response message for invalid request due to the file not being found (404)
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")
            connectionSocket.send(b'<html><head></head><body>h1> 404 Not Found </h1></body></html>')
            connectionSocket.send(b"\r\n")
            connectionSocket.close()


    serverSocket.close()
    sys.exit()


if __name__ == "__main__":
    webServer(13331)
