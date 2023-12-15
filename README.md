# Transfer Protocol
Transfer Protocol for transferring drone's coordinates and imagery to remote server via Web Sockets

## Image Transfer
![image](https://github.com/Frankovich/transfer_protocol/assets/91154822/b471678c-2ed3-4a6e-8a73-8ae4cd494c42)

### Server Image Listener Script

#### Overview
The Server Listener script is designed to receive images over a network connection. It sets up a server socket, listens for incoming connections, and processes received image data.

#### Functions

- **`startListener(host, port, commRate=1)`**
  - **Purpose:** Initializes and starts the server listener.
  - **Parameters:**
    - `host`: The IP address to bind the server to.
    - `port`: The port number on which the server will listen.
    - `commRate`: The communication rate in seconds, defaulting to 1 second.
  - **Functionality:** The function creates a socket and binds it to the specified host and port and then it listens for incoming connections and handles the reception of image data.

#### Main Execution Loop
- The script continuously attempts to start the server listener.
- If an exception occurs, it waits for 3 seconds before trying to reconnect.

### Image Transfer Script

#### Overview
The Image Transfer script is designed to send images to a remote server. It establishes a client socket, connects to the server, and transfers image files.

#### Functions

- **`connect(host="xxxx", port=8080)`**
  - **Purpose:** Establishes a connection to the server and sends images.
  - **Parameters:**
    - `host`: The IP address of the server.
    - `port`: The port number to connect to.
  - **Functionality:** The function attempts to connect to the server. Once connected, it reads an image file and sends its contents over the socket and it handles reconnection in case the connection is lost.

#### Main Execution Loop
- The script continuously attempts to connect to the server and transfer images.
- In case of a disconnection or an error, it will try to reconnect after a delay.

### Usage Instructions

1. **Server Listener Script**
   - Update `receiverConfig` with the correct IP and port settings.
   - Run the script on the machine designated as the server.

2. **Image Transfer Script**
   - Update `droneConfig` with the server's IP and port settings.
   - Place the image you want to transfer in the same directory as the script.
   - Update the `image` variable with the name of the image file.
   - Run the script on the client machine.

### Notes

- The scripts are designed to work at the same time, where the Image Transfer script acts as the client, and the Server Listener script acts as the server.
- These scripts assume a reliable network connection. In case of network instability, additional error handling may be necessary.

## Coordinate Transfer

### `coordReceiver.py` - Coordinate Receiver Script

#### Overview
The Coordinate Receiver script sets up a server to receive coordinate data over a network connection and this data is then logged into a file with timestamps.

#### Functions

- **`startListener(host, port, commRate=1)`**
  - **Purpose:** Initializes and starts the server listener for receiving coordinates.
  - **Parameters:**
    - `host`: The IP address to bind the server to.
    - `port`: The port number on which the server will listen.
    - `commRate`: The communication rate in seconds, defaulting to 1 second.
  - **Functionality:** The function creates a socket and binds it to the specified host and port. It listens for incoming connections and handles the reception of coordinate data, which is appended to a file along with timestamps.

#### Main Execution Loop
- The script continuously runs the `startListener` function.
- It attempts to start the server listener and restarts it in case of exceptions.

### `coordTransfer.py` - Coordinate Transfer Script

#### Overview
The Coordinate Transfer script is designed to send coordinate data to a remote server. It establishes a client socket, connects to the server, and transfers coordinate data regularly.

#### Functions

- **`connect(host, port)`**
  - **Purpose:** Establishes a connection to the server and sends coordinate data.
  - **Parameters:**
    - `host`: The IP address of the server.
    - `port`: The port number to connect to.
  - **Functionality:** The function attempts to connect to the server. Once connected, it repeatedly sends coordinate data obtained from a `Drone` object over the socket. It handles reconnection in case the connection is lost.

#### Main Execution Loop
- The script continuously attempts to connect to the server and transfer coordinate data.
- If the connection is lost or an error occurs, the script tries to reconnect after a delay.

### Usage Instructions

1. **Coordinate Receiver Script (`coordReceiver.py`)**
   - Update `receiverConfig` with the correct IP and port settings.
   - Run the script on the machine designated as the server.

2. **Coordinate Transfer Script (`coordTransfer.py`)**
   - Update `droneConfig` with the server's IP and port settings.
   - Ensure that the `Drone` class provides a method `statusExample()` that returns coordinate data in a string format.
   - Run the script on the client machine that will be sending the coordinate data.

### Notes

- The scripts are intended to work together, with `coordTransfer.py` acting as the client and `coordReceiver.py` as the server.
