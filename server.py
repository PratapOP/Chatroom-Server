import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port for communication

# List to store connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Function to handle client communication
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)  # Receive message
            if not message:
                break
            broadcast(message, client_socket)  # Send to all clients
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Main server function
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)  # Max 5 pending connections
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        
        # Start a new thread for the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Run the server
start_server()