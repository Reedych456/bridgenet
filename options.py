import random

serverPort = 10001
clientPort = random.randrange(10000,29999)

serverHost = ''

# If you want to accept incoming connections (be a server), set serverStart variable to True
serverStart = False
# Known ip's
# How to write your ip correctly? You need to write your ip (without port) + , + port, example:
# peerList = ['127.0.0.1', 59386, '115.11.5.6', 58256]
peerList = ['127.0.0.1', 10001]
