#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os.path


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    
    IP = sys.argv[1]
    PORT = sys.argv[2]
    SONG = sys.argv[3]
    print('IP: ' + IP)
    print('PORT: ' + PORT)
    if len(sys.argv) != 4:
        if sys.argv[3][-4:] != ".mp3":
            sys.exit("Usage: python server.py IP port audio_file")
    else:
        print('Listening...')
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + text.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
