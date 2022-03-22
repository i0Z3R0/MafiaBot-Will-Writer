import string
import os
import re
import random

def msg(message, Player1, Player2):
	global players
	newmsg = ''
	matches = ["PLAYER1", "PLAYER2"]
	if any(x in message for x in matches):
		newmsg = message.replace("PLAYER1", Player1)
		print("Replaced PLAYER1 with " + Player1)
		newmsg = newmsg.replace("PLAYER2", Player2)
		print("Replaced PLAYER2 with " + Player2)
		return newmsg
	elif "PLAYERX" in message:
		# First check for PLAYERX, so player can be removed
		preplace = random.choice([Player1, Player2])
		newmsg = message.replace("PLAYERX", preplace)
		print("Replaced PLAYERX with " + preplace)
		players.remove(preplace)
		print(f'Removed {preplace} from players')
		return newmsg
	elif "PLAYER" in message:
		preplace = random.choice([Player1, Player2])
		newmsg = message.replace("PLAYER", preplace)
		print("Replaced PLAYER with " + preplace)
		return newmsg
	else:
		newmsg = message
		return newmsg
		

players = []
pl = False

c = input("Parse players from rawplayers.txt? (y/n) ")
if c.lower() == "y" or c.lower() == "yes":
	f = open("rawplayers.txt", "r")
	for line in f:
		if pl == False:
			# Party Leader
			players.append(line.strip("\n")[16:])
			pl = True
		else:
			players.append(line.strip("\n")[2:])
	f.close()
	
	for i in range(len(players)):
		tpos = players[i].find(' - "')
		if tpos != -1:
			players[i] = players[i][0:tpos]
	for i in range(len(players)):
		players[i] = re.sub(r'[^A-Za-z0-9 ]+', '', players[i]).strip()
	
	g = open("players.txt", "w")
	for p in players:
		#print(p)
		g.write(p + "\n")
	g.close()
elif c.lower() == "n" or c.lower() == "no":
	print("Fetching players from players.txt")
	g = open("players.txt", "r")
	for p in g:
		#print(p)
		players.append(p.strip("\n"))
	g.close()

# Subsitution
j = open("messages.txt", "r")
messages = []
for line in j:
	messages.append(line.strip("\n"))
j.close()
# Shuffles the messages
random.shuffle(messages)

will = []
for message in messages:
	tmp1 = random.choice(players)
	tmp2 = random.choice(players)
	while tmp2 == tmp1:
		tmp2 = random.choice(players)
	willmsg = msg(message, tmp1, tmp2)
	print(f'Next Line in Will: {willmsg}\n')
	will.append(willmsg)
will.append("I died wtf")

for n in range(len(will)):
	will[n] = f'N{n + 1} | {will[n]}'

# Commented out for now, already shuffled in the beginning
# This keeps consistency (e.g.: Lethaled Player, then watched them the next night???)
#random.shuffle(will)
print("\n\n\n\n\n")
willtxt = ""
k = open("fullwill.txt", "w")
for w in will:
	#print(w)
	k.write(w + "\n")
	willtxt = willtxt + w + "\n"

print(willtxt.strip("\n"))

# Mafiabot allows only 286 characters for some weird reason…