# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connecting to localhost")
URL = (HOST,PORT)

while True:
    print("OK")
    data = raw_input()
    s.sendto(data, (HOST, PORT))
    if data == 'bye':
        break

s.close()
    


