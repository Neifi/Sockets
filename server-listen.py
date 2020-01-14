# Echo server program
import socket
import time



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))


print ("Starting server in localhost")
while True:
    print("OK")

    data = s.recvfrom(1024)
    if data == 'bye':
        time.sleep(1)
        s.close()

