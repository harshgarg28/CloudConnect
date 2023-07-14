
import socket
import sys
import time
import json
import _thread
from datetime import datetime
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
com_port = 5556
server_address = ('', int(com_port))
print('connecting to %s port %s' % server_address, file=sys.stderr)

sock.bind(server_address)
sock.listen(5)
fileName = "";
try:
    while True:
        s, addr = sock.accept()
        data = s.recv(1024).decode() # receive up to 1024 bytes of data
        
        # converting to json object
        json_object = json.loads(data)
    	
        node_id = str(json_object["node_id"])
        
        if node_id == "fc:69:47:c:2b:63":
        	
        	data = data[2:-1]
        	
        	# current date and time
        	current_date_time = str(datetime.now())
        	
        	# current date
        	current_date = current_date_time[0:10]
        	
        	# current time
        	current_time = current_date_time[11:19]
        	
        	# converting to json object
        	j_date = {"date": current_date}
        	
        	# converting to json object
        	j_time = {"time": current_time}
        	
        	# concatenating two json object
        	json_object.update(j_date)
        	json_object.update(j_time)
        	
        	# converting json_object to string
        	json_string = str(json_object) + "\n"
        	
        	# Open a txt file for writing
        	with open('group_10.txt', 'a') as txtfile:
        		txtfile.write(json_string)
        
        	print(json_string)
        
        time.sleep(8)
        s.close()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()


