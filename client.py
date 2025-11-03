# Josephine Lyou
# ZeroMQ as communication pipeline

# client sending request to server

import zmq
context = zmq.Context()
print("Client attempting to connect to server...")

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# request a value from server
print(f"Sending a request...")

socket.send_string("Generate the exact statement for Assignment 4")

message = socket.recv()

print(f"{message.decode()}")

# end server
socket.send_string("Q")