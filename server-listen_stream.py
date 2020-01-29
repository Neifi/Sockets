# Echo server program
import socket
import time
import threading


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50015              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
text = ""
print ("Starting server in localhost")
conn, address = s.accept()
print ("Started")
print "**********SERVER**********"

def msgRecv(conn):
    while True:
        data = conn.recv(1024)
        print (":: " + data)
        if data == "bye":
            conn.sendall(data)
            break

def msgSend(conn,text):
    while True: 
        text = raw_input()
        if text:
            conn.sendall(text) 
        if text == 'bye':
            print "Closing connection..."
            break
    

reciverThread = threading.Thread(target=msgRecv, args=(conn,))
senderThread = threading.Thread(target=msgSend, args=(conn, text))
senderThread.daemon = True
reciverThread.start()
senderThread.start()

reciverThread.join()
s.close()
