#!/usr/bin/env python
from rickroll import roll
import time
import socket
import threading
import sys
import signal


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
