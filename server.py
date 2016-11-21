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
    
    
    def handle(self):

        # Escribe dirección y puerto del cliente (de tupla client_address)

        #Leyendo linea a linea lo que nos envia el cliente
        data = self.rfile.read().decode('utf-8')
        METHOD = data.split(' ')[0]
        
      # Detección de método SIP
        if METHOD == 'INVITE':
            print("El cliente nos manda: " + data)
            self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
            self.wfile.write(b"SIP/2.0 180 Ring\r\n\r\n")
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

        elif METHOD == 'ACK':
            print("El cliente nos manda: " + data)
            aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + SONG
            print("Executing...", aEjecutar)
            print()
            os.system(aEjecutar)

        elif METHOD == 'BYE':
            print("El cliente nos manda: " + data)
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

        elif METHOD not in ['INVITE', 'ACK', 'BYE']:
            self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
        else:
            self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos

    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    SONG = sys.argv[3]
    print('IP: ' + IP)
    print('PORT: ' + str(PORT))

    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")

    elif sys.argv[3][-4:] != ".mp3":
        sys.exit("Usage: python server.py IP port audio_file")
    else:
        print('Listening...')

    serv = socketserver.UDPServer(('',PORT) , EchoHandler)
    print("Lanzando servidor UDP de eco...")
    
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")
