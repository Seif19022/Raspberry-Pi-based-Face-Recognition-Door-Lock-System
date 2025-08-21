import socket
import pyttsx3

# Real-time notification setup
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000

engine = pyttsx3.init()

# Function to speak the notification
def speak_notification(message):
    engine.say(message)
    engine.runAndWait()

# Server setup
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Listening for notifications on {HOST}:{PORT}...")

    while True:
        client_socket, address = server_socket.accept()
        with client_socket:
            print(f"Connection from {address}")
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {message}")
            speak_notification(message)
