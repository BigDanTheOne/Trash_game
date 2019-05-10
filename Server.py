from __future__ import print_function
from _thread import *
import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

class ClientChannel(Channel):
	"""
	This is the server representation of a single connected client.
	"""

	def __init__(self, *args, **kwargs):
		self.player_name = "unknown"
		Channel.__init__(self, *args, **kwargs)

	def Close(self):
		self._server.DelPlayer(self)

	##################################
	### Network specific callbacks ###
	##################################

	def Network_action(self, data):
		self._server.SendToAll(data)

	def Network_player_name(self, data):
		print(data, "  <<--------channel")
		self._server.SendPlayersOrder()

	def Network_all(self):
		self._server.SendPlayersOrder()


class GameServer(Server):
	channelClass = ClientChannel

	def __init__(self, *args, **kwargs):
		Server.__init__(self, *args, **kwargs)
		self.players = WeakKeyDictionary()
		print('Server launched')
		self.Launch()

	def Connected(self, channel, addr):
		print('someone connected')
		self.AddPlayer(channel)

	def AddPlayer(self, player):
		print("New Player" + str(player.addr))
		self.players[player] = True
		self.SendPlayers()
		print("players", [p for p in self.players])

	def DelPlayer(self, player):
		print("Deleting Player" + str(player.addr))
		del self.players[player]
		self.SendPlayers()

	def SendPlayers(self):
		self.SendToAll({"action": "players", "players": [p.nickname for p in self.players]})

	def SendToAll(self, data):
		for p in self.players:
			p.Send(data)

	def Launch(self):
		while True:
			self.Pump()
			if dict(self.players):
				print(dict(self.players))

s = GameServer(localaddr=('127.0.0.1', 34421))
