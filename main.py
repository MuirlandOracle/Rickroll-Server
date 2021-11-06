#!/usr/bin/env python
import time
import pickle
import socket
import threading
import sys
import signal
import bz2

with bz2.BZ2File("rickroll.pbz2", "rb") as h:
    roll = pickle.load(h)


listensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensock.bind(("0.0.0.0", 23))
listensock.listen()

def dataRecv(client, addr):
    for i in roll:
        if type(i) == float:
            time.sleep(i)
        else:
            for j in i:
                try:
                    client.send(j.encode())
                except:
                    return
    client.close()

print("Ready")
while True:
    try:
        client, addr = listensock.accept()
    except KeyboardInterrupt:
        listensock.close()
        sys.exit()
    except Exception:
        continue
    thread = threading.Thread(target=lambda:dataRecv(client, addr))
    thread.setDaemon(True)
    thread.start()
