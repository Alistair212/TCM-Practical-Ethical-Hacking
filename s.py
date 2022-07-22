#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

#AF_INET = IVP4
#SOCK_STREAM = PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
