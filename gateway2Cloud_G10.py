import socket
import time

# creating the sock object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket successfully created')
# vm communication port
communcation_port = 5555
# vm ip address
ip_address = '172.29.0.207'
server_address = (ip_address, communcation_port)
# connecting to the server
sock.connect(server_address)
print('Connected with server', ip_address)

try:
    # file name of txt file
    file_name = 'group_10.txt'

    while True:
        # read the next line of data from the file
        with open(file_name, 'r') as f:
            line = f.readline().strip()

        if not line:
            # if there is no more data in the file, wait for 1 second before checking again
            time.sleep(1)
            continue

        try:
            # send the line of data to the server
            sock.sendall(line.encode())
            time.sleep(1)
            print(f"Sent data to {ip_address}:{communcation_port}: {line}")

            # remove the sent line from the file
            with open(file_name, 'r') as f:
                lines = f.readlines()
            with open(file_name, 'w') as f:
                for l in lines:
                    if l.strip() != line:
                        f.write(l)

        except:
            # if there is an error sending the data, wait for 10 seconds before trying again
            print(f"Error sending data to {ip_address}:{communcation_port}: {line}")
            time.sleep(10)
            continue

except KeyboardInterrupt:
    # if the user presses Ctrl+C, close the connection and exit the program
    print('User interrupted')
    sock.close()

except:
    # if there is an error, print a message and close the connection
    print('Error in sending file to gateway ' + ip_address + ' at port ' + str(communcation_port))
    sock.close()

