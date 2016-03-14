import socket

intro_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
intro_socket.connect(("www.pythonlearn.com", 80))
intro_socket.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n")

while True :
    data = intro_socket.recv(512)
    if len(data) < 1 :
        break
    print data

intro_socket.close()
