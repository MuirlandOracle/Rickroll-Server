#!/usr/bin/env python
import time
import pickle
import socket
import threading
import sys
import signal
import bz2
import os
import pwd
import grp


with bz2.BZ2File("rickroll.pbz2", "rb") as h:
    roll = pickle.load(h)


listensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensock.bind(("0.0.0.0", 23))
listensock.listen()

#Try to drop privileges having bound to the port
#0day was here
try:
    os.setgroups([])
    os.setgid(grp.getgrnam("nogroup").gr_gid)
    os.setuid(pwd.getpwnam("nobody").pw_uid)
except OSError:
    print("Failed to drop permissions")
    sys.exit()


def dataRecv(client, addr):
    print(f"[+] Connection from {addr[0]}")
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
