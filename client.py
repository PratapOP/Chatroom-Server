import socket
import threading

# Server details
HOST = '127.0.0.1'
PORT = 12345

# Function to receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("Disconnected from server")
            client_socket.close()
            break

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Start a thread to listen for messages
thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

# Send messages
while True:
    message = input()
    client.send(message.encode('utf-8'))
    if message.lower() == 'exit':
        break
