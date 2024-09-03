# ai_core/collaboration_manager.py

import socket
import threading

class CollaborationManager:
    def __init__(self, ai):
        self.ai = ai
        self.clients = []
        self.server_socket = None

    def start_server(self, host='0.0.0.0', port=5555):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Collaboration server started on {host}:{port}")
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"New client connected from {addr}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received message: {message}")
                    self.broadcast(message, client_socket)
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                client.send(message.encode())

    def send_message(self, message):
        for client in self.clients:
            client.send(message.encode())
