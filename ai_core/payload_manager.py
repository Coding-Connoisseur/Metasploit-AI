# ai_core/payload_manager.py

import os
import json

class PayloadManager:
    def __init__(self, ai):
        self.ai = ai
        self.payloads_dir = "payloads"
        os.makedirs(self.payloads_dir, exist_ok=True)
        self.payloads = self.load_payloads()

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
        with open(payload_path, 'w') as f:
            json.dump(payload, f)
        self.payloads[name] = payload
        self.ai.logging_manager.log_info(f"Saved payload: {name}")

    def list_payloads(self):
        return list(self.payloads.keys())

    def get_payload(self, name):
        return self.payloads.get(name, None)

    def delete_payload(self, name):
        payload_path = os.path.join(self.payloads_dir, f"{name}.json")
        if os.path.exists(payload_path):
            os.remove(payload_path)
            del self.payloads[name]
            self.ai.logging_manager.log_info(f"Deleted payload: {name}")
            return True
        return False
