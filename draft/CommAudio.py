import socket
import threading

# Server IP address and port
SERVER_IP = "192.168.1.5"
PORT = 5555

# List to store connected clients
clients = []

# Function to handle messages from a client
def handle_client(client_socket):
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            # Broadcast message to all clients
            broadcast(message)
    except Exception as e:
        print("Error:", e)
        # Remove the client from the list if an error occurs
        if client_socket in clients:
            clients.remove(client_socket)

# Function to broadcast a message to all clients
def broadcast(message):
    for client_socket in clients:
        try:
            client_socket.send(bytes(message, "utf-8"))
        except Exception as e:
            print("Error broadcasting message to a client:", e)
            # Remove the client from the list if an error occurs
            if client_socket in clients:
                clients.remove(client_socket)

# Function to accept incoming connections
def accept_connections():
    try:
        while True:
            client_socket, client_address = server.accept()
            print("Connected to:", client_address)
            
            # Add the client socket to the list
            clients.append(client_socket)
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
            
            # Send a welcome message to the client
            client_socket.send(bytes("\t--Server Online--", "utf-8"))
            print("I reached Here")
    except OSError as e:
        # Handle OSError, which might occur if the server socket is closed
        print("OSError:", e)
    except Exception as e:
        # Handle other exceptions
        print("Error accepting connections:", e)


# Function to handle messages from the server
def handle_server_messages():
    try:
        while True:
            message = input("Server: ")
            broadcast(message)
    except KeyboardInterrupt:
        print("Server stopped")

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server IP and port
server.bind((SERVER_IP, PORT))

# Listen for incoming connections
server.listen(10)

print("Server is listening on port", PORT)

# Start accepting connections
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()


# Start handling server messages
handle_server_messages()
