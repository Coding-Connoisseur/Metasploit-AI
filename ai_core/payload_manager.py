# ai_core/payload_manager.py

import os
import json
from cryptography.fernet import Fernet

class PayloadManager:
    def __init__(self, ai):
        self.ai = ai
        self.payloads_dir = "payloads"
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
        self.ai.logging_manager.log_info(f"Saved encrypted payload: {name}")

    def encrypt_payload(self, payload):
        payload_json = json.dumps(payload).encode('utf-8')
        encrypted_payload = self.cipher.encrypt(payload_json)
        return encrypted_payload.decode('utf-8')

    def decrypt_payload(self, encrypted_payload):
        decrypted_payload = self.cipher.decrypt(encrypted_payload.encode('utf-8'))
        return json.loads(decrypted_payload.decode('utf-8'))

    def create_modular_payload(self, base_payload, modules):
        modular_payload = base_payload
        for module in modules:
            modular_payload = self.apply_module(modular_payload, module)
        self.ai.logging_manager.log_info(f"Created modular payload: {modular_payload}")
        return modular_payload

    def apply_module(self, payload, module):
        # Placeholder logic for applying a module to the payload
        # This should be replaced with actual module application logic
        return f"{payload}-{module}"

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
            self.ai.logging_manager.log_info(f"Deleted payload: {name}")
            return True
        return False
