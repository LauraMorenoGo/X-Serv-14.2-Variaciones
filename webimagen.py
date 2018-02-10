import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #Al socket le añadimos opciones adicionales REUSEADDR: el puerto no se libera directamente
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235)) #socket.gethostname(): coge el nombre de tu máquina

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello World!</h1>" +
                        b"<p>And in particular hello to you, " +
                        bytes(address[0], 'utf-8') +
                        b"</p><img src='https://gsyc.urjc.es/~mortuno/images/gsyc.png'\>" +
                        b"</body></html>" +
                        b"\r\n")    #address[0] es la IP, posición 1 es el puerto
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()    #Cierro el socket
