#!/usr/bin/python3
"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #He creado un socket de Internet de TCP
mySocket.bind(('localhost', 1234))  #atamos nuestro socket a un sitio(le decimos:tú vas a estar escuchando aquí)
                                    #localhost: máquina, 1234: puerto

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)  #puede escuchar hasta 5 peticiones

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()   #Si alguien se conecta, lo acepto y se crea una tupla, tengo su socket, para cuando quiera coger cosas de su socket necesito su socket
    print('HTTP request received:') 
    print(recvSocket.recv(1024))    #un buffer con los 1024 primeros bytes y los imprimo
    recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                    b"<html><body>" +
                    b"<a href='https://gsyc.urjc.es'>GSyC</a>" +
                    b"</body></html>" +
                    b"\r\n")    #lenguaje http porque es un servidor
    recvSocket.close()
