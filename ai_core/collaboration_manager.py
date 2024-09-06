# ai_core/collaboration_manager.py

import asyncio
import json
import websockets

class CollaborationManager:
    def __init__(self, ai):
        self.ai = ai
        self.clients = set()
        self.server = None

    async def start_server(self, host, port):
        self.server = await websockets.serve(self.handle_client, host, port)
        self.ai.logging_manager.log_info(f"Collaboration server started on {host}:{port}")

    async def handle_client(self, websocket, path):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                await self.process_message(message, websocket)
        finally:
            self.clients.remove(websocket)

    async def process_message(self, message, sender):
        data = json.loads(message)
        if data['type'] == 'chat':
            await self.broadcast(message, sender)
        elif data['type'] == 'action':
            result = self.ai.execute_command(data['command'])
            await self.broadcast(json.dumps({'type': 'action_result', 'result': result}), None)

    async def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                await client.send(message)

    def send_update(self, update_type, data):
        message = json.dumps({"type": update_type, "data": data})
        asyncio.create_task(self.broadcast(message, None))
