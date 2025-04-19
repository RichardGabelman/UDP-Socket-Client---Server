# UDP Client-Server Project
Group 9's submission for Programming Assignment 2 in Dr. Wang's CS576 @ SDSU

## **Features**
- Implements **UDP communication** over `localhost:9999`
- **Client sends dynamic user input** to server
- **Server responds with humorous reply**
- **Graceful shutdown** by sending the keyword `"exit"`
- **Error handling** for timeouts, malformed input, and disconnections

## **Requirements**
- Python 3.x installed
- Runs **locally** on `127.0.0.1`

## **How to Run the Program**

### **Step 1: Start the Server**
Open a terminal and run:
```sh
python server.py
```
Expected output:
```
UDP server listening on localhost:9999
```

### **Step 2: Start the Client**
Open a terminal and run:
```sh
python client.py
```
Expected output:
```
Enter your message (type 'exit' to exit): Hello
[CLIENT] Sending message to server: Hello
[CLIENT] Received from server: Hello - Nah... you did not just send that...
```

### **Step 3: Exit**
To gracefully terminate the session:
```
Enter your message (type 'exit' to exit): exit
[CLIENT] Sending message to server: exit
[CLIENT] Received from server: Goodbye! Exiting
[CLIENT] Exit signal sent. Closing.
```
Server logs:
```
[SERVER] Received message from client: exit
[SERVER] Client requested exit.
```