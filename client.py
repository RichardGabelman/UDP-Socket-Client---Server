import socket

# client configuration
SERVER_IP = 'localhost'     # server address (loopback)
SERVER_PORT = 9999          # server listening port
CLIENT_PORT = 0             # 0 = OS assign random port
BUFFER_SIZE = 1024          # max size of response to receive (bytes)
EXIT_KEYWORD = 'exit'       # server sends this to end client loop

try:
    # create and bind UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('', CLIENT_PORT)) # bind socket to all local interfaces ''
    client_socket.settimeout(10) # wait 10 seconds max for server response

    while True:
        # get user input
        message = input("Enter your message (type 'exit' to exit): ")
        if not message:
            print(f"[CLIENT] Empty message skipped.")
            continue

        # send to server
        print(f"[CLIENT] Sending message to server: {message}")
        client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

        try:
            # receive response
            response, _ = client_socket.recvfrom(BUFFER_SIZE)
            decoded_response = response.decode('utf-8')
            print(f"[CLIENT] Received from server: {decoded_response}")
        except socket.timeout:
            print(f"[CLIENT] No response from server (timed out).")

        # handle exit
        if message.lower() == EXIT_KEYWORD:
            print("[CLIENT] Exit signal sent. Closing.")
            break

except Exception as e:
    print(f"[CLIENT] There was an error {e}")

finally:
    client_socket.close()