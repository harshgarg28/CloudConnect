import socket			
import time
import json
import sys
import psycopg2

conn = psycopg2.connect(
    dbname="group_10",
    user="postgres",
    password="test",
    host="172.29.0.207"
)

cur = conn.cursor()


# creating a socket object
server_socket = socket.socket()		

print ("Socket successfully created")

# gateway listing port
l_port = 5555			

# reciving data from all ip or can be specified as sender_ip = 'x.x.x.x'
sender_ip = ''

server_address = (sender_ip,l_port)


print('connecting to %s port %s' % server_address, file=sys.stderr)


# Next bind to the port
server_socket.bind(server_address)		

# put the socket into listening mode
server_socket.listen(5) 	
print ("socket is listening")		

# accept a client connection
client_socket, client_address = server_socket.accept()
	
print ('Got connection from', client_address )

while True:
    
    data = client_socket.recv(1024).decode()
    
        	
    new_string = data.replace("'", "\"")
    
    json_object = json.loads(new_string)  
    
    temp = str(json_object['temp'])
    humi = str(json_object['humi'])
    node_id = str(json_object['node_id'])
    device = str(json_object['device'])
    date = str(json_object['date'])
    time = str(json_object['time'])
    
    print(json_object)
    
    cur.execute("INSERT INTO group_10_data (temp, humi, node_id, device, date, time) VALUES (%s, %s, %s,%s,%s,%s)", (temp, humi, node_id, device, date, time))
    
    # Commit the changes to the database:
    conn.commit()
    
    
   
    
    # converting to json object
    #json_object = json.loads(data)
    
    print(data)
    


# Close the connection with the client
client_socket.close()

# Close server socket 
server_socket.close()



# Note :- when we run server_socket.accept() in while loop it will take only one entry 
