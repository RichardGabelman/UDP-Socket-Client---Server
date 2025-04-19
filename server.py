import socket

# server configuration
SERVER_IP = 'localhost'
SERVER_PORT = 9999
BUFFER_SIZE = 1024
EXIT_KEYWORD = 'exit'

try:
    # create and bind UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    print(f"UDP server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        try:
            # receive message from client
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            message = data.decode('utf-8')
            print(f"[SERVER] Received message from client: {message}")

            # handle exit
            if message.lower() == EXIT_KEYWORD:
                print(f"[SERVER] Client requested exit.")
                response = "Goodbye! Exiting"
                server_socket.sendto(response.encode('utf-8'), client_address)
                continue

            # build humorous reply
            humorous_response = f"{message} - Nah... you did not just send that..."

            # send reply
            server_socket.sendto(humorous_response.encode('utf-8'), client_address)
            print(f"[SERVER] Replied to {client_address}")
        
        except Exception as err:
            print(f"[SERVER] Failed to process message {err}")

except Exception as e:
    print(f"[SERVER] There was an error {e}")

finally:
    server_socket.close()