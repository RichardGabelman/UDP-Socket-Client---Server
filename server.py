import socket

# Set up server
SERVER_IP = 'localhost'
SERVER_PORT = 9999
BUFFER_SIZE = 1024

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"UDP server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    message = data.decode('utf-8')
    print(f"Received message from client: {message}")

    humorous_response = f"{message} - Nah... you did not just send that..."

    server_socket.sendto(humorous_response.encode('utf-8'), client_address)

