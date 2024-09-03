# ai_core/custom_payload_manager.py

import os
import json
from cryptography.fernet import Fernet

class CustomPayloadManager:
    def __init__(self, ai):
        self.ai = ai
        self.payloads_dir = "custom_payloads"
        os.makedirs(self.payloads_dir, exist_ok=True)
        self.payloads = self.load_payloads()
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def load_payloads(self):
        payloads = {}
        for file_name in os.listdir(self.payloads_dir):
            if file_name.endswith(".json"):
                with open(os.path.join(self.payloads_dir, file_name), 'r') as f:
                    payload_name = file_name[:-5]
                    payloads[payload_name] = json.load(f)
        return payloads

    def save_payload(self, name, payload):
        payload_path = os.path.join(self.payloads_dir, f"{name}.json")
        encrypted_payload = self.encrypt_payload(payload)
        with open(payload_path, 'w') as f:
            json.dump(encrypted_payload, f)
        self.payloads[name] = encrypted_payload
        self.ai.logging_manager.log_info(f"Saved encrypted custom payload: {name}")

    def encrypt_payload(self, payload):
        payload_json = json.dumps(payload).encode('utf-8')
        encrypted_payload = self.cipher.encrypt(payload_json)
        return encrypted_payload.decode('utf-8')

    def decrypt_payload(self, encrypted_payload):
        decrypted_payload = self.cipher.decrypt(encrypted_payload.encode('utf-8'))
        return json.loads(decrypted_payload.decode('utf-8'))

    def list_payloads(self):
        return list(self.payloads.keys())

    def get_payload(self, name):
        encrypted_payload = self.payloads.get(name, None)
        if encrypted_payload:
            return self.decrypt_payload(encrypted_payload)
        return None

    def delete_payload(self, name):
        payload_path = os.path.join(self.payloads_dir, f"{name}.json")
        if os.path.exists(payload_path):
            os.remove(payload_path)
            del self.payloads[name]
            self.ai.logging_manager.log_info(f"Deleted custom payload: {name}")
            return True
        return False
