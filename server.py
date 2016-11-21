#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    
    IP = sys.argv[1]
    PORT = (sys.argv[2])
    SONG = sys.argv[3]
    print('IP: ' + IP)
    print('PORT: ' + PORT)

    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")

    elif sys.argv[3][-4:] != ".mp3":
        sys.exit("Usage: python server.py IP port audio_file")
    else:
        print('Listening...')

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))
            elem = line.split(' ')
            METHOD = elem[0]
            if METHOD == 'INVITE':
                self.wfile.write(b"SIP/2.0 100 Trying,SIP/2.0 180 Ring y SIP/2.0 200 OK\r\n\r\n")
            if METHOD not in ['INVITE', 'ACK', 'BYE']:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('',int(sys.argv[2]) ), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
