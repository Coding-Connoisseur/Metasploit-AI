# ai_core/session_manager.py

import os
import json

class SessionManager:
    def __init__(self):
        self.current_session = None

    def manage_session(self, args):
        action = args[0] if len(args) > 0 else None
        name = args[1] if len(args) > 1 else None
        session_dir = "sessions"
        os.makedirs(session_dir, exist_ok=True)
        session_path = os.path.join(session_dir, f"{name}.json")

        if action == "save" and name:
            if self.current_session:
                with open(session_path, 'w') as f:
                    json.dump(self.current_session, f)
                return f"Session {name} saved."
            else:
                return "No active session to save."
        elif action == "load" and name:
            if os.path.exists(session_path):
                with open(session_path, 'r') as f:
                    self.current_session = json.load(f)
                return f"Session {name} loaded."
            else:
                return f"Session {name} not found."
        elif action == "list":
            return "\n".join(os.listdir(session_dir))
        elif action == "delete" and name:
            if os.path.exists(session_path):
                os.remove(session_path)
                return f"Session {name} deleted."
            else:
                return f"Session {name} not found."
        else:
            return "Invalid action or parameters."
