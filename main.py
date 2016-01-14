import client
import socket
import options
import sys

if len(sys.argv) > 1:
	if sys.argv[1] == 'start':
		client.clientLaunch()
	elif sys.argv[1] == 'configure':
		print ("All configurations stored in options.py file")
	elif sys.argv[1] == 'help':
		print ("""start - start the program
configure - configure the program""")
