import socket;
import time;
import logging;


logging.getLogger().setLevel(logging.INFO)
logging.info("start the client");
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ip_addr = '127.0.0.1';
ip_port = 6689

# test 1:
# client.connect((ip_addr, ip_port));
# logging.info('client has connected');
# # client.close();
# time.sleep(1)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# client.connect((ip_addr, ip_port));
# logging.info('client has reconnected');
# # client.send(b'do this ')
# word = client.recv(1024);
# logging.info(word);

# conclusion:
# 1. if we close the client, we need reset client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# 2. if client close() or reset the client, though it can connect to the server, the server cannot send any message, that's because connect variable of server doesn't work, we need to accept again, and get new connect;
# 因此，对于client每个connect request, the server need to use accept to update them, if not, the connect will out of date and cannot work;
# 3. if the old connect send the binary words, but client update the client, the old binary word will be left.


# test 2
client.connect((ip_addr, ip_port));
logging.info('client has connected');
client.send(b'do this')
client.send(b'do this')