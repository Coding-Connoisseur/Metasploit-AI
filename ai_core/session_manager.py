# ai_core/session_manager.py

import os
import json

class SessionManager:
    def __init__(self, ai):
        self.ai = ai
        self.sessions_dir = "sessions"
        os.makedirs(self.sessions_dir, exist_ok=True)
        self.active_session = None

    def handle_session_command(self, args):
        action = args[0]
        name = args[1] if len(args) > 1 else None

        if action == "save":
            return self.save_session(name)
        elif action == "load":
            return self.load_session(name)
        elif action == "list":
            return self.list_sessions()
        elif action == "delete":
            return self.delete_session(name)
        else:
            return "Invalid session command."

    def save_session(self, name):
        if not name:
            return "No session name provided."
        session_path = os.path.join(self.sessions_dir, f"{name}.json")
        session_data = {
            "cwd": self.ai.cwd,
            "actions": self.ai.logging_manager.get_session_actions(),
        }
        with open(session_path, 'w') as f:
            json.dump(session_data, f)
        self.active_session = name
        self.ai.logging_manager.log_info(f"Session '{name}' saved.")
        return f"Session '{name}' saved."

    def load_session(self, name):
        if not name:
            return "No session name provided."
        session_path = os.path.join(self.sessions_dir, f"{name}.json")
        if not os.path.exists(session_path):
            return f"Session '{name}' not found."
        with open(session_path, 'r') as f:
            session_data = json.load(f)
        self.ai.cwd = session_data.get("cwd", self.ai.cwd)
        self.ai.logging_manager.log_info(f"Session '{name}' loaded.")
        self.active_session = name
        return f"Session '{name}' loaded."

    def list_sessions(self):
        sessions = os.listdir(self.sessions_dir)
        return "\n".join(sessions) if sessions else "No sessions found."

    def delete_session(self, name):
        if not name:
            return "No session name provided."
        session_path = os.path.join(self.sessions_dir, f"{name}.json")
        if os.path.exists(session_path):
            os.remove(session_path)
            self.ai.logging_manager.log_info(f"Session '{name}' deleted.")
            return f"Session '{name}' deleted."
        else:
            return f"Session '{name}' not found."
