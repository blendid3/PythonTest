
#!/usr/bin/python3
import time
import socket
import logging
class Server_PC:
    def __init__(self):
        ## section1: file and floder creation
        self.socketInit();
        logging.getLogger().setLevel(logging.INFO)

    def start(self):
        print('start');
        self.socketConnection();
        while True:
            try:
                self.run();
            except Exception as e:
                print(e);
                self.socketDisconnect()
                try:
                    time.sleep(1)
                    self.socketReconnect();
                except Exception as e:
                    print(e);


    def socketInit(self):
        self.ip_addr='127.0.0.1'
        self.ip_port = 6699

    def socketConnection(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip_addr, self.ip_port))
        self.server.listen()
        # logging.info()
        print(u'waiting for connect...')
        self.connect, (host, port) = self.server.accept()
        print(u'the client %s:%s has connected.' % (host, port))

    def socketReconnect(self):
        logging.info("try reconnecting")
        self.server.listen()
        print(u'waiting for reconnect...')
        self.connect, (host, port) = self.server.accept()
        print(u'the client %s:%s has connected.' % (host, port));
        pass
    def socketDisconnect(self):
        self.connect.close();
        pass

    def run(self):
        self.connect.settimeout(5);
        # print('try 1')
        chunk = self.connect.recv(1024);
        if chunk == b'':
            raise RuntimeError("socket connection broken");
        logging.info(chunk)
        logging.info("label_list has received");
        time.sleep(7);
        self.connect.sendall(b'your label_list has received.');
        logging.info('has complete')

print("label_list has received");
server = Server_PC();
server.start();