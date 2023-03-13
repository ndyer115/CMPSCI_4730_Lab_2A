from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('153.33.133.200', 8000))
serverSocket.listen(1)

while True:
    clientSocket, address = serverSocket.accept()
    print(f'Connection from {address} has been established')
    try:
        message = clientSocket.recv(1024).decode()
        filename = message.split()[1].partition('/')[2]
        f = open(filename)
        outputData = f.read()
        clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputData)):
            clientSocket.send(outputData[i].encode())
        clientSocket.send('\r\n'.encode())
        clientSocket.close()

    except IOError:
        clientSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        clientSocket.send('404 File Not Found'.encode())
        clientSocket.send('\r\n'.encode())
        clientSocket.close()

    serverSocket.close()
    sys.exit()
