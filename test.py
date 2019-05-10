from Client import *

client1 = Client('127.0.0.1', 34421, 'fuck')
#client2 = Client('127.0.0.1', 34421, 'you')
client1.send_action(123)
client1.Update()
#client2.Update()
client1.get_action()
print(client1.actions)