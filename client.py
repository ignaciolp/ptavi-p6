#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.

METHOD = sys.argv[1]
LOGIN = sys.argv[2].split("@")[0]
PORT = int(sys.argv[2].split("@")[1].split(":")[1])
SERVER = sys.argv[2].split("@")[1].split(":")[0]

print("Servidor:" , SERVER)
print("Puerto:" , PORT)
print("Usuario:" , LOGIN)

if len(sys.argv) !=3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

if METHOD not in ['INVITE', 'BYE']:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

LINE_INF = ' sip:' + LOGIN + "@" + SERVER + " SIP/2.0\r\n\r\n"
LINE = METHOD + LINE_INF

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
