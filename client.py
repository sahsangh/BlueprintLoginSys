import threading
import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_binding = ("localhost", 8888)
cs.connect(server_binding)

data_from_server = cs.recv(1024)
message = data_from_server.decode()
#print("[C] Data Received: " + message)
cs.send(input("Enter Username: ").encode())
cs.send(input("Enter Password: ").encode())

data_from_server = cs.recv(1024)
message = data_from_server.decode()
print(message)

cs.close()
exit()


