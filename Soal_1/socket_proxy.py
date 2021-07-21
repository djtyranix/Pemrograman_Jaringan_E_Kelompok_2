from socket import *
import socket
import threading
import time
import sys
import logging
from reverse_proxy import ReverseProxy

reverseProxy = ReverseProxy()

class ProcessTheClient(threading.Thread):
	def __init__(self, connection, address):
		self.destination_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.destination_sock.connect(destination_sock_address)
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		rcv=""
		while True:
			try:
				data = self.connection.recv(8192)
				if data:
					forward_response = reverseProxy.proses(data)
					logging.warning(forward_response)
					self.destination_sock.connect(forward_response['server'])
					self.destination_sock.sendall(forward_response['request'].encode())
					while True:
						data_balasan = self.destination_sock.recv(8192)
						if data_balasan:
							self.connection.sendall(data_balasan)
							#logging.warning(data_balasan)
						else:
							break
					logging.warning(data)
				else:
					break
			except OSError as e:
				pass
		self.connection.close()



class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		#self.destination_sock_address = ('localhost',8887)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('127.0.0.1', 8000))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			logging.warning("connection from {}".format(self.client_address))

			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)



def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()

