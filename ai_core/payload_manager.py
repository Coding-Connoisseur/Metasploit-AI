# ai_core/payload_manager.py

import os

class PayloadManager:
    def __init__(self):
        self.payloads_dir = "payloads"
        os.makedirs(self.payloads_dir, exist_ok=True)

    def manage_payload(self, args):
        action = args[0]
        name = args[1] if len(args) > 1 else None
        payload = " ".join(args[2:]) if len(args) > 2 else None
        payload_path = os.path.join(self.payloads_dir, f"{name}.txt")

        if action == "create" and name and payload:
            with open(payload_path, 'w') as f:
                f.write(payload)
            return f"Payload {name} created."
        elif action == "list":
            return "\n".join(os.listdir(self.payloads_dir))
        elif action == "delete" and name:
            if os.path.exists(payload_path):
                os.remove(payload_path)
                return f"Payload {name} deleted."
            else:
                return f"Payload {name} not found."
        elif action == "view" and name:
            if os.path.exists(payload_path):
                with open(payload_path, 'r') as f:
                    return f.read()
            else:
                return f"Payload {name} not found."
        else:
            return "Invalid action or parameters."
