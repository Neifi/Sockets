import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(3)
conList = []


def acceptace(s):
    while True:
        conn, addr = s.accept()

        t = threading.Thread(target=msgRecv, args=(conn, conList))
        t.start()


def msgRecv(conn, conList):
    name = ""
    while True:
        if name == "":
            name = conn.recv(1024)
            conList.append((conn, name[:-1]))
        else:

            data = conn.recv(1024)

            t2 = threading.Thread(target=msgSend, args=(conn, name, data))
            t2.start()
            if data == "bye\n":
                conn.close()
                conList.remove(conn)

                break


def msgSend(conn, name, data):

    for x in conList:

        if x[0] == conn:
            pass
        else:
            x[0].sendall(name[:-1]+":"+data)


acceptaceThread = threading.Thread(target=acceptace, args=(s,))
acceptaceThread.start()
acceptaceThread.join()
s.close()
