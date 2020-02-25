# Echo server program
import socket
import time
import threading


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8070              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
text = ""
print ("Starting server in localhost")

print ("Started")
print "**********SERVER**********"
# conn,addr = s.accept()
conList = []
# thread


def msgRecv(c, conList):
    name = ""
    while True:
        if name == "":
            # establecer nombre
            name = c.recv(1024)
            conList.append((c, name[:-1]))
            print ("-" + name)
        else:
            data = c.recv(1024)

            senderThread = threading.Thread(
                target=msgSend, args=(c, name, data))
            senderThread.start()

            if data == "bye\n":
                c.close()
                conList.remove(c)
                break


def acceptance():

    while True:
        conn, addr = s.accept()
  
        reciverThread = threading.Thread(target=msgRecv, args=(conn, conList))
        reciverThread.start()


def msgSend(c, nombre, text):
    for i in conList:
        if i[0] != c:
            i[0].sendall(nombre[:-1]+":"+text)
        

acceptanceThread = threading.Thread(target=acceptance)
# senderThread.daemon = True
acceptanceThread.start()

# senderThread.start()
acceptanceThread.join()

s.close()
