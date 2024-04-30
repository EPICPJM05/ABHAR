import socket
import threading

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

            # Start receiving messages from the server in a separate thread
            threading.Thread(target=self.receive_messages).start()
            
            # Start sending messages to the server
            self.send_messages()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def receive_messages(self):
        try:
            while True:
                # Receive message from server
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print("Server:", message)
        except Exception as e:
            print(f"Error receiving messages from server: {e}")
        finally:
            self.client_socket.close()

    def send_messages(self):
        try:
            cnt=0
            while True:
                if(cnt==0):
                    client_name = input("Enter your name: ")
                    self.client_socket.send(client_name.encode())
                    cnt+=1
                # Input message from user
                message = input("You: ")
                # Send message to serverh
                self.client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending messages to server: {e}")
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    server_ip = input("Enter the server's IP address: ")
    # client_name = input("Enter your name: ")
    client = Client(server_ip, 12345)
    client.connect()