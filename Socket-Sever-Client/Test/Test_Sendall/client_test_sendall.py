import socket;
import time;
import logging;
logging.getLogger().setLevel(logging.INFO)
logging.info("start the client");
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ip_addr = '127.0.0.1';
ip_port = 6689
client.connect((ip_addr, ip_port));
logging.info('client has connected');
while(True):
    time.sleep(1)
    client.settimeout(1)
    client.send(b"test"*1024*64*4)
    logging.info('has sent')
    pass

# Problem Summary:
# 1. can only send the binary string b'test', sending the text string directly will cause problems
# 2.

# result: if the cient send or sendall but server don't receive them, the sending content will store in the queue and wait for receiving;
# if the send content is as much as enough, send will block and wait for receive;
# client settimeout will affect the client.send, if the time is long enough, it will casue error;