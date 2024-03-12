import socket

# Server IP address and port
server_ip = "192.168.6.169"
port = 5555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server IP and port
server_socket.bind((server_ip, port))

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for connection...")

# Accept connection from client
client_socket, client_address = server_socket.accept()

print("Connected to:", client_address)

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()

    if not message:
        break

    print("Client:", message)

    # Send response
    response = input("Server: ")
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
