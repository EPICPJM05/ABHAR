import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            # Connect to the server
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            self.listen()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def listen(self):
        try:
            while True:
                # Input message from user
                message = input("Enter message: ")
                # Send message to server
                self.client_socket.send(message.encode())
        except KeyboardInterrupt:
            print("Client disconnected.")
            self.client_socket.close()

if __name__ == "__main__":
    client = Client('localhost', 12345)
    client.connect()
