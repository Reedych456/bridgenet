import socket
import options

def server():
	# Is user want to start server or be client only?
	
	if options.serverStart == True:
		print ("Starting server")
		print ("Creating socket")
	
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((options.serverHost, options.serverPort))
		server.listen(8)
	
		#connection, address = server.accept()
	
		print ("Server started")