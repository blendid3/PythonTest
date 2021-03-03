#!/usr/bin/python3
import time
import socket
import logging

class Client:
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        pass;

    def start(self):
        self.socketConnection();
        while True:
            try:
                self.run();
            except Exception as e:
                print(e, flush= True);
                self.socketDisconnect();
                while True:
                    time.sleep(5);
                    try:
                        self.socketReconnect();
                        break;
                    except Exception as e:

                        continue;

    def socketConnection(self):
        #### ip address
        self.ip_addre = '127.0.0.1'
        self.ip_port = 6699
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip_addre, self.ip_port))
        logging.info('socket has connected')
        pass;

    def socketReconnect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info('reconnect....');
        self.client.connect((self.ip_addre, self.ip_port))


    def socketDisconnect(self):
        self.client.close();

    def run(self):
        self.client.send(b"label_list");
        self.client.settimeout(15);
        data = self.client.recv(1024);
        if data == b'':
            raise RuntimeError("socket connection broken");
        print('Received', flush=True);
        print(data, flush=True)
        time.sleep(1);


client = Client();
client.start();

