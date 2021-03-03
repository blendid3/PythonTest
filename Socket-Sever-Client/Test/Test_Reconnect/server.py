
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

# test 1
# i = 1;
# connect.send('test{0}'.format(i).encode())
# time.sleep(5)
# connect, (host, port) = server.accept();
# i += 1
# connect.send('test{0}'.format(i).encode())
# while True:
#     # word = 'test{0}'.format(i);
#     # connect.send('test{0}'.format(i).encode())
#     connect.settimeout(1)
#     # connect.send('test{0}'.format(i).encode())
#     connect.recv();
#     # connect.recv()
#
#     logging.info(i)
#     i += 1

# problem summary,
# 1. if the client exit, the server sendall will raise error ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
# 2. send need bytes string, using b'' or "word".encoding();
# 3. if the connect is out of date, but you send it using send, then it will rasie error;
# link: string conversion https://docs.python.org/3/library/string.html#formatspec


# test2
connect.settimeout(3)
time.sleep(2)
connect.recv(1024)
time.sleep(2)
connect.recv(1024)

