# MafiaBot-Will-Writer
A super simple single-purpose tool to generate stupidly hilariously funnily dumb wills for MafiaBot on Discord, used usually when you're Jester or Mafia or a Neutral role, or just want to troll. 

MafiaBot Wiki: https://mafiabot.fandom.com/wiki/MafiaBot_Wiki

MafiaBot Support Server: https://discord.gg/2bnpcx8

MafiaBot Community Server: https://discord.gg/V8s9t5Gf9g

The wiki, support server, and community server links are taken directly from MafiaBot's `m.info` command. 

# Installation
1. git clone https://github.com/i0Z3R0/MafiaBot-Will-Writer.git
2. cd MafiaBot-Will-Writer
##### Note: no installation of libraries necessary

# Usage
1. Paste in players from `m.party` into rawplayers.txt or edit players.txt and enter each player individually.
2. Edit messages.txt if you want to add / remove / change the default messages. 
3. python3 main.py
## Messages Format
Messages are seperated by a new line. PLAYER is replaced with a random player, PLAYER1 and PLAYER2 will be replaced by two different random players, and PLAYERX will be replaced by a random player BUT this player will not appear again for the rest of the will. Useful for consistencies with baiting, killing, shooting, etc. 

Death messages follow the same format. 

##### Note: Death messages not implemented as of right now