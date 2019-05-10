from typing import Dict, List
from PodSixNet.Connection import connection, ConnectionListener
import pickle
from _thread import *
from copy import deepcopy
from collections import defaultdict, deque


class Client(ConnectionListener):
	actions = defaultdict(lambda: [])
	players_order = []

	def __init__(self, host, port, player_name):
		self.Connect((host, port))
		self.player_name = player_name
		connection.Send({"action": "player_name", "player_name": player_name})
		# t = start_new_thread(self.InputLoop, ())

	def get_action(self):
		player_events = deepcopy(self.actions[self.player_name])
		del self.actions[self.player_name]
		return player_events


	def Update(self):
		connection.Pump()
		self.Pump()

	def send_action(self, action):
		print('sending to ', connection)
		connection.Send({"action": "action", "event": action, "player_name" : self.player_name})

	#######################################
	### Network event/message callbacks ###
	#######################################

	def Network_players(self, data):
		print("*** players: " + ", ".join([p for p in data['players']]))

	def Network_action(self, data):
		print('hey')
		print(data)
		self.actions[data["player_name"]].append(data["event"])

	# built in stuff

	def Network_connected(self, data):
		print("You are now connected to the server")

	def Network_error(self, data):
		print(data)
		print('error:', data['error'][1])
		connection.Close()

	def Network_disconnected(self, data):
		print('Server disconnected')
		exit()
