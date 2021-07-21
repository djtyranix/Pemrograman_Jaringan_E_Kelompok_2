import os.path
from datetime import datetime
from urllib.parse import unquote
import re

class LoadBalancer:
	def __init__(self):
		self.server_list = []
		self.server_list.append(("localhost", 9000))
		#self.server_list.append(("localhost", 9001))
		#self.server_list.append(("localhost", 9002))
		#self.server_list.append(("localhost", 9003))
		#self.server_list.append(("localhost", 9004))
		self.counter = 0
	def get_server(self):
		server = self.server_list[self.counter]
		self.counter += 1
		if self.counter >= len(self.server_list) :
			self.counter = 0
		return server

if __name__=="__main__": 
	load_balancer = LoadBalancer()
	for i in range(0, 100):
		d = load_balancer.get_server()
		print(d)



#ab -n 10000 -c 10 http://localhost:55555/
#ab -n 10000 -c 10 http://localhost:8080/











