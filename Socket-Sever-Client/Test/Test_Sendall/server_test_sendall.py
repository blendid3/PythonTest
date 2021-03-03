
# test the server send and recv
import socket
import logging;
import time;
logging.getLogger().setLevel(logging.INFO)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ip_addr = '127.0.0.1';
ip_port = 6689
server.bind((ip_addr, ip_port));
server.listen();
logging.info("waiting for connectiong...");
connect, (host, port) = server.accept();

while True:
    time.sleep(1)

    connect.sendall(b'test')
    logging.info("has sent")

# problem summary,
# 1. if the client exit, the server sendall will raise error ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host