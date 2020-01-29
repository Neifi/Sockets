# Echo client program
import socket, threading

HOST = 'localhost'    # The remote host
PORT = 50015             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to localhost")
URL = (HOST, PORT)
s.connect(URL)
data = ""
print "********CLIENT*********"

def msgRecv(socket):
    while True:
        r = s.recv(1024)
        print (":: " + r)
        if r == "bye":
            s.sendall(r)
            break

def msgSend(socket, msg):
    while True:
        data = raw_input()
        if data:
            s.sendall(data)
        if data == "bye":
            print "Closing connection..."
            break

reciverThread = threading.Thread(target=msgRecv, args=(s,))
senderThread = threading.Thread(target=msgSend, args=(s,data))
senderThread.daemon = True
reciverThread.start()
senderThread.start()
reciverThread.join()
s.close()

    
