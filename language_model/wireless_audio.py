import socket
import sounddevice as sd
import numpy as np

# Server IP address and port
server_ip = "192.168.137.1"
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

# Function to receive audio from client
def receive_audio(indata, frames, time, status):
    audio_data = (indata * 32767).astype(np.int16).tobytes()
    client_socket.send(audio_data)

# Start audio stream
with sd.InputStream(callback=receive_audio):
    while True:
        pass

# Close the connection
client_socket.close()
server_socket.close()
