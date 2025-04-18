import socket

# Set up client
SERVER_IP = 'localhost'
SERVER_PORT = 9999
CLIENT_PORT = 0
MESSAGE = "Hello server!"
BUFFER_SIZE = 1024

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', CLIENT_PORT))

print(f"Sending message to server: {MESSAGE}")
client_socket.sendto(MESSAGE.encode('utf-8'), (SERVER_IP, SERVER_PORT))

response, _ = client_socket.recvfrom(BUFFER_SIZE)
print(f"Received from server: {response.decode('utf-8')}")

