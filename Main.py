import socket
import time
import os
import platform
import binascii
import json
import traceback
from threading import *
from Packets.MessageFactory import *
from Logic.Device import Device

config = json.load(open("config.json", "r"))

class ServerThread():
    def __init__(self, ip, port):
        self.address = str(ip)
        self.port = int(port)
        self.client = socket.socket()

    def start(self):
        self.client.bind((self.address, self.port))

        print(f'[*] Server is listening on {self.address}:{self.port}'.format(self.address, self.port))

        while True:
            self.client.listen(5)
            client, address = self.client.accept()
            if config['Debug']:
                print('[*] New connection from {}'.format(address[0]))
            else:
                print(f"[*] New connection!")
            clientThread = ClientThread(client, address[0]).start()

    def stop(self):
        self.client.stop(self.address, self.port)


class ClientThread(Thread):
    def __init__(self, client, address):
        Thread.__init__(self)

        self.client = client
        self.address = address
        self.device = Device(self.client)

    def recvall(self, size):
        data = []
        while size > 0:
            self.client.settimeout(5.0)
            s = self.client.recv(size)
            self.client.settimeout(None)
            if not s:
                raise EOFError
            data.append(s)
            size -= len(s)
        return b''.join(data)

    def run(self):
        last_packet = time.time()
        while True:
            header   = self.client.recv(7)
            if len(header) >= 7:
                last_packet = time.time()
                packetid = int.from_bytes(header[:2], 'big')
                length   = int.from_bytes(header[2:5], 'big')
                version  = int.from_bytes(header[5:], 'big')
                data     = self.recvall(length)
                if len(header) > 0:
                    if packetid != 14102:
                        print('[*] {} received'.format(packetid))

                    try:
                        decrypted = self.device.decrypt(data)
                        if packetid in availablePackets:

                            Message = availablePackets[packetid](decrypted, self.device)

                            Message.decode()
                            Message.process()

                        else:
                            print('[*] {} not handled'.format(packetid))

                    except:
                            print('[*] Error while decrypting / handling {}'.format(packetid))
                            traceback.print_exc()
                else:
                    print('[*] Incorrect Length for packet {} (header length: {}, data length: {})'.format(packetid, length, len(data)))
            else:
                print(f"[*] Received an invalid packet from client!")
                self.client.close()

if __name__ == '__main__':
    # Install requirements
    os.system("py -m pip install -r requirements.txt")

    # Platform stuff
    if os.name == "nt":  # Windows
        os.system("title ClassicClash")
    else:  # Linux/MacOS
        print("\033]0;ClassicClash\007", end="")
    os.system("cls" if platform.system() == "Windows" else "clear")

    print("""
  ____ _               _       ____ _           _     
 / ___| | __ _ ___ ___(_) ___ / ___| | __ _ ___| |__  
| |   | |/ _` / __/ __| |/ __| |   | |/ _` / __| '_ \ 
| |___| | (_| \__ \__ \ | (__| |___| | (_| \__ \ | | |
 \____|_|\__,_|___/___/_|\___|\____|_|\__,_|___/_| |_|
    """)
    print('Server created by @Greedycell on Github!')
    print()

    # Listener
    try:
        server = ServerThread("0.0.0.0", 9339)
        server.start()
    except OSError as e:
        print("[*] Server already running:", e)
