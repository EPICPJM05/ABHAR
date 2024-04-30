import socket
import threading
import time
import sys

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            # Bind the server socket to the host and port
            self.server_socket.bind((self.host, self.port))
            # Listen for incoming connections
            self.server_socket.listen(5)
            print(f"Server listening on {self.host}:{self.port}...")

            # Accept incoming connections and handle them in separate threads
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"New connection from {address}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_thread.start()
                self.clients.append((client_socket, address))
        except Exception as e:
            print(f"Error starting server: {e}")

    def handle_client(self, client_socket, address):
        try:
            while True:
                # Receive message from client
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Received message from {address}: {message}")

                # Broadcast message to all clients
                for client in self.clients:
                    if client[0] != client_socket:  # Exclude the sender
                        client[0].send(message.encode())
        except Exception as e:
            print(f"Error handling client {address}: {e}")
        finally:
            # Remove client from the list when disconnected
            self.clients.remove((client_socket, address))
            client_socket.close()

    def send_auto_messages(self, interval=5):
        try:
            while True:
                time.sleep(interval)
                auto_message = input("This is an automated message from the server.")
                print(f"Sending automated message: {auto_message}")
                for client in self.clients:
                    client[0].send(auto_message.encode())
        except Exception as e:
            print(f"Error sending automated messages: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = '0.0.0.0'  # Listen on all available interfaces

    server = Server(host, 12345)
    threading.Thread(target=server.send_auto_messages).start()  # Start auto message sender thread
    server.start()
