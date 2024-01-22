import sqlite3 
import threading
import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_binding = ("localhost", 8888)
ss.bind(server_binding)
ss.listen()

def start_connection(c):
    msg = " "
    c.send(msg.encode())

    response = c.recv(1024).decode()
    user = response
    print("Username: " + user)

    response = c.recv(1024).decode()
    password = response
    print("Password: " + password)

    conn = sqlite3.connect("users1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM user WHERE username = ?", (user,))
    row = cursor.fetchone()
    print (row)
    if row:
        db_password = row[0]
        print(db_password)
        if db_password == password:
            c.send("Login successful.".encode())
        else:
            c.send("Incorrect password.".encode())
    else:
        c.send("Username not found.".encode())


while(True):
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

ss.close()
exit()