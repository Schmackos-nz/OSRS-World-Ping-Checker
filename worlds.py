"""
OSRS Server Ping Checker
Python 3.6
Schmackos-nz on Github
"""

import os

recommend = 1
recommendPing = 1000

additionalServers = [100, 117] # servers that aren't in sequential order

def getResponse(server):
    actualServer = "oldschool" + str(server) + ".runescape.com"
    ret = os.system("ping " + actualServer + " -l 0 -n 1 | findstr /rc:\"time=[0-9]*ms\" > c.txt") # ping server with 0 length and only once and output result into c.txt, using findstr to reduce parsing

    f = open("c.txt", "r")
    ping = f.read()

    msStart = ping.find("time=") + 5 # look for time (aka ping) and add 5 to exclude time=
    msEnd = ping.find("ms", msStart) # look for ms after time=
    msPing = ping[msStart:msEnd] # ping value which is between time= and ms (eg. time=100ms returns 100)

    recommendWorld(server, msPing) # check if this server has better ping than the last ones... etc
    print("World " + str(server) + " = " + msPing + "ms") # output the servers ping

def recommendWorld(server, ping):
    global recommendPing, recommend
    if int(ping) <= int(recommendPing):
        recommend = server
        recommendPing = ping

def servers():
    for i in range(1, 95): # check the first 95 servers
        getResponse(i)
    for p in additionalServers: # check servers that don't come after 95 sequentially
        getResponse(p)

def start():
    servers()

print ("OSRS Server Ping Checker")
print ("By Schmackos-nz on Github\n")
start()
print ("\nWorld " + str(recommend) + " has the best ping with " + str(recommendPing) + "ms.")
print ("\nThat's all the servers done :3")